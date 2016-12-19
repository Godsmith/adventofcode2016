import hashlib
from functools import lru_cache

from day14.key_generator import KeyGenerator


class StretchingKeyGenerator(KeyGenerator):
    @lru_cache(maxsize=None)
    def _md5(self, index):
        m = hashlib.md5()
        m.update(self._salt)
        m.update(str(index).encode('utf-8'))
        hash_ = m.hexdigest()
        for _ in range(2016):
            m = hashlib.md5()
            m.update(hash_.encode('utf-8'))
            hash_ = m.hexdigest()
        return hash_
