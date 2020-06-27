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
    output_id_quant = {}
    output = {}
    needed = []

    for kes, vals in typesTemp.items():
        try:
            temp = { }
            for reproMaterials in materialsTemp[kes]['materials']:
                mater = reproMaterials["materialTypeID"]
                if((mater not in typesTemp.keys()) and (mater not in needed)):
                    needed += [mater]
                temp[mater] = reproMaterials["quantity"]
            output_id_quant[vals] = temp
        except Exception as e:
            pass
    if(len(needed) == 0):
        return output_id_quant
    typesTemp = {**typesTemp, **Util.get_name(map(str, needed))}
    for kes, vals in output_id_quant.items():
        try:
            temp = {}
            for vals_kes, vals_vals in vals.items():
                temp[typesTemp[vals_kes]] = vals_vals
            output[kes] = temp
        except Exception as e:
            pass
    return output
    
oreTypes = Util.get_type_IDs(ores)
materials = Util.get_yaml("typeMaterials")
MAIN_OUT = compute(oreTypes, materials)

print(MAIN_OUT)
Util.write_json('OreRepro', MAIN_OUT)
