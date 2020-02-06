###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings

# does as the name suggests
def convert_yaml_json(yaml_path):
    with open(yaml_path, 'r', encoding='utf8') as yaml_file:
        try:
            print("Loading yaml file")
            yaml_blueprints = yaml.safe_load(yaml_file)
        except yaml.YAMLError as exc:
            warnings.warn("Error in reading yaml_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)

    json_path = yaml_path[0:yaml_path.rfind(".")] + ".json"
    with open(json_path , 'w', encoding='utf8') as json_file:
        try:
            print("Writing: " + json_path)
            json.dump(yaml_blueprints, json_file)
        except Exception as exc:
            warnings.warn("Error in writing json_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)
