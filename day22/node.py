class Node:
    def __init__(self, used, avail, name='temp'):
        self.name, self.used, self.avail = name, used, avail

    def __eq__(self, other):
        return self.name == other.name and self.used == other.used and self.avail == other.avail

    def __repr__(self):
        return 'Node(%s, %s, %s)' % (self.name, self.used, self.avail)

    @classmethod
    def from_string(cls, string):
        string_list = [s for s in string.split(' ') if s != '']
        name = string_list[0]
        used = int(string_list[2][:-1])
        avail = int(string_list[3][:-1])
        return cls(name=name, used=used, avail=avail)

    @classmethod
    def viable_pair(cls, A, B):
        return A.used != 0 and A.used <= B.avail and A != B
