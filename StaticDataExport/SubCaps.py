###
### Code base aquired from Ravandel
###

import Util

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

def compute(typesTemp, blueprintsTemp):
    output_id_quant = {};
    output = {};
    needed = [];

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

types = Util.get_yaml("typeIDs")
blueprints = Util.get_yaml("blueprints")

MAIN_OUT = compute(types, blueprints)

print(MAIN_OUT)
Util.write_json('exportT1S', MAIN_OUT)
