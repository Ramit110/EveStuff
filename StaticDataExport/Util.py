###
### Code base aquired from Ravandel
###

import yaml
import json
import warnings
import requests

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
            json.dump(data, json_file, indent=4)
            print("Written: " + yaml_path + ".json")
        except Exception as exc:
            warnings.warn("Error in writing json_file in convert_yaml_json().")
            warnings.warn(exc)
            quit(1)

def make_post_request(url_uri, array):
    print("Sending request to Server: " + str(array))
    while(1):
        print("Request sending")
        r = requests.post(
            url_uri,
            data=('["' + '", "'.join(array) + '"]')
        )
        if(r.status_code == 200):
            break
    print("Request accepted")

    return json.loads(r.text)

def get_type_IDs(array):
    json_res = make_post_request("https://esi.evetech.net/v1/universe/ids/?datasource=tranquility&language=en-us", array)
    tbr = {}
    for items in json_res["inventory_types"]:
        tbr[items['id']] = items['name']

    return tbr

def get_name(array):
    json_res = make_post_request("https://esi.evetech.net/latest/universe/names/?datasource=tranquility", array)
    tbr = {}
    for items in json_res:
        tbr[items['id']] = items['name']
    return tbr