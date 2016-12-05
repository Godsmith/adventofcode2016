import hashlib


class Door:
    def __init__(self, id):
        self.id = id
        self.hashes = {}
        self.advanced_password = [None] * 8

    def hash(self, index):
        if index in self.hashes:
            return self.hashes[index]
        m = hashlib.md5()
        m.update(self.id.encode())
        m.update(str(index).encode())
        hexdigest = m.hexdigest()
        self.hashes[index] = hexdigest
        return hexdigest

    def hash_indicates_next_character_in_password(self, index):
        return self.hash(index)[:5] == '00000'

    def password_character(self, index):
        return self.hash(index)[5]

    def advanced_password_character_location(self, index):
        return self.password_character(index)

    def advanced_password_character(self, index):
        return self.hash(index)[6]

    def password(self):
        out = ''
        i = 0
        while len(out) < 8:
            if self.hash_indicates_next_character_in_password(i):
                out += self.password_character(i)
                print(str(i) + '/' + str(len(out)))
            i += 1
        return out

    def try_insert_in_advanced_password(self, index):
        if self.hash_indicates_next_character_in_password(index):
            location = self.advanced_password_character_location(index)
            if location.isdigit():
                location_int = int(location)
                if location_int < 8:
                    if self.advanced_password[location_int] is None:
                        self.advanced_password[location_int] = self.advanced_password_character(index)
                        return True
        return False

    def generate_advanced_password(self):
        i = 0
        while True:
            if self.try_insert_in_advanced_password(i):
                print(self.advanced_password)
                if not None in self.advanced_password:
                    return ''.join(self.advanced_password)
            i += 1
