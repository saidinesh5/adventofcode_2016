def process_instructions(instructions = []):
    # [ East, South, West, North ]
    orientations = ( (1,0), (0,-1), (-1,0), (0,1) )
    current_position = [0,0]
    current_orientation = 3

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
        current_position = ( current_position[0] + move*orientation[0], current_position[1] + move*orientation[1] )

    print(current_position)
    return abs(current_position[0]) + abs(current_position[1])

def main():
    #instructions = 'R2, L3'.split(', ')
    #instructions = 'R2, R2, R2'.split(', ')
    #instructions = 'R5, L5, R5, R3'.split(', ')
    instructions = open('input1.txt').read().split(', ')
    #print(instructions)
    print(process_instructions(instructions))

if __name__ == '__main__':
    main()
