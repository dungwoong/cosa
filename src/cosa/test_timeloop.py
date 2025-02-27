from cosa.utils import parse_yaml
from cosa.parse_workload import get_subnest_info
from cosa.cosa_input_objs import Arch, Prob, Mapspace

from pathlib import Path
import subprocess
import os
import yaml
import argparse

_COSA_DIR = os.path.abspath(__file__ + "/../")

def construct_argparser():
    parser = argparse.ArgumentParser(description='Run Configuration')
    parser.add_argument('-o',
                        '--output_dir',
                        type=str,
                        help='Output Folder',
                        default='output_dir/timeloop_hybrid',
                        )
    parser.add_argument('-ap',
                        '--arch_path',
                        type=str,
                        help='Hardware Architecture Path',
                        default=f'{_COSA_DIR}/configs/arch/simba.yaml',
                        )
    parser.add_argument('-mp',
                        '--mapspace_path',
                        type=str,
                        help='Mapspace Path',
                        default=f'{_COSA_DIR}/configs/mapspace/mapspace.yaml',
                        )
    parser.add_argument('-pp',
                        '--prob_path',
                        type=str,
                        help='Problem Dimension Path',
                        default=f'{_COSA_DIR}/configs/workloads/resnet50_graph/_outputs_input.2.yaml',
                        )
    return parser

def combine_yaml_files(file_paths, output_path='tmp.yaml'): # thanks chatGPT
    with open(output_path, 'w') as output_file:
        for i, file_path in enumerate(file_paths):
            with open(file_path, 'r') as file:
                content = yaml.full_load(file)
                
                # Write the content of the current file
                yaml.dump(content, output_file, default_flow_style=False)
                
                # If it's not the last file, add a separator between documents
                # if i < len(file_paths) - 1:
                #     output_file.write("\n---\n")

def run_timeloop_mapper_hybrid_test(arch_path, prob_path, mapspace_path, mapper_path='cosa/configs/new/mapper_template.yaml', cwd=os.getcwd(), stdout=None, stderr=None, output_dir=None):
    try:
        print("Running HYBRID Random Index + Linear Pruning")
        combine_yaml_files([mapper_path, arch_path, prob_path, mapspace_path])
        # arch_path = pathlib.Path('timeloop_configs/arch/simba_large.yaml').resolve()
        # mapspace_path = pathlib.Path('timeloop_configs/mapspace/mapspace_io_hybrid.yaml').resolve()
        args = ['timeloop-mapper', 'tmp.yaml', ]
        if output_dir is not None:
            args.append('-o')
            args.append(output_dir)
        p = subprocess.check_call(args, \
                                  cwd=cwd, stdout=stdout, stderr=stderr)
        return True
    except Exception as e:
        print(e)
        return False

def main(arch, prob, mapspace, output_dir):
    arch = Path(arch)
    prob = Path(prob)
    mapspace = Path(mapspace)

    os.mkdirs(output_dir)

    success = run_timeloop_mapper_hybrid_test(arch, prob, mapspace, output_dir=output_dir)
    if not success:
        print("TIMELOOP FAILED")
    else:
        try:
            status_dict = {'utilized_capacity': []}

            subnest_info = get_subnest_info('timeloop-mapper.map+stats.xml')
            bufsize = subnest_info['bufsize']
            pe_cycle = subnest_info['pe_cycle']
            pe_energy = subnest_info['pe_energy']
            cycle = subnest_info['cycle']
            energy = subnest_info['energy']
            status_dict['pe_cycle'] = pe_cycle
            status_dict['pe_energy'] = pe_energy
            status_dict['energy'] = energy
            status_dict['cycle'] = cycle
            for buf_idx, (buf_name, buf) in enumerate(bufsize.items()):
                utilized_capacity = 0
                for mem_util in buf:
                    utilized_capacity += mem_util
                status_dict['utilized_capacity'].append(utilized_capacity)

            print(status_dict)
        except:
            print(status_dict)

# TODO make the stuff actually save to the right folder, get ready to run a bunch of experiments with this.