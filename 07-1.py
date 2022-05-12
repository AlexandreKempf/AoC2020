from utils import read_inputs

inputs = read_inputs("inputday7.txt")

rule={}
for line in inputs:
    current_bag=line[:-1].split(" bags contain ")[0]
    containable_bag=line[:-1].split(" bags contain ")[1]
    color_containable_bag=containable_bag.split(", ")
    color_containable=[]
    number_containable_bag=[]
    if color_containable_bag != "no other bags":
      for bags in color_containable_bag:
          number_containable_bag.append(bags.split(" ")[0])
          color_containable.append(" ".join(bags.split(" ")[1:-1]))
    rule[current_bag]=[]
    rule[current_bag].append(number_containable_bag)
    rule[current_bag].append(color_containable)
    




color_possible=[]
marked_color=["shiny gold"]

while len(marked_color):
    for key, value in rule.items():
        if (key not in marked_color) and (key not in color_possible) and (marked_color[0] in value[1]):
            marked_color.append(key)
    color_possible.append(marked_color.pop(0))
    

number_of_bag=0
number_of_bag_of_this_color=[1]
marked_color=["shiny gold"]

while len(marked_color):
    if rule[marked_color[0]][0]!=['no']:
        number_of_contained_bag=[int(number) for number in rule[marked_color[0]][0]]
        total_number_of_contained_bag=sum(number_of_contained_bag)
        number_of_bag+=number_of_bag_of_this_color[0]*total_number_of_contained_bag
        marked_color.extend(rule[marked_color[0]][1])
        number_of_bag_of_this_color.extend(number_of_contained_bag)
        marked_color.pop(0)
        number_of_bag_of_this_color.pop(0)
        
    else:
        marked_color.pop(0)
        number_of_bag_of_this_color.pop(0)

