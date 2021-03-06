from utils import read_inputs

inputs = read_inputs("inputday4.txt")


nbpasseport = inputs.count("")
print(nbpasseport)
indexnextpasseport = 0
indexcurrentpasseport = 0
print(inputs[i] for i in range(20))
goodpasseport = 0
for i in range(nbpasseport):
    condition = 0
    numberofkey = 0
    currentpasseportkey = []
    currentpasseportvalue = []
    while inputs[indexnextpasseport] != "":
        indexnextpasseport += 1

    idpasseport = []
    idpasseport = " ".join(
        [inputs[idx] for idx in range(indexcurrentpasseport, indexnextpasseport)]
    )
    idpasseportsplitkey = idpasseport.split(" ")

    for k in range(len(idpasseportsplitkey)):
        currentpasseportkey.append(idpasseportsplitkey[k].split(":")[0])
        currentpasseportvalue.append(idpasseportsplitkey[k].split(":")[1])
    if all(
        [
            element in currentpasseportkey
            for element in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        ]
    ):
        condition = 1
        print("i", i)
        byr_index = currentpasseportkey.index("byr")
        iyr_index = currentpasseportkey.index("iyr")
        eyr_index = currentpasseportkey.index("eyr")
        hgt_index = currentpasseportkey.index("hgt")
        hcl_index = currentpasseportkey.index("hcl")
        ecl_index = currentpasseportkey.index("ecl")
        pid_index = currentpasseportkey.index("pid")
        if not 1920 - 1 < int(currentpasseportvalue[byr_index]) < 2002 + 1:
            condition = 0
            print("byr", currentpasseportvalue[byr_index])
        if not 2010 - 1 < int(currentpasseportvalue[iyr_index]) < 2020 + 1:
            condition = 0
            print("iyr", currentpasseportvalue[iyr_index])
        if not 2020 - 1 < int(currentpasseportvalue[eyr_index]) < 2030 + 1:
            condition = 0
            print("eyr", currentpasseportvalue[eyr_index])
        currentpasseport_height = list(currentpasseportvalue[hgt_index])
        if all([element in currentpasseport_height for element in ["i", "n"]]):
            if len(currentpasseport_height) != 4:
                condition = 0
                print("hgt", currentpasseportvalue[hgt_index])
            else:
                height_in = int(
                    "".join([currentpasseport_height[0], currentpasseport_height[1]])
                )
                if not 59 - 1 < height_in < 76 + 1:
                    condition = 0
                    print("height_in", height_in)
        elif all([element in currentpasseport_height for element in ["c", "m"]]):
            if len(currentpasseport_height) != 5:
                condition = 0
                print("height", currentpasseport_height)
            else:
                height_cm = int(
                    "".join(
                        [
                            currentpasseport_height[0],
                            currentpasseport_height[1],
                            currentpasseport_height[2],
                        ]
                    )
                )
                if not 150 - 1 < height_cm < 193 + 1:
                    condition = 0
                    print("height", height_cm)
        else:
            condition = 0
        hair_color = list(currentpasseportvalue[hcl_index])
        if hair_color[0] != "#":
            condition = 0
            print("hair color", hair_color)
        if len(hair_color) != 7:
            condition = 0
            print("hair", hair_color)
        if any(
            [
                element in hair_color
                for element in [
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                    "s",
                    "t",
                    "u",
                    "v",
                    "w",
                    "x",
                    "y",
                    "z",
                ]
            ]
        ):
            condition = 0
            print("hair", hair_color)
        if not any(
            [
                element in currentpasseportvalue[ecl_index]
                for element in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            ]
        ):
            condition = 0
            print("ecl", currentpasseportvalue[ecl_index])
        passeport_id = list(currentpasseportvalue[pid_index])
        if len(passeport_id) != 9:
            condition = 0
            print("passeport_id", currentpasseportvalue[pid_index])
        else:
            if passeport_id[8] == 0 or passeport_id[0] == 0:
                condition = 0

    if condition:
        goodpasseport += 1

    indexnextpasseport = indexnextpasseport + 1
    indexcurrentpasseport = indexnextpasseport
print(goodpasseport)


#####################################################################

from utils import read_inputs
import re

inputs = read_inputs("inputs/04.txt")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def check_valid_fields(identity, required_fields):
    good_byr = 1920 <= int(identity.get("byr", 0)) <= 2002
    good_iyr = 2010 <= int(identity.get("iyr", 0)) <= 2020
    good_eyr = 2020 <= int(identity.get("eyr", 0)) <= 2030

    hgt = identity.get("hgt", "00cm")
    hgt_value, hgt_unit = hgt[:-2], hgt[-2:]
    hgt_value = int(hgt_value) if len(hgt_value) else hgt_value
    good_hgt = (hgt_unit == "cm" and 150 <= hgt_value <= 193) or (
        hgt_unit == "in" and 59 <= hgt_value <= 76
    )

    hcl = identity.get("hcl", "false")
    good_hcl = hcl[0] == "#" and re.match(r"^[0-9, a-f]{6}$", hcl[1:]) is not None

    allowed_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    good_ecl = identity.get("ecl", "false") in allowed_ecl

    good_pid = re.match(r"^[0-9]{9}$", identity.get("pid", "false")) is not None

    print(good_byr, good_iyr, good_eyr, good_hgt, good_hcl, good_ecl, good_pid)
    return (
        good_byr
        and good_iyr
        and good_eyr
        and good_hgt
        and good_hcl
        and good_ecl
        and good_pid
    )


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
    1 for identity in identities if check_valid_fields(identity, required_fields)
)

print(count_valid_password)