from day10.container import Bot, Output


class Factory:
    def __init__(self):
        self.bots = []
        self.outputs = []
        self.containers = {'bot': self.bots, 'output': self.outputs}
        self.add_bots(300)
        self.add_outputs(30)

    def add_bots(self, n):
        for i in range(n):
            self.bots.append(Bot(n))

    def add_outputs(self, n):
        for i in range(n):
            self.outputs.append(Output(n))

    def execute_string(self, string):
        instructions = [s.strip() for s in string.split('\n')]
        instructions = [i for i in instructions if i != '']
        while len(instructions) > 0:
            s = instructions.pop(0)
            if 'goes to' in s:
                chip_value = int(s.split(' ')[1])
                bot_index = int(s.split(' ')[5])
                self.bots[bot_index].cargo.add(chip_value)
            if 'gives' in s:
                source_bot = self.bots[int(s.split(' ')[1])]
                low_recipient_index = int(s.split(' ')[6])
                high_recipient_index = int(s.split(' ')[11])
                low_recipient_type = s.split(' ')[5]
                high_recipient_type = s.split(' ')[10]
                if len(source_bot.cargo) == 2:
                    highest, lowest = source_bot.empty()
                    self.containers[low_recipient_type][low_recipient_index].cargo.add(lowest)
                    self.containers[high_recipient_type][high_recipient_index].cargo.add(highest)
                else:
                    instructions.append(s)
