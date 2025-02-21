So two things I could investigate are:
- How do different configurations on the same workload affect the workload?
- How do different input architectures and workloads affect solving time, energy consumption and the optimal solution?

Might not do the first one now because
- It's hard to code up using this codebase
- It may not be as informative to me compared to the second question. If my goal is to figure out how different things are affecting the runtime of a kernel, I can make my own tests later, I don't need the CoSA codebase.

# How do different arch/problems affect solving time, energy consumption and optimal solution?

### What to save:
- Architecture config
- Problem config
- Time to solve the MIP
- PE energy(1e-12J)
- Total energy(1e-6J)
- PE cycles and total cycles

### Notes
- seems like cycles is actually the total cycles, and PE cycles is number of cycles in the PE(may need to verify)
- Since eg. if you multiply stuff together you get like 37M for one thing, but only 3.7M cycles. We'll see.

### TODO
- [DONE] write a script to list every thing in the config workloads that contain a 'problem' key

Test various random configs
- make sure to change output_dir to something else
- maybe the RQ is to test the effect of different permutations, etc. so we can mutate the optimal solution found by CoSA and plot the runtime etc. of all the runs
- We can also test what happens when we scale the architecture up, given our hypothesis about solver time. From what we've found, it doesn't seem like buffers are completely used on average, so increasing those probably wouldn't do much. We probably want to try scaling up spatial resources. I think that's what will make the solver slower.

- maybe writeup what I have so far and show Maryam, to see if best course of action is to keep looking into this, or to start looking at TACCL since this probably won't be the final goal