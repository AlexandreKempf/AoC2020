#Day 3 first problem

inputs = read_inputs("inputday3.txt")
position=0
nbtree=0
for i in range(1,len(inputs)):
    path=list(inputs[i])
    position=position+3
    if path[position%len(path)]=="#":
        nbtree+=1
print(nbtree)


#Day 3 second problem

import numpy as np
inputs = read_inputs("inputday3.txt")
position=0
nbtree1=np.zeros(4)
slope=[1,3,5,7]
for j in range(len(slope)):
    position=0
    for i in range(1,len(inputs)):
        path=list(inputs[i])
        position=position+slope[j]
        if path[position%len(path)]=="#":
            nbtree1[j]+=1
print(nbtree1)

nbtree2=0
position=0
z=np.arange(3,len(inputs)+2,2)
for i in range(np.size(z)):
    path=list(inputs[z[i]-1])
    position=position+1
    if path[position%len(path)]=="#":
        nbtree2+=1
print(nbtree2)

result=nbtree1[0]*nbtree1[1]*nbtree1[2]*nbtree1[3]*nbtree2
print(result)