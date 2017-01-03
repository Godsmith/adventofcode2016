from day13.location import location

# for y in range(40):
#     print(''.join([location(x, y, 1362) for x in range(32)]))

locations_to_investigate_next = {(1, 1)}
visited_locations = set()
for step in range(51):
    locations_to_investigate = set(locations_to_investigate_next)
    locations_to_investigate_next = set()
    for current_location in locations_to_investigate:
        adjacent_locations = {(current_location[0] + 1, current_location[1]),
                              (current_location[0] - 1, current_location[1]),
                              (current_location[0], current_location[1] + 1),
                              (current_location[0], current_location[1] - 1)}
        adjacent_valid_locations = {adjacent_location for adjacent_location in adjacent_locations if
                                    adjacent_location[0] >= 0 and adjacent_location[1] >= 0 and location(
                                        adjacent_location[0], adjacent_location[1], 1362) == '.'}
        locations_to_investigate_next.update(adjacent_valid_locations)
        visited_locations.add(current_location)
    locations_to_investigate_next = locations_to_investigate_next.difference(visited_locations)

print(sorted(list(visited_locations)))
print(len(visited_locations))
