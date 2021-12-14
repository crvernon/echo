import os
import yaml
import logging
import pkg_resources


class Config:
    """Load and set a configuration."""

    DEFAULT_PARAMS = pkg_resources.resource_filename('echo', 'data/config.yml')

    def __init__(self):

        # load default parameters
        self._params = read_yaml(Config.DEFAULT_PARAMS)

    @property
    def params(self):
        """Configuration parameters."""

        return self._params

    @params.setter
    def params(self, new_params: {} = dict):
        """Update parameter settings."""

        self._params.update(new_params)


def read_yaml(config_file):
    """Read the YAML config file.

    :return:                            YAML config object
    """

    # if config file not passed
    if config_file is None:
        msg = "Config file must be passed as an argument using:  config_file='<path to config.yml'>"
        logging.error(msg)
        raise AttributeError(msg)

    # check for path exists
    if os.path.isfile(config_file):
        with open(config_file, 'r') as yml:
            return yaml.load(yml, Loader=yaml.FullLoader)

    else:
        msg = f"Config file not found for path:  {config_file}."

        logging.error(msg)
        raise FileNotFoundError(msg)
