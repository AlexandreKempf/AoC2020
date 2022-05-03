# Day 3 second problem
from utils import read_inputs

import numpy as np

inputs = read_inputs("inputs/03/1.txt")
position = 0
nbtree1 = np.zeros(4)
slope = [1, 3, 5, 7]
for j in range(len(slope)):
    position = 0
    for i in range(1, len(inputs)):
        path = list(inputs[i])
        position = position + slope[j]
        if path[position % len(path)] == "#":
            nbtree1[j] += 1
print(nbtree1)

nbtree2 = 0
position = 0
z = np.arange(3, len(inputs) + 2, 2)
for i in range(np.size(z)):
    path = list(inputs[z[i] - 1])
    position = position + 1
    if path[position % len(path)] == "#":
        nbtree2 += 1
print(nbtree2)

result = nbtree1[0] * nbtree1[1] * nbtree1[2] * nbtree1[3] * nbtree2
print(result)


##############################################################

from utils import read_inputs
import numpy as np

inputs = read_inputs("inputs/03/1.txt")


def count_trees(inputs, x_steps, y_steps):
    x_position = 0
    tree_count = 0
    for line in inputs[::y_steps]:
        if line[x_position % len(line)] == "#":
            tree_count += 1
        x_position += x_steps
    return tree_count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (x_steps, y_steps)
count_trees_all_slopes = [
    count_trees(inputs, x_step, y_step) for x_step, y_step in slopes
]
print(np.prod(count_trees_all_slopes))
