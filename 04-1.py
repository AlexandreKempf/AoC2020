from utils import read_inputs

inputs = read_inputs("inputs/04.txt")


nbpasseport = inputs.count("")
print(nbpasseport)
indexnextpasseport = 0
indexcurrentpasseport = 0
goodpasseport = 0
for i in range(nbpasseport):
    numberofkey = 0
    currentpasseportkey = []
    while inputs[indexnextpasseport] != "":
        indexnextpasseport += 1

    idpasseport = []
    idpasseport = " ".join(
        [inputs[idx] for idx in range(indexcurrentpasseport, indexnextpasseport)]
    )
    idpasseportsplitkey = idpasseport.split(" ")

    for k in range(len(idpasseportsplitkey)):
        currentpasseportkey.append(idpasseportsplitkey[k].split(":")[0])

    if all(
        [
            element in currentpasseportkey
            for element in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        ]
    ):
        goodpasseport += 1

    indexnextpasseport = indexnextpasseport + 1
    indexcurrentpasseport = indexnextpasseport
print(goodpasseport)


############################################################

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