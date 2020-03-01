###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings

ships = [
    "Impairor",
    "Ibis",
    "Velator",
    "Reaper",
    "Executioner",
    "Inquisitor",
    "Tormentor",
    "Crucifier",
    "Punisher",
    "Magnate",
    "Condor",
    "Bantam",
    "Kestrel",
    "Griffin",
    "Merlin",
    "Heron",
    "Atron",
    "Navitas",
    "Tristan",
    "Maulus",
    "Incursus",
    "Imicus",
    "Slasher",
    "Burst",
    "Breacher",
    "Vigil",
    "Rifter",
    "Probe",
    "Coercer",
    "Dragoon",
    "Cormorant",
    "Corax",
    "Catalyst",
    "Algos",
    "Thrasher",
    "Talwar",
    "Arbitrator",
    "Augoror",
    "Omen",
    "Maller",
    "Blackbird",
    "Osprey",
    "Caracal",
    "Moa",
    "Celestis",
    "Exequror",
    "Thorax",
    "Vexor",
    "Bellicose",
    "Scythe",
    "Stabber",
    "Rupture",
    "Prophecy",
    "Harbinger",
    "Oracle",
    "Ferox",
    "Drake",
    "Naga",
    "Brutix",
    "Myrmidon",
    "Talos",
    "Cyclone",
    "Hurricane",
    "Tornado",
    "Armageddon",
    "Apocalypse",
    "Abaddon",
    "Scorpion",
    "Raven",
    "Rokh",
    "Dominix",
    "Megathron",
    "Hyperion",
    "Typhoon",
    "Tempest",
    "Maelstrom",
    "Bestower",
    "Sigil",
    "Badger",
    "Tayra",
    "Nereus",
    "Kryos",
    "Epithal",
    "Miasmos",
    "Iteron Mark V",
    "Hoarder",
    "Mammoth",
    "Wreathe",
    "Amarr Shuttle",
    "Caldari Shuttle",
    "Gallente Shuttle",
    "Minmatar Shuttle",
    "Venture",
    "Covetor",
    "Retriever",
    "Procurer",
    "Noctis",
    "Porpoise",
    "Dramiel",
    "Cruor",
    "Worm",
    "Garmur",
    "Succubus",
    "Daredevil",
    "Astero",
    "Cynabal",
    "Ashimmu",
    "Gila",
    "Orthrus",
    "Phantasm",
    "Vigilant",
    "Stratios",
    "Machariel",
    "Bhaalgorn",
    "Rattlesnake",
    "Barghest",
    "Nightmare",
    "Vindicator",
    "Nestor"
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
            if(name in ships):
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
write_json('exportT1S', MAIN_OUT)
