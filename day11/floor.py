class Floor:
    def __init__(self, set_):
        self._set = {o for o in set_}

    def __eq__(self, other):
        return type(self) == type(other) and self.objects == other.objects

    @property
    def objects(self):
        return self._set

    def is_legal(self):
        for s in self._set:
            if len(s) == 2:
                if s[1] == 'M':
                    if self._contains_generator_not_of_type(s[0]):
                        return False
        return True

    def _contains_generator_not_of_type(self, type):
        return len(list(filter(lambda x: len(x) == 2 and x[1] == 'G' and x[0] != type, self._set))) > 0

    def without(self, objects):
        return Floor(self.objects.difference(objects))

    def including(self, objects):
        return Floor(self.objects.union(objects))
