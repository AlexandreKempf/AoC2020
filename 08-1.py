from utils import read_inputs

inputs = read_inputs("inputs/08.txt")
list_of_action=[]
list_of_argument=[]
for instructions in inputs:
    action,argument=instructions.split(" ")
    list_of_action.append(action)
    list_of_argument.append(int(argument))
    
accumulator=0    
current_level=0

level_visited=set()
while current_level not in level_visited:
    level_visited|={current_level}
    
    action=list_of_action[current_level]
    
    if action=='jmp':
        current_level+=list_of_argument[current_level]
    if action=='acc':
        
        accumulator+=list_of_argument[current_level]
        current_level+=1
    if action=='nop':
        current_level+=1


        
print(accumulator)  