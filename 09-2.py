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

index_first_number=0
index_second_number=1
contiguous_set=[list_of_number[index_first_number],list_of_number[index_second_number]]
sum_first_to_second_number=list_of_number[index_first_number]+list_of_number[index_second_number]
while sum_first_to_second_number!=invalid_number:
    if index_second_number<len(list_of_number)-1:
        index_second_number+=1
        contiguous_set.append(list_of_number[index_second_number])
        sum_first_to_second_number+=list_of_number[index_second_number]
    else:
        index_first_number+=1
        index_second_number=index_first_number+1
        sum_first_to_second_number=list_of_number[index_first_number]+list_of_number[index_second_number]
        contiguous_set=[list_of_number[index_first_number],list_of_number[index_second_number]]
print(max(contiguous_set)+min(contiguous_set))
print(list_of_number[index_first_number]+list_of_number[index_second_number])