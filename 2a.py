def process_instructions(instructions = []):
    keypad  = ('123','456', '789')
    min_x, x, max_x = (0, 1, 2)
    min_y, y, max_y = (0, 1, 2)

    result = ''

    #Instructions are of the form [Turn][Move]
    for line in instructions:
        for char in line:
            if char is 'D':
                y = min(max_y, y + 1)
            elif char is 'U':
                y = max(min_y, y - 1)
            elif char is 'L':
                x = max(min_x, x - 1)
            elif char is 'R':
                x = min(max_x, x + 1)
            else :
                print('Ignoring instruction:')
        print(keypad[y][x])
        result += keypad[y][x]

    return result

def main():
    instructions = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    instructions = open('input2.txt').read().strip().split('\n')
    #print(instructions)
    print(process_instructions(instructions))

if __name__ == '__main__':
    main()
