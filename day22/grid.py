from copy import deepcopy

from day22.node import Node


class Grid:
    def __init__(self, nodes):
        self.width = 0
        self.height = 0
        node_list = list(nodes)
        for node in node_list:
            self.width = max(self.width, node.x + 1)
            self.height = max(self.height, node.y + 1)
        self._nodes = {(node.x, node.y): node for node in node_list}
        self._nodes[(self.width - 1, 0)].has_target_data = True

    def __str__(self):
        string_list = []
        for x in range(self.width):
            for y in range(self.height):
                string_list.append(str(self.get_node(x, y)))
            string_list.append('\n')
        return ' '.join(string_list)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        for coordinate in self._nodes:
            if self._nodes[coordinate].avail != other._nodes[coordinate].avail:
                return False
        return True

    def __hash__(self):
        used_list = []
        for x in range(self.width):
            for y in range(self.height):
                node = self.get_node(x, y)
                used_list.append(str(node.used))
                used_list.append(str(node.has_target_data))
        return hash(''.join(used_list))


    def _adjacent_nodes(self, node):
        coordinates = [(x, y) for x, y in [(node.x, node.y - 1),
                                           (node.x, node.y + 1),
                                           (node.x - 1, node.y),
                                           (node.x + 1, node.y)] if
                       0 <= x < self.width and 0 <= y < self.height]
        return [self._nodes[coordinate] for coordinate in coordinates]

    def get_node(self, x, y):
        return self._nodes[(x, y)]

    def available_moves(self):
        for node in self._nodes.values():
            for node2 in self._adjacent_nodes(node):
                if Node.viable_pair(node, node2):
                    yield (node, node2)

    @property
    def target_data_distance(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.get_node(x, y).has_target_data:
                    return x + y

    @property
    def adjacent_grids(self):
        for node_source, node_target in self.available_moves():
            grid = deepcopy(self)
            source = grid.get_node(node_source.x, node_source.y)
            target = grid.get_node(node_target.x, node_target.y)
            source.move_data_to(target)
            yield grid
