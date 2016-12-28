class Computer:
    def __init__(self):
        self.registers = {}

    def evaluate(self, instructions, instruction_index=0):
        while instruction_index < len(instructions):
            instruction = instructions[instruction_index]
            print(self.registers, instruction)
            list_ = instruction.split(' ')
            if list_[0] == 'cpy':
                if list_[1] in self.registers:
                    self.registers[list_[2]] = self.registers[list_[1]]
                else:
                    self.registers[list_[2]] = int(list_[1])
            elif list_[0] == 'inc':
                self.registers[list_[1]] += 1
            elif list_[0] == 'dec':
                self.registers[list_[1]] -= 1
            elif list_[0] == 'jnz':
                if list_[1].isdigit():
                    value = int(list_[1])
                else:
                    if list_[1] in self.registers:
                        value = self.registers[list_[1]]
                    else:
                        value = 0
                if value != 0:
                    if list_[2] in self.registers:
                        instruction_index += self.registers[list_[2]]
                    else:
                        instruction_index += int(list_[2]) - 1  # -1 due to always moves one step forward
            elif list_[0] == 'tgl':
                if list_[1].isdigit():
                    offset = int(list_[1])
                else:
                    offset = self.registers[list_[1]]
                if instruction_index + offset < len(instructions):
                    i = instructions[instruction_index + offset]
                    if len(i.split(' ')) == 2:
                        if 'inc' in i:
                            instructions[instruction_index + offset] = i.replace('inc', 'dec')
                        else:
                            instructions[instruction_index + offset] = 'inc' + i[3:]
                    else:
                        if 'jnz' in i:
                            instructions[instruction_index + offset] = i.replace('jnz', 'cpy')
                        else:
                            instructions[instruction_index + offset] = 'jnz' + i[3:]

            instruction_index += 1

    def register(self, x):
        return self.registers[x]
