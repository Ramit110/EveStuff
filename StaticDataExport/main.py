###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings

importantKeys = {}
output = {}

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
            json.dump(data, json_file)
            print("Written: " + yaml_path + ".json")
        except Exception as exc:
            warnings.warn("Error in writing json_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)

types = get_yaml("typeIDs")
materials = get_yaml("invTypeMaterials")

for kes, vals in types.items():
    try:
        if("Compressed" in vals['name']['en'][0:10]):
            importantKeys[kes] = vals['name']['en']
            output[vals['name']['en']] = {}
    except Exception as e:
        pass

for num in range(0, len(materials)):
    if(materials[num]['typeID'] in importantKeys.keys()):
        try:
            matDetails = materials[num]
            output[types[matDetails['typeID']]['name']['en']][types[matDetails['materialTypeID']]['name']['en']] = matDetails['quantity']
        except Exception as e:
            print(e)
            pass

print(output)
write_json('export', output)
