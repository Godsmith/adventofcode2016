from day24.maze import Maze

with open('input.txt') as f:
    maze = [line[:-1] for line in f.readlines()]
    print(Maze(maze).fewest_steps_to_visit_all())
