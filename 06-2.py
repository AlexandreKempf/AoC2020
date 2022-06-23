from utils import read_inputs
import string

alphabet = string.ascii_lowercase[:26]
inputs = read_inputs("inputs/06.txt")


def parse_form_intersection(inputs):
    form = [set(alphabet)]
    identity_index = 0
    for line in inputs:
        if line == "":
            identity_index += 1
            form.append(set(alphabet))
        else:
            form[identity_index] &= set(line)
    return form


yes_count = sum(len(answers) for answers in parse_form_intersection(inputs))

print(yes_count)