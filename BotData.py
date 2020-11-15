from discord import Status
import configparser
import os

class BotData:
    BOT_NAME = str()
    TOKEN = str()
    BOT_PREFIX = str()
    STATUS = Status.online

    def read_config_data(self, path: str):
        """[summary]
        Reads the bot config info from the config file and stores it in the BotData class.
        Args:
            path (str): path to config file
        """
        cfg_parser = configparser.ConfigParser()
        if os.path.exists(path):
            cfg_parser.read(path)
        else:
            raise Exception("config file path does not exist!")
        self.BOT_PREFIX = cfg_parser['data']['prefix']
        self.TOKEN = cfg_parser['data']['token']