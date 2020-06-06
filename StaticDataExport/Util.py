###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings
import requests

def get_yaml(yaml_path):
    with open(yaml_path + ".yaml", 'r', encoding='utf8') as yaml_file:
        try:
            print("Loading yaml file " + yaml_path)
            yaml_out = yaml.safe_load(yaml_file)
            print("Loaded yaml file " + yaml_path)
        except yaml.YAMLError as exc:
            warnings.warn("Error in reading yaml_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)
    return yaml_out


def write_json(yaml_path, data):
    with open(yaml_path + ".json" , 'w', encoding='utf8') as json_file:
        try:
            print("Writing: " + yaml_path + ".json")
            json.dump(data, json_file, indent=4)
            print("Written: " + yaml_path + ".json")
        except Exception as exc:
            warnings.warn("Error in writing json_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)

def get_type_IDs(array):
    tbr = {}

    r = requests.post(
        "https://esi.evetech.net/v1/universe/ids/?datasource=tranquility&language=en-us",
        data=('["' + '", "'.join(array) + '"]'))

    if(r.status_code == 200):
        for items in json.loads(r.text)["inventory_types"]:
            tbr[items['name']] = items['id']

    return tbr
