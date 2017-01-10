class Grid:
    def __init__(self, nodes):
        self.width = 0
        self.height = 0
        node_list = list(nodes)
        for node in node_list:
            self.width = max(self.width, node.x + 1)
            self.height = max(self.height, node.y + 1)
        self._nodes = {(node.x, node.y): node for node in node_list}

    def __str__(self):
        string_list = []
        for x in range(self.width):
            for y in range(self.height):
                string_list.append(str(self.get_node(x, y)))
            string_list.append('\n')
        return ' '.join(string_list)

    def _adjacent_nodes(self, node):
        coordinates = [(x, y) for x, y in [(node.x, node.y - 1),
                                           (node.x, node.y + 1),
                                           (node.x - 1, node.y),
                                           (node.x + 1, node.y)] if
                       0 <= x < self.width and 0 <= y < self.height]
        return [self._nodes[coordinate] for coordinate in coordinates]

    def get_node(self, x, y):
        return self._nodes[(x, y)]
