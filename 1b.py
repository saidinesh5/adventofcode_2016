def get_points(line):
    result = set()
    x_low = min(line[0][0], line[1][0])
    x_high = max(line[0][0], line[1][0])
    y_low = min(line[0][1], line[1][1])
    y_high = max(line[0][1], line[1][1])
    for x in range(x_low, x_high + 1):
        for y in range(y_low, y_high + 1):
            result.add((x,y))
    return result

def get_intersection(line1, line2):
    #each line is basically a line segment represented by (startPoint, endPoint)
    intersection = get_points(line1).intersection( get_points(line2) )
    if len(intersection) is 0:
        return None
    return list(intersection)[0]

def get_endpoint(visited, next_position):
    if len(visited) < 2:
        return (False, next_position)

    current_line = (visited[-1], next_position)

    for i in range(len(visited) - 2):
        intersection = get_intersection( (visited[i], visited[i+1]), current_line)
        if intersection is not None:
            return (True, intersection)

    return (False, next_position)

def process_instructions(instructions = []):
    # [ East, South, West, North ]
    orientations = ( (1,0), (0,-1), (-1,0), (0,1) )
    current_position = [0,0]
    current_orientation = 3

    visited = [(0,0)]

    #Instructions are of the form [Turn][Move]
    for instruction in instructions:
        turn = instruction[0]
        move = int(instruction[1:])
        if turn[0] is 'L':
            current_orientation = (current_orientation - 1)%len(orientations)
        elif turn[0] is 'R':
            current_orientation = (current_orientation + 1)%len(orientations)
        else:
            print('Ignoring instruction:', instruction)
            continue
        orientation = orientations[current_orientation]
        next_position = ( current_position[0] + move*orientation[0], current_position[1] + move*orientation[1] )

        end_trip, current_position = get_endpoint(visited, next_position)

        if not end_trip:
            visited.append(next_position)
        else:
            print('Already visited: ', current_position)
            break

    print(current_position)
    return abs(current_position[0]) + abs(current_position[1])

def main():
    #instructions = 'R8, R4, R4, R8'.split(', ')
    instructions = open('input1.txt').read().split(', ')
    #print(instructions)
    print(process_instructions(instructions))

if __name__ == '__main__':
    main()
