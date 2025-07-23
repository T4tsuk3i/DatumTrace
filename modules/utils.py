import yaml
import os

def load_config():
    path = os.path.join(os.path.dirname(__file__), '..', 'config', 'sources.yaml')
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def build_headers(config):
    return config.get('headers', {}).get('default', {})
