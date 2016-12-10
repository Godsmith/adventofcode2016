from day10.factory import Factory

with open('input.txt') as f:
    factory = Factory()
    factory.execute_string(f.read())
    for i, bot in enumerate(factory.bots):
        if bot.responsibilities == {61, 17}:
            print(i)
    print(list(factory.outputs[0].cargo)[0] * list(factory.outputs[1].cargo)[0] * list(factory.outputs[2].cargo)[0])
