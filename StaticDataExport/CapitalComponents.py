import Util
import json
import requests

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

def compute(typesTemp, blueprintsTemp):
    output_id_quant = {}
    output = {}
    needed = []

    for bps, datas in blueprintsTemp.items():
        try:
            nameID = datas['activities']['manufacturing']['products'][0]['typeID'];
            if(nameID in typesTemp.keys()):
                temp = { }
                for mats in datas['activities']['manufacturing']['materials']:
                    currentMaterial = mats['typeID']
                    if((currentMaterial not in typesTemp.keys()) and (currentMaterial not in needed)):
                        needed += [currentMaterial]
                    temp[currentMaterial] = mats['quantity']
                output_id_quant[typesTemp[nameID]] = temp
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

types = Util.get_type_IDs(components)
blueprints = Util.get_yaml("blueprints")

MAIN_OUT = compute(types, blueprints)

Util.write_json('CapComponents', MAIN_OUT)
