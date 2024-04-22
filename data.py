import re
import os

import bs4
import requests
from bs4 import BeautifulSoup
from yaml import dump, load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


class Scraping:
    def __init__(self):
        self.main_url = "https://wr-meta.com"
        self.stat_names = [
            "Attack Damage",
            "Ability Power",
            "Armor",
            "Magic Resistance",
            "Max Health",
            "% Critical Rate",
            "% Attack Speed",
            "Move Speed",
            "% Physical Vamp",
            "Armor Penetration",
            "% Armor Penetration",
            "Magic Penetration",
            "% Magic Penetration",
            "Ability Haste",
            "% Move Speed",
            "Max Mana",
            "% Omnivamp",
            "% Health Regen",
            "% Mana Regeneration",
        ]
        self.bases = {
            "first_base": {
                "Attack Damage": "Long Sword",
                "Ability Power": "Amplifying Tome",
                "Armor": "Cloth Armor",
                "Magic Resistance": "Null-Magic Mantle",
                "Max Health": "Ruby Crystal",
                "% Critical Rate": "Brawler's Gloves",
                "% Attack Speed": "Dagger",
                "Move Speed": "Boots of Speed",
                "Ability Haste": "Ring of Revelation",
            },
            "second_base": {
                "% Physical Vamp": "Vampiric Scepter",
                "Armor Penetration": "Serrated Dirk",
                "% Armor Penetration": "Last Whisper",
                "Magic Penetration": "Prophet's Pendant",
                "% Move Speed": "Aether Wisp",
                "Max Mana": "Sapphire Crystal",
            }
        }
        self.datas = []
        self.stat_price = {}

    def parse_stat(self, stat: str) -> tuple[str, int] | None:
        try:
            stat = stat.split("+")[1]
        except Exception:
            return None
        stat = stat.strip(". ")

        for stat_name in self.stat_names:
            if match := re.search(r"^([\d-]*) *" + stat_name + "$", stat):
                if "-" in (value := match.group(1)):
                    return stat_name, int(value.split("-")[1])
                return stat_name, int(match.group(1))

    def get_abs_filename(self) -> str:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, f"./_data/items.yml")

        return file_path

    def write_yaml(self):
        file_path = self.get_abs_filename()

        with open(file_path, "w") as f:
            dump(self.datas, f, Dumper=Dumper)

    def read_yaml(self):
        file_path = self.get_abs_filename()

        with open(file_path, 'r') as f:
            return load(f, Loader=Loader)

    def scrap(self):
        try:
            response = requests.get(f"{self.main_url}/items/", timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            items = soup.find_all(class_="bild-img-short")

            for item in items:
                image = item.find(class_="xfieldimage lazy-loaded itemimage")
                desc = item.find("p")

                parent = item.find_parent("div", class_="clearfix sect-cont-incat")
                category = parent.find("div", class_="sect-title").text.upper()

                image_url = self.main_url + image["data-src"]
                item_name = desc.find(class_="iname").text.strip()

                # base stats
                istats: list[tuple[str, str]] = [
                    ("", state.text) for state in desc.find_all(class_="istats")
                ]
                # base stats in passives
                istats2: list[tuple[str, str]] = []
                for stat in desc.find_all(class_="istats2"):
                    if (
                        stat.find_next_sibling().name == "i"
                        and stat.find_next_sibling().children
                        and not isinstance(
                            list(stat.find_next_sibling().children)[0],
                            bs4.element.NavigableString,
                        )
                        and list(stat.find_next_sibling().children)[0].has_attr("class")
                        and list(stat.find_next_sibling().children)[0].get("class")
                        == ["fr-fic", "fr-dii"]
                    ):
                        next_sibling_text = stat.find_next_sibling().text
                    else:
                        next_sibling_text = str(stat.next_element.next_element)

                    if next_sibling_text and (
                        re.fullmatch(r"^(?:&nbsp;|\xa0|\s)\+.*", next_sibling_text)
                    ):
                        istats2.append((stat.text.strip(":"), next_sibling_text))

                istats += istats2

                cost = int(desc.find(class_="goldt").text.strip())

                stats = []
                for passive, stat in istats:
                    stat = self.parse_stat(stat)
                    if stat:
                        if passive:
                            stats.append(
                                {"type": stat[0], "value": stat[1], "passive": passive}
                            )
                        else:
                            stats.append({"type": stat[0], "value": stat[1]})

                self.datas.append(
                    {
                        "name": item_name,
                        "image": image_url,
                        "cost": cost,
                        "stats": stats,
                        "category": category,
                    }
                )

            self.write_yaml()

        except requests.exceptions.ConnectTimeout as execinfo:
            print(str(execinfo))

    def find_data_with_name(self, datas, name: str):
        for data in datas:
            if data['name'] == name:
                return data

    def find_stat_with_type(self, data, type: str):
        for stat in data['stats']:
            if stat['type'] == type:
                return stat

    def calculate_base_statistic_prices(self):
        if self.datas:
            datas = self.datas
        else:
            datas = self.read_yaml()
        first_base = self.bases['first_base']
        second_base = self.bases['second_base']

        for _type in first_base:
            _name = first_base[_type]

            data = self.find_data_with_name(datas, _name)
            target_stat = self.find_stat_with_type(data, _type)
            if not (data and target_stat):
                raise ValueError(f"data: {data}, target_stat: {target_stat}")
            cost = data['cost']

            stat_cost = float("{:.2f}".format(cost / target_stat['value']))
            data['first_base'] = {'type': _type, 'value': stat_cost, 'formula': f"{data['cost']}/{target_stat['value']}={stat_cost}"}
            self.stat_price[_type] = stat_cost

        for _type in second_base:
            _name = second_base[_type]

            data = self.find_data_with_name(datas, _name)
            target_stat = self.find_stat_with_type(data, _type)
            if not (data and target_stat):
                raise ValueError(f"data: {data}, target_stat: {target_stat}")
            cost = data['cost']

            formula_minus_part = ""
            for stat in data['stats']:
                if stat['type'] != _type:
                    cost -= stat['value']*self.stat_price[stat['type']]
                    formula_minus_part += f"-{stat['value']}*{self.stat_price[stat['type']]}"

            stat_cost = float("{:.2f}".format(cost / target_stat['value']))
            data['second_base'] = {
                'type': _type,
                'value': stat_cost,
                'formula': f"({data['cost']}{formula_minus_part})/{target_stat['value']}={stat_cost}"
            }
            self.stat_price[_type] = stat_cost

        self.datas = datas
        self.write_yaml()

    def calculate_gold_efficiency(self):
        if self.datas:
            datas = self.datas
        else:
            datas = self.read_yaml()

        if not self.stat_price:
            for data in datas:
                if 'first_base' in data:
                    self.stat_price[data['first_base']['type']] = data['first_base']['value']
                if 'second_base' in data:
                    self.stat_price[data['second_base']['type']] = data['second_base']['value']
        stat_price = self.stat_price

        for data in datas:
            if not ('first_base' in data or 'second_base' in data):
                worth = 0
                formula_bonux_part = ""
                for stat in data['stats']:
                    worth += stat['value']*stat_price.get(stat['type'], 0)
                    formula_bonux_part += f"{'+' if formula_bonux_part else ''}{stat['value']}*{stat_price.get(stat['type'], 0)}"
                amount = "{:.2f}".format(worth/data['cost']*100) + "%"
                data['amount'] = amount
                data['formula'] = f"({formula_bonux_part if formula_bonux_part else '0'})/{data['cost']}={amount}"
            else:
                data['amount'] = "100%"
                data['formula'] = "Base Item"

        self.datas = datas
        self.write_yaml()



scraping = Scraping()

# Due to missing or incorrect information on the source website, it is advised not to use it.
# scraping.scrap()

scraping.calculate_base_statistic_prices()
scraping.calculate_gold_efficiency()
