import json
import random
import string
from pathlib import Path


class Util:

    @staticmethod
    def get_config(key):
        """
        Reads the json file and return the required config value
        :param key:
        :return: config_file_value
        """
        json_path = Path(__file__).parent.parent.joinpath("resources").joinpath("config.json")
        with open(json_path, 'r') as file:
            config_file = json.load(file)
            return config_file[key]

    def generate_random_chars(self, n: int):
        """
        generate random characters
        :param n:
        :return: char
        """
        name = string.ascii_lowercase
        char = (''.join(random.choice(name) for _ in range(n)))
        return char
