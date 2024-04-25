import argparse
import logging
import os

from yaml import dump, load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


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
        logging.info(f"write `datas` into {file_name}")
        file_path = self.get_abs_filename(file_name)

        with open(file_path, "w") as f:
            dump(self.datas, f, Dumper=Dumper)

    def read_yaml(self, file_name: str):
        logging.info(f"read `datas` from {file_name}")
        file_path = self.get_abs_filename(file_name)

        with open(file_path, "r") as f:
            return load(f, Loader=Loader)

    def find_data_with_name(self, datas, name: str):
        for data in datas:
            if data["name"] == name:
                return data

    def find_stat_with_type(self, data, _type: str):
        for stat in data["stats"]:
            if stat["type"] == _type:
                return stat

    def read_bases(self):
        stats = self.read_yaml(self.stats_file_name)
        bases = {"first": {}, "second": {}}

        for stat in stats:
            if "base_type" in stats[stat]:
                bases[stats[stat]["base_type"]][stat] = stats[stat]["base_item"]

        return bases

    def calculate_base_statistic_prices(self):
        logging.info("calculate base statistic prices")

        datas = self.datas

        first_base = self.bases["first"]
        second_base = self.bases["second"]

        logging.info("  - first base")
        for _type in first_base:
            _name = first_base[_type]

            data = self.find_data_with_name(datas, _name)
            target_stat = self.find_stat_with_type(data, _type)
            if not (data and target_stat):
                raise ValueError(f"data: {data}, target_stat: {target_stat}")
            cost = data["cost"]

            stat_cost = float("{:.2f}".format(cost / target_stat["value"]))
            data["first_base"] = {
                "type": _type,
                "value": stat_cost,
                "formula": f"{data['cost']}/{target_stat['value']}={stat_cost}",
            }
            self.stat_price[_type] = stat_cost

        logging.info("  - second base")
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

            stat_cost = float("{:.2f}".format(cost / target_stat["value"]))
            data["second_base"] = {
                "type": _type,
                "value": stat_cost,
                "formula": f"({data['cost']}{formula_minus_part})/{target_stat['value']}={stat_cost}",
            }
            self.stat_price[_type] = stat_cost

        self.datas = datas
        logging.info("write `datas` into yml")
        self.write_yaml(self.items_file_name)

    def calculate_gold_efficiency(self):
        logging.info("calculate gold efficiency based on base statistic prices")

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
                formula_bonux_part = ""
                for stat in data["stats"]:
                    worth += stat["value"] * stat_price.get(stat["type"], 0)
                    formula_bonux_part += f"{'+' if formula_bonux_part else ''}{stat['value']}*{stat_price.get(stat['type'], 0)}"
                amount = "{:.2f}".format(worth / data["cost"] * 100) + "%"
                data["amount"] = amount
                data["formula"] = (
                    f"({formula_bonux_part if formula_bonux_part else '0'})/{data['cost']}={amount}"
                )
            else:
                data["amount"] = "100%"
                data["formula"] = "Base Item"

        self.datas = datas
        self.write_yaml(self.items_file_name)

    def clean_base_GE(self):
        logging.info("Clean gold efficiency and base statistic price from item data")
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract data from WR Meta via web scraping, or calculate the gold efficiency of item data."
    )
    parser.add_argument("--items", help="The file storage item data")
    parser.add_argument("--stats", help="The file storage stat data")
    parser.add_argument(
        "-c",
        "--calculate",
        action="store_true",
        help="Calculate the gold efficiency of item data",
    )
    parser.add_argument(
        "--clean_only",
        action="store_true",
        help="Only clean gold efficiency and base statistic price from item data",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

    item_data = ItemData(items_file_name=args.items, stats_file_name=args.stats)

    if args.clean_only is True:
        item_data.clean_base_GE()
    else:
        if args.calculate is True:
            item_data.clean_base_GE()
            item_data.calculate_base_statistic_prices()
            item_data.calculate_gold_efficiency()






















