class DragonCurveGenerator:
    @staticmethod
    def step(a):
        b = reversed(a)
        b = ''.join(['1' if c == '0' else '0' for c in b])
        return a + '0' + b

    @staticmethod
    def checksum(a):
        if len(a) % 2 == 1:
            return a
        pairs = DragonCurveGenerator._chunks(a, 2)
        new_string = ''.join(['1' if p[0] == p[1] else '0' for p in pairs])
        return DragonCurveGenerator.checksum(new_string)

    @staticmethod
    def checksum_of_filled_disk(length, state):
        if len(state) < length:
            return DragonCurveGenerator.checksum_of_filled_disk(length, DragonCurveGenerator.step(state))
        state = state[:length]
        return DragonCurveGenerator.checksum(state)


    @staticmethod
    def _chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]


print(DragonCurveGenerator.checksum_of_filled_disk(272, '11101000110010100'))
print(DragonCurveGenerator.checksum_of_filled_disk(35651584, '11101000110010100'))
