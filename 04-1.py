from utils import read_inputs
inputs = read_inputs("inputday4.txt")


nbpasseport=inputs.count('')
print(nbpasseport)
indexnextpasseport=0
indexcurrentpasseport=0
goodpasseport=0
for i in range(nbpasseport):
    numberofkey=0
    currentpasseportkey=[]
    while inputs[indexnextpasseport]!='':
        indexnextpasseport+=1
        
    idpasseport=[]
    idpasseport=" ".join([inputs[idx] for idx in range(indexcurrentpasseport,indexnextpasseport)])
    idpasseportsplitkey=idpasseport.split(" ")
    
    for k in range(len(idpasseportsplitkey)):
        currentpasseportkey.append(idpasseportsplitkey[k].split(":")[0]) 
    
    if all([element in currentpasseportkey for element in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
        goodpasseport+=1
    
    indexnextpasseport=indexnextpasseport+1
    indexcurrentpasseport=indexnextpasseport
print(goodpasseport)