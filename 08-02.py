from copy import deepcopy
from utils import read_inputs

inputs = read_inputs("inputs/08.txt")
list_of_action=[]
list_of_argument=[]
for instructions in inputs:
    action, argument=instructions.split(" ")
    list_of_action.append(action)
    list_of_argument.append(int(argument))
    
    
accumulator=0    
current_level=0
index_changed=0
level_visited=set()
while current_level!=len(list_of_action):
    current_level=0
    accumulator=0
    level_visited=set()
    while current_level not in level_visited and current_level!=len(list_of_action):
        level_visited|={current_level}

        action=list_of_action_changed[current_level]

        if action=='jmp':
            current_level+=list_of_argument[current_level]
        if action=='acc':
            accumulator+=list_of_argument[current_level]
            current_level+=1
        if action=='nop':
            current_level+=1
        if current_level>len(list_of_action):
            print("oui")
    list_of_action_changed=deepcopy(list_of_action)    
    while list_of_action[index_changed] not in ["jmp","nop"]:
        index_changed+=1
    if list_of_action[index_changed]=="jmp":
        list_of_action_changed[index_changed]='nop'
    if list_of_action[index_changed]=="nop":
        list_of_action_changed[index_changed]='jmp'
    
    
    index_changed+=1
print(accumulator)