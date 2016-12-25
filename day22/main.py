from day22.node import Node

with open('input.txt') as f:
    lines = [line[:-1] for line in f.readlines() if len(line) > 0][2:]
    nodes = [Node.from_string(line) for line in lines]
    viable_pairs = 0
    for node1 in nodes:
        for node2 in nodes:
            if Node.viable_pair(node1, node2):
                viable_pairs += 1

    print(viable_pairs)
