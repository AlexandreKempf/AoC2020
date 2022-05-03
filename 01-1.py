from utils import read_inputs

inputs = read_inputs("inputs/01.txt")

inputs = {int(x) for x in inputs}
for x in inputs:
    if 2020 - x in inputs:
        result = x * (2020 - x)
        break

print(result)
