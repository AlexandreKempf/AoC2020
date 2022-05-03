from utils import read_inputs

inputs = read_inputs("inputs/02.txt")

right_pswd = 0

for ele in inputs:
    temp_tab = ele.split(" ")
    tab_num = temp_tab[0].split("-")
    letter_cnt = 0
    if (temp_tab[2][int(tab_num[0]) - 1] == temp_tab[1][0]) ^ (
        temp_tab[2][int(tab_num[1]) - 1] == temp_tab[1][0]
    ):
        right_pswd += 1

print(right_pswd)


##############################################################

import re
from utils import read_inputs

inputs = read_inputs("inputs/02.txt")

split_caracters = [": ", " ", "-"]
num_correct_passwords = 0
for line in inputs:
    first_index, second_index, letter, password = re.split(
        "|".join(split_caracters), line
    )
    is_first_match = password[int(first_index) - 1] == letter
    is_second_match = password[int(second_index) - 1] == letter
    if is_first_match ^ is_second_match:  # XOR
        num_correct_passwords += 1

print(num_correct_passwords)
