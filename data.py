import argparse
import logging
import os
import re

from yaml import dump, load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


class PairingException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ItemData:
    def __init__(
        self, items_file_name: str | None = None, stats_file_name: str | None = None
    ):
        self.stat_price = {}
        self.stats_file_name = stats_file_name or "stats.yml"
        self.items_file_name = items_file_name or "items.yml"

        self.datas = self.read_yaml(self.items_file_name)
        self.bases = self.read_bases()

    def get_abs_filename(self, file_name: str) -> str:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, f"./_data/{file_name}")

        return file_path

    def write_yaml(self, file_name: str):
        logging.debug(f"write `datas` into {file_name}")
        file_path = self.get_abs_filename(file_name)

        with open(file_path, "w") as f:
            dump(self.datas, f, Dumper=Dumper)

    def read_yaml(self, file_name: str):
        logging.debug(f"read `datas` from {file_name}")
        file_path = self.get_abs_filename(file_name)

        with open(file_path, "r") as f:
            return load(f, Loader=Loader)

    def find_data_with_name(self, datas, name: str):
        for data in datas:
            if data["name"] == name:
                return data

    def find_stat_with_type(self, data, _type: str):
        _sum = 0

        for stat in data["stats"]:
            if stat["type"] == _type:
                _sum += stat["value"]

        return _sum

    def read_bases(self):
        stats = self.read_yaml(self.stats_file_name)
        bases = {"first": {}, "second": {}}

        for stat in stats:
            if "base_type" in stats[stat] and stats[stat]["base_type"] not in ["exclude"]:
                bases[stats[stat]["base_type"]][stat] = stats[stat]["base_item"]

        return bases

    def calculate_base_statistic_prices(self):
        logging.debug("calculate base statistic prices")

        datas = self.datas

        first_base = self.bases["first"]
        second_base = self.bases["second"]

        logging.debug("  - first base")
        for _type in first_base:
            _name = first_base[_type]

            data = self.find_data_with_name(datas, _name)
            target_stat = self.find_stat_with_type(data, _type)
            if not (data and target_stat):
                raise ValueError(f"data: {data}, target_stat: {target_stat}")
            cost = data["cost"]

            stat_cost = float("{:.2f}".format(cost / target_stat))
            data["first_base"] = {
                "type": _type,
                "value": stat_cost,
                "formula": f"{data['cost']}/{target_stat}",
            }
            self.stat_price[_type] = stat_cost

        logging.debug("  - second base")
        for _type in second_base:
            _name = second_base[_type]

            data = self.find_data_with_name(datas, _name)
            target_stat = self.find_stat_with_type(data, _type)
            if not (data and target_stat):
                raise ValueError(f"data: {data}, target_stat: {target_stat}")
            cost = data["cost"]

            formula_minus_part = ""
            for stat in data["stats"]:
                if stat["type"] != _type:
                    cost -= stat["value"] * self.stat_price[stat["type"]]
                    formula_minus_part += (
                        f"-{stat['value']}*{self.stat_price[stat['type']]}"
                    )

            stat_cost = float("{:.2f}".format(cost / target_stat))
            data["second_base"] = {
                "type": _type,
                "value": stat_cost,
                "formula": f"({data['cost']}{formula_minus_part})/{target_stat}",
            }
            self.stat_price[_type] = stat_cost

        self.datas = datas
        logging.debug("write `datas` into yml")
        self.write_yaml(self.items_file_name)

    def calculate_gold_efficiency(self):
        logging.debug("calculate gold efficiency based on base statistic prices")

        datas = self.datas

        if not self.stat_price:
            for data in datas:
                if "first_base" in data:
                    self.stat_price[data["first_base"]["type"]] = data["first_base"][
                        "value"
                    ]
                if "second_base" in data:
                    self.stat_price[data["second_base"]["type"]] = data["second_base"][
                        "value"
                    ]
        stat_price = self.stat_price

        for data in datas:
            if not ("first_base" in data or "second_base" in data):
                worth = 0
                formula_bonus_part = ""
                for stat in data["stats"]:
                    if "value" in stat:
                        if "ratio" in stat:
                            ref_base = 0
                            if "ref_type" in stat:
                                for _stat in data["stats"]:
                                    if (
                                        "ratio" not in _stat
                                        and _stat["type"] == stat["ref_type"]
                                    ):
                                        ref_base += _stat["value"]
                            if ref_base and "ref" in stat:
                                stat["value"] = (stat["ref"] + ref_base) * stat["ratio"]
                                stat["formula"] = (
                                    f'({stat["ref"]}+{ref_base})*{stat["ratio"]}'
                                )
                            elif ref_base:
                                stat["value"] = ref_base * stat["ratio"]
                                stat["formula"] = f'{ref_base}*{stat["ratio"]}'
                            elif "ref" in stat:
                                stat["value"] = stat["ref"] * stat["ratio"]
                                stat["formula"] = f'{stat["ref"]}*{stat["ratio"]}'
                            stat["value"] = float("{:.2f}".format(stat["value"]))

                        worth += stat["value"] * stat_price.get(stat["type"], 0)
                        formula_bonus_part += f"{'+' if formula_bonus_part else ''}{stat['value']}*{stat_price.get(stat['type'], 0)}"
                amount = "{:.2f}".format(worth / data["cost"] * 100) + "%"
                data["amount"] = amount
                data["formula"] = (
                    f"({formula_bonus_part if formula_bonus_part else '0'})/{data['cost']}"
                )
            else:
                data["amount"] = "100%"
                data["formula"] = "Base Item"

        self.datas = datas
        self.write_yaml(self.items_file_name)

    def clean_base_GE(self):
        logging.debug("Clean gold efficiency and base statistic price from item data")
        if self.datas:
            datas = self.datas
        else:
            datas = self.read_yaml(self.items_file_name)

        cleared_datas = []

        for data in datas:
            new_data = dict()
            for key in ("category", "cost", "image", "name", "stats"):
                new_data[key] = data[key]
            cleared_datas.append(new_data)

        self.datas = cleared_datas
        self.write_yaml(self.items_file_name)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Extract data from WR Meta via web scraping, or calculate the gold efficiency of item data."
    )
    parser.add_argument("--items", help="The file storage item data")
    parser.add_argument("--stats", help="The file storage stat data")
    parser.add_argument(
        "--clean_only",
        action="store_true",
        help="Only clean gold efficiency and base statistic price from item data",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    return parser.parse_args()


def setup_logger(debug_mode):
    logging.basicConfig(
        level=logging.DEBUG if debug_mode else logging.INFO,
        format="%(asctime)s %(filename)s %(levelname)s %(message)s",
        datefmt="%a %d %b %Y %H:%M:%S",
    )


def process_item_data(items_file, stats_file, clean_only):
    item_data = ItemData(items_file_name=items_file, stats_file_name=stats_file)

    if clean_only:
        item_data.clean_base_GE()
    else:
        item_data.clean_base_GE()
        item_data.calculate_base_statistic_prices()
        item_data.calculate_gold_efficiency()


def find_and_process_files(clean_only):
    datas = next(os.walk("./_data"), (None, None, []))[2]
    pattern = re.compile(r"^(items|stats)_(.+)\.yml$")
    parsed_files = {}

    for data in datas:
        match = pattern.match(data)
        if match:
            file_type, patch = match.groups()
            if patch not in parsed_files:
                parsed_files[patch] = {}
            parsed_files[patch][file_type] = data

    for key, value in sorted(parsed_files.items()):
        try:
            if "items" in value and "stats" in value:
                process_item_data(value["items"], value["stats"], clean_only)
                logging.info(f"finished: ({value['items']}, {value['stats']})")
                logging.debug("\n")
            else:
                raise PairingException(f"No matching pair for patch number {key}")
        except PairingException as e:
            print(e)


def main():
    args = parse_arguments()
    setup_logger(args.debug)

    if args.items and args.stats:
        process_item_data(args.items, args.stats, args.clean_only)
        logging.info(f"finished: ({args.items}, {args.stats})")
    elif not args.items and not args.stats:
        find_and_process_files(args.clean_only)
    else:
        logging.error("Both items and stats files must be provided together.")


if __name__ == "__main__":
    main()
