from utils import read_inputs
from functools import lru_cache

inputs = read_inputs("inputs/07.txt")


def get_bag_name(content):
    return " ".join(content.split(" ")[1:-1])


database = {}
for line in inputs:
    container, content = line[:-1].split(" bags contain ")
    if content == "no other bags":
        database[container] = []
    else:
        database[container] = [get_bag_name(c) for c in content.split(", ")]


@lru_cache
def get_containers(bag):
    return {container for container, content in database.items() if bag in content}


def recursive_containers(bag, accumulator=set()):
    containers = get_containers(bag)
    if not containers < accumulator:  # all containers has already been found
        accumulator |= containers
        for container_bag in containers:
            accumulator |= recursive_containers(container_bag, accumulator)
    return accumulator


print(len(recursive_containers("shiny gold")))
