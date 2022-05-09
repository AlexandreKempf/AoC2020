from utils import read_inputs
import numpy as np

input = read_inputs("inputs/04-2.txt")
key = []
count_valid_passport = 0
nb_passport = 0
for line in input:
    if line:
        fields = line.split(" ")
        for element in fields:
            element = element.split(":")
            key.append(element[0])
    else:
        key = []
    if all(
        [
            element in key
            for element in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        ]
    ):
        count_valid_passport += 1
        key = []

print(count_valid_passport)
