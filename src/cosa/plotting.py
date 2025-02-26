import os
import json

def combine_jsons(root_path, output_json_path='output.json'):
    lst = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if 'json' in file:
                fpath = os.path.join(root, file)
                with open(fpath, 'r') as f:
                    lst.append(json.load(f))
    return lst