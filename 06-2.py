import string
alphabet=string.ascii_lowercase[:26]

from utils import read_inputs
inputs = read_inputs("inputday6.txt")


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

form_input=parse_form_intersection(inputs)
yes_count=0
yes_count=sum(len(answers) for answers in form_input) 

print(yes_count)