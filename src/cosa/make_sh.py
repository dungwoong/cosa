import os
import yaml

def parse_yaml(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.full_load(f)
    return data

# print(parse_yaml('cosa/configs/workloads/alexnet_graph/_outputs_210.yaml'))

WORKLOADS_PATH = 'cosa/configs/workloads'

def walk_directory(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if 'yaml' in file:
                yield os.path.join(root, file)

for f in walk_directory(WORKLOADS_PATH):
    try:
        if 'problem' in parse_yaml(f):
            print(f"poetry run python -m cosa.cosa -ap cosa/configs/arch/simba.yaml -pp {f} -mp cosa/configs/mapspace/mapspace.yaml")
            print(f"poetry run python -m cosa.cosa -ap cosa/configs/arch/simba_large.yaml -pp {f} -mp cosa/configs/mapspace/mapspace.yaml")
    except:
        continue