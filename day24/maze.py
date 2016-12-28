from collections import namedtuple
from itertools import combinations, permutations


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self._width = len(maze[0])
        self._height = len(maze)

    def _is_wall(self, point):
        return self._is_character(point, '#')

    def _is_character(self, point, character):
        return self.maze[point.y][point.x] == character

    def shortest_route_length(self, start_character, end_character):
        starting_point = self._find_coordinates(str(start_character))
        end_point = self._find_coordinates(str(end_character))
        points_to_evaluate_next = [starting_point]
        points_evaluated = []
        moves = 0
        while True:
            points_to_evaluate = list(points_to_evaluate_next)
            points_to_evaluate_next = set()
            for point in points_to_evaluate:
                if point == end_point:
                    return moves
                neighboring_points = self._neighboring_points(point)
                neighboring_not_evaluated_points = [p for p in neighboring_points if p not in points_evaluated]
                neighboring_not_evaluated_not_wall_points = [p for p in neighboring_not_evaluated_points if
                                                             not self._is_wall(p)]
                points_to_evaluate_next.update(neighboring_not_evaluated_not_wall_points)
            moves += 1

    def fewest_steps_to_visit_all(self):
        route_lengths = {}
        special_characters = self._special_characters
        for start_character, end_character in combinations(special_characters, 2):
            length = self.shortest_route_length(start_character, end_character)
            route_lengths[(start_character, end_character)] = length
            route_lengths[(end_character, start_character)] = length

        complete_routes = [route for route in permutations(special_characters, len(special_characters)) if
                           route[0] == '0']
        complete_route_lengths = []
        for complete_route in complete_routes:
            routes = [(complete_route[i], complete_route[i + 1]) for i, _ in list(enumerate(complete_route))[:-1]]
            partial_route_lengths = [route_lengths[route] for route in routes]
            complete_route_lengths.append(sum(partial_route_lengths))
        return min(complete_route_lengths)

    @property
    def _special_characters(self):
        characters = set()
        for x in range(self._width):
            for y in range(self._height):
                character = self.maze[y][x]
                if character not in ['.', '#']:
                    characters.add(character)
        return characters


    def _find_coordinates(self, character):
        for x in range(self._width):
            for y in range(self._height):
                if self.maze[y][x] == character:
                    return Point(x=x, y=y)

    def _neighboring_points(self, point):
        return [Point(point.x - 1, point.y),
                Point(point.x + 1, point.y),
                Point(point.x, point.y + 1),
                Point(point.x, point.y - 1)]


Point = namedtuple('Point', ['x', 'y'])
