import yaml
import pathlib

config_path = pathlib.Path('config/config.yml')
with open(config_path, 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)
