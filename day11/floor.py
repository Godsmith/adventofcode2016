class Floor:
    def __init__(self, id, set_=None):
        if set_ is None:
            set_ = set()
        self.id = id
        self._set = {o for o in set_}

    def __eq__(self, other):
        return type(self) == type(other) and self.objects == other.objects

    def __repr__(self):
        return self._set.__repr__()

    @property
    def objects(self):
        return self._set

    def is_legal(self):
        for s in self._set:
            if len(s) == 2:
                if s[1] == 'M':
                    if self._contains_generator_not_of_type(s[0]) and not s[0] + 'G' in self._set:
                        return False
        return True

    def _contains_generator_not_of_type(self, type):
        return len(list(filter(lambda x: len(x) == 2 and x[1] == 'G' and x[0] != type, self._set))) > 0

    def without(self, objects):
        return Floor(self.id, self.objects.difference(objects))

    def including(self, objects):
        return Floor(self.id, self.objects.union(objects))
