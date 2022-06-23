from utils import read_inputs
from functools import lru_cache

inputs = read_inputs("inputs/07.txt")


def get_bag_number_and_name(content):
    return int(content.split(" ")[0]), " ".join(content.split(" ")[1:-1])


database = {}
for line in inputs:
    container, content = line[:-1].split(" bags contain ")
    if content == "no other bags":
        database[container] = []
    else:
        database[container] = [get_bag_number_and_name(c) for c in content.split(", ")]


def count_content(bag, nb_container):
    content = database[bag]
    if len(content):
        return nb_container + sum(
            count_content(bag, number) * nb_container for number, bag in content
        )
    else:
        return nb_container


print(count_content("shiny gold", 1) - 1)
