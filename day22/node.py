class Node:
    def __init__(self, x, y, used, avail):
        self.x, self.y, self.used, self.avail = x, y, used, avail
        self.has_target_data = False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '(%sT / %sT)' % (self.used, self.avail + self.used)

    @classmethod
    def from_string(cls, string):
        string_list = [s for s in string.split(' ') if s != '']
        path = string_list[0]
        path_split = path.split('-')
        x = int(path_split[1][1:])
        y = int(path_split[2][1:])
        used = int(string_list[2][:-1])
        avail = int(string_list[3][:-1])
        return cls(x=x, y=y, used=used, avail=avail)

    @classmethod
    def viable_pair(cls, A, B):
        return A.used != 0 and A.used <= B.avail and A != B

    def move_data_to(self, node):
        node.used += self.used
        node.avail -= self.used
        self.avail += self.used
        self.used = 0
        if self.has_target_data:
            node.has_target_data = True
            self.has_target_data = False
