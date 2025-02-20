# setup
2025/02/19 Current progress: seems like timeloop is working now. Getting cosa.py:599 error invalid schedule. That could be any issue from run_config. Need to probably print the error. 
- poetry install, poetry run
- [cannot open file](https://stackoverflow.com/questions/480764/linux-error-while-loading-shared-libraries-cannot-open-shared-object-file-no-s)
- [some more of that](https://forum.cardano.org/t/error-cardano-node-error-while-loading-shared-libraries-libsodium-so-23-cannot-open-shared-object-file-no-such-file-or-directory/39820/2)
- At the end of parse_workload where they use `ET.parse`, read the file in, strip it, add `</boost_serialization>` and use `ET.fromstring` from the resulting string. That will return root, so you don't need to run `get_root` anymore either

# run

cd src
python3.10 -m cosa.cosa

- follow the timeloop accelergy tutorial and set the timeloop env var as just wherever that timeloop folder is.
- replace np.math with import math and just math
- sample command: `wangke61@comps0:~/cosa/src$ python3.10 -m cosa.cosa -ap cosa/configs/arch/simba.yaml -pp cosa/configs/workloads/alexnet_graph/_outputs_210.yaml -mp cosa/configs/mapspace/mapspace.yaml`
- `poetry run python -m cosa.cosa -ap cosa/configs/arch/simba.yaml -pp cosa/configs/workloads/alexnet_graph/_outputs_210.yaml -mp cosa/configs/mapspace/mapspace.yaml`
- delete output_dir, or else it'll cache stuff. Seems like timeloop isn't working rn