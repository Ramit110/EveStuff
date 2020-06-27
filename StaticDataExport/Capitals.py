###
### Code base aquired from Ravandel
###

import Util

caps = [
    "Archon",
    "Chimera",
    "Thanatos",
    "Nidhoggur",
    "Revelation",
    "Phoenix",
    "Moros",
    "Naglfar",
    "Apostle",
    "Minokawa",
    "Ninazu",
    "Lif",
    "Avatar",
    "Leviathan",
    "Erebus",
    "Ragnarok",
    "Providence",
    "Charon",
    "Obelisk",
    "Fenrir",
    "Rorqual",
    "Orca",
    "Chemosh",
    "Caiman",
    "Vehement",
    "Revenant",
    "Vendetta",
    "Dagon",
    "Loggerhead",
    "Molok",
    "Komodo",
    "Vanquisher",
    "Aeon",
    "Hel",
    "Nyx",
    "Wyvern"
]

def compute(typesTemp, blueprintsTemp):
    output = {}
    for bps, datas in blueprintsTemp.items():
        try:
            name = typesTemp[datas['activities']['manufacturing']['products'][0]['typeID']]['name']['en'];
            if(name in caps):
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
Util.write_json('exportCaps', MAIN_OUT)
