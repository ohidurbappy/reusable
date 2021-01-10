#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class AppConfig:
    r"""AppConfig is an utility class that converts a json file into attributes

    Atrributes::

        config_file_name (str) : Name of config file (default config.json)

    Usage::
        >>> from reusable import AppConfig
        >>> config=AppConfig()
        >>> my_key=config.my_key

    """

    def __init__(self, config_file_name="config.json"):
        r"""The constructor for Config class

        Initializes the Config class

        Parameters::

            config_file_name (str): Name of the config file (default config.json)

        Returns::

            AppConfig: An instance of the AppConfig class

        """
        with open(config_file_name, "r") as config:
            f = dict(json.load(config))
            for key, value in f.items():
                setattr(self, key, value)


class Config(object):
    r"""Config utility class to load a json file

    Usage::

        >>> from reusable import Config
        >>> config=Config("myconfig.json")
        >>> my_key=config.get("your_key")


    """

    def __init__(self, config_file_name="config.json"):
        r"""Class constructor for Config

        Parameters::

            config_file_name (str): Name of the config file passed as string

        """
        self.config_file_name = config_file_name
        self._config = self._open_config_file()

    def _open_config_file(self):
        """Load the config file"""

        with open(self.config_file_name) as json_data_file:
            conf = json.load(json_data_file)
        return conf

    def save_config_file(self):
        """Saves the config file"""
        with open(self.config_file_name, 'w') as outfile:
            json.dump(self._config, outfile,indent=2)

    def get(self, key, default_val=None):
        """Return value stored in config 

        Parameters::

            key (str): The key to look for
            default_val (any): The value to return when the key is not found

        """
        if key not in self._config.keys():  # we don't want KeyError
            return default_val  # just return None if not found
        return self._config[key]

    def put(self, key, value):
        self._config[key] = value

    def update(self):
        """Update the config file"""
        self.save_config_file()
