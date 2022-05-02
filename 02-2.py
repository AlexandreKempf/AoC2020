from utils import read_inputs

inputs = read_inputs('inputs/input2.txt')

right_pswd = 0

for ele in inputs:
	temp_tab = ele.split(' ')
	tab_num = temp_tab[0].split('-')
	letter_cnt = 0
	if ((temp_tab[2][int(tab_num[0]) - 1] == temp_tab[1][0]) \
	^ (temp_tab[2][int(tab_num[1]) - 1] == temp_tab[1][0])):
		right_pswd+=1

print(right_pswd)