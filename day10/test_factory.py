from day10.factory import Factory


def test_init():
    factory = Factory()
    assert len(factory.bots) == 300
    assert len(factory.outputs) == 30


class TestExecuteString:
    def test_goes_to(self):
        factory = Factory()
        factory.execute_string('value 5 goes to bot 2')
        assert factory.bots[2].cargo == {5}

    def test_gives(self):
        factory = Factory()
        factory.execute_string('value 5 goes to bot 2')
        factory.execute_string('value 4 goes to bot 2')
        factory.execute_string('bot 2 gives low to bot 1 and high to output 0')
        assert factory.bots[2].cargo == set()
        assert factory.outputs[0].cargo == {5}
        assert factory.bots[1].cargo == {4}

    def test_multiline(self):
        instructions = """value 5 goes to bot 2
        bot 2 gives low to bot 1 and high to bot 0
        value 3 goes to bot 1
        bot 1 gives low to output 1 and high to bot 0
        bot 0 gives low to output 2 and high to output 0
        value 2 goes to bot 2"""
        factory = Factory()
        factory.execute_string(instructions)
        assert factory.outputs[0].cargo == {5}
        assert factory.outputs[1].cargo == {2}
        assert factory.outputs[2].cargo == {3}
        assert factory.bots[2].responsibilities == {5, 2}
