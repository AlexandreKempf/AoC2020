from utils import read_inputs


inputs = read_inputs("inputs/03/1.txt")
position = 0
nbtree = 0
for i in range(1, len(inputs)):
    path = list(inputs[i])
    position = position + 3
    if path[position % len(path)] == "#":
        nbtree += 1
print(nbtree)

##############################################################

from utils import read_inputs


inputs = read_inputs("inputs/03/1.txt")
x_position, x_steps = 0, 3
tree_count = 0
for line in inputs:
    if line[x_position % len(line)] == "#":
        tree_count += 1
    x_position += x_steps
print(tree_count)
