###
### Code base aquired from Ravandel
###

import Util

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

types = Util.get_yaml("typeIDs")
blueprints = Util.get_yaml("blueprints")

MAIN_OUT = compute(types, blueprints)

print(MAIN_OUT)
Util.write_json('exportCapComp', MAIN_OUT)
