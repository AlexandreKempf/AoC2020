from utils import read_inputs

inputs = read_inputs("inputs/02/1.txt")

right_pswd = 0

for ele in inputs:
    temp_tab = ele.split(" ")
    tab_num = temp_tab[0].split("-")
    letter_cnt = 0
    for letter in temp_tab[2]:
        if letter == temp_tab[1][0]:
            letter_cnt += 1
    if int(tab_num[0]) <= letter_cnt <= int(tab_num[1]):
        right_pswd += 1

print(right_pswd)


##############################################################

import re
from utils import read_inputs

inputs = read_inputs("inputs/02/1.txt")

split_caracters = [": ", " ", "-"]
num_correct_passwords = 0
for line in inputs:
    min_allowed, max_allowed, letter, password = re.split(
        "|".join(split_caracters), line
    )
    if int(min_allowed) <= password.count(letter) <= int(max_allowed):
        num_correct_passwords += 1

print(num_correct_passwords)
