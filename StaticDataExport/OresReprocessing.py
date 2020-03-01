###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings

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
            json.dump(json.dumps(data, indent=4, sort_keys=True), json_file)
            print("Written: " + yaml_path + ".json")
        except Exception as exc:
            warnings.warn("Error in writing json_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)

def compute(typesTemp, materialsTemp):
    output = {}
    for kes, vals in typesTemp.items():
        try:
            if("Compressed " in vals['name']['en'][0:11]):
                temp = { }
                for its in materialsTemp[kes]['materials']:
                    temp[typesTemp[its['materialTypeID']]['name']['en']] = its['quantity']
                output[vals['name']['en']] = temp
        except Exception as e:
            pass
    return output

types = get_yaml("typeIDs")
materials = get_yaml("typeMaterials")

MAIN_OUT = compute(types, materials)

print(MAIN_OUT)
write_json('export', MAIN_OUT)
