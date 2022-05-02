def read_inputs(path):
    with open(path, "r") as file:
        return [line.replace("\n", "") for line in file.readlines()]
