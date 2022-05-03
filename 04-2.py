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
