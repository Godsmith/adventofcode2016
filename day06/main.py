from day06 import most_frequent_for_each_position, least_frequent_for_each_position

with open('input.txt') as f:
    input_ = f.readlines()
    print(most_frequent_for_each_position(input_))
    print(least_frequent_for_each_position(input_))
