import Util
import json
import requests

ores = [
    "Compressed Arkonor",
    "Compressed Bistot",
    "Compressed Crokite",
    "Compressed Dark Ochre",
    "Compressed Gneiss",
    "Compressed Hedbergite",
    "Compressed Hemorphite",
    "Compressed Jaspet",
    "Compressed Kernite",
    "Compressed Omber",
    "Compressed Plagioclase",
    "Compressed Pyroxeres",
    "Compressed Scordite",
    "Compressed Spodumain",
    "Compressed Veldspar"
]

def compute(typesTemp, materialsTemp):
    output = {}
    stored = {}

    for kes, vals in typesTemp.items():
        try:
            temp = { }
            for its in materialsTemp[vals]['materials']:
                if(its["materialTypeID"] not in stored):
                    r = requests.get("https://esi.evetech.net/v3/universe/types/" + str(its["materialTypeID"]) + "/?datasource=tranquility&language=en-us")
                    if(r.status_code == 200):
                        stored[its["materialTypeID"]] = json.loads(r.text)["name"]
                temp[stored[its["materialTypeID"]]] = its["quantity"]
            output[kes] = temp
        except Exception as e:
            pass
    return output
    
oreTypes = Util.get_type_IDs(ores)
materials = Util.get_yaml("typeMaterials")
MAIN_OUT = compute(oreTypes, materials)

print(MAIN_OUT)
Util.write_json('OreRepro', MAIN_OUT)
