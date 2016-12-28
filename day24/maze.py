from collections import namedtuple


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
