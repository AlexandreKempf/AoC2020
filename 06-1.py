from utils import read_inputs
inputs = read_inputs("inputs/06.txt")

def parse_form(inputs):
    form = [set()]
    identity_index = 0
    for line in inputs:
        if line == "":
            identity_index += 1
            form.append(set())
        else:
            form[identity_index] |= set(line)
    return form

yes_count=0
            
form_input=parse_form(inputs)
for length_form in form_input:
    yes_count+=len(length_form)

print(yes_count)