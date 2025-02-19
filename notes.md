# run

cd src
python3.10 -m cosa.cosa

- follow the timeloop accelergy tutorial and set the timeloop env var as just wherever that timeloop folder is.
- replace np.math with import math and just math
- sample command: `wangke61@comps0:~/cosa/src$ python3.10 -m cosa.cosa -ap cosa/configs/arch/simba.yaml -pp cosa/configs/workloads/alexnet_graph/_outputs_210.yaml -mp cosa/configs/mapspace/mapspace.yaml`
- delete output_dir, or else it'll cache stuff. Seems like timeloop isn't working rn