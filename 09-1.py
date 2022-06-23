from utils import read_inputs
inputs = read_inputs("inputs/09.txt")


list_of_number=[int(number) for number in inputs]

index_invalid_number=0

preamble=list_of_number[index_invalid_number:index_invalid_number+25]
allowed_number=set()
for first_number in preamble:
    for second_number in preamble:
        if second_number!=first_number:
            allowed_number|={(second_number+first_number)}
                


while list_of_number[index_invalid_number+25] in allowed_number:
    index_invalid_number+=1
    preamble=list_of_number[index_invalid_number:index_invalid_number+25]
    allowed_number=set()
    for first_number in preamble:
        for second_number in preamble:
            if second_number!=first_number:
                allowed_number|={(second_number+first_number)}
    
invalid_number=list_of_number[index_invalid_number+25]    
print(invalid_number)