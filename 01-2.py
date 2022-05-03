from utils import read_inputs

inputs = read_inputs("inputs/01.txt")

inputs = [int(x) for x in inputs]
for i, x in enumerate(inputs):
    for j, y in enumerate(inputs[i:]):
        for z in inputs[j:]:
            if x + y + z == 2020:
                result = x * y * z

print(result)
