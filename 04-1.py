from utils import read_inputs

inputs = read_inputs("inputs/04.txt")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def check_fields(identity, required_fields):
    return all(field in identity for field in required_fields)


def parse_identities(inputs):
    identities = [{}]
    identity_index = 0
    for line in inputs:
        if line == "":
            identity_index += 1
            identities.append({})
        else:
            partial_identity = dict([word.split(":") for word in line.split(" ")])
            identities[identity_index].update(partial_identity)
    return identities


identities = parse_identities(inputs)
count_valid_password = sum(
    1 for identity in identities if check_fields(identity, required_fields)
)

print(count_valid_password)
