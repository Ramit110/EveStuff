###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings

components = [
    "Capital Propulsion Engine",
    "Capital Turret Hardpoint",
    "Capital Sensor Cluster",
    "Capital Armor Plates",
    "Capital Cargo Bay",
    "Capital Capacitor Battery",
    "Capital Power Generator",
    "Capital Shield Emitter",
    "Capital Jump Drive",
    "Capital Drone Bay",
    "Capital Computer System",
    "Capital Construction Parts",
    "Capital Jump Bridge Array",
    "Capital Clone Vat Bay",
    "Capital Doomsday Weapon Mount",
    "Capital Siege Array",
    "Capital Launcher Hardpoint",
    "Capital Ship Maintenance Bay",
    "Capital Corporate Hangar Bay"
]

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

def compute(typesTemp, blueprintsTemp):
    output = {}
    for bps, datas in blueprintsTemp.items():
        try:
            name = typesTemp[datas['activities']['manufacturing']['products'][0]['typeID']]['name']['en'];
            if(name in components):
                temp = { }
                for mats in datas['activities']['manufacturing']['materials']:
                    temp[typesTemp[mats['typeID']]['name']['en']] = mats['quantity']
                output[name] = temp
        except Exception as e:
            pass
    return output

types = get_yaml("typeIDs")
blueprints = get_yaml("blueprints")

MAIN_OUT = compute(types, blueprints)

print(MAIN_OUT)
write_json('exportCapComp', MAIN_OUT)
