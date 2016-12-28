def process_instructions(instructions = []):
    keypad  = ('  1  ',
               ' 234 ',
               '56789',
               ' ABC ',
               '  D  ')
    min_x, x, max_x = (0, 0, 4)
    min_y, y, max_y = (0, 2, 4)

    next_x, next_y = x, y

    result = ''
    #Instructions are of the form [Turn][Move]
    for line in instructions:
        for char in line:
            if char is 'D':
                next_x = x
                next_y = min(max_y, y + 1)
            elif char is 'U':
                next_x = x
                next_y = max(min_y, y - 1)
            elif char is 'L':
                next_x = max(min_x, x - 1)
                next_y = y
            elif char is 'R':
                next_x = min(max_x, x + 1)
                next_y = y
            else :
                print('Ignoring instruction:', char)

            if keypad[next_y][next_x] is not ' ':
              x, y = next_x, next_y

        result += keypad[y][x]

    return result

def main():
    #instructions = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    instructions = open('input2.txt').read().strip().split('\n')
    #print(instructions)
    print(process_instructions(instructions))

if __name__ == '__main__':
    main()
