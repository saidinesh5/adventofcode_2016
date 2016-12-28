import re

def rect(screen, A, B):
    for row in range(B):
        for column in range(A):
            screen[row][column] = True
    return screen

def rotate_column(screen, x, rotation):
    rows = len(screen)
    rotation = rotation%rows
    overflowing_elements = rotation
    remaining_elments = rows - rotation
    tmp = [None]*rotation

    #Save the overflowing items first
    for r in range(rotation):
        tmp[r] = screen[rows - rotation + r][x]

    #Move the current elements into their place
    for r in range(remaining_elments):
        screen[rows - r - 1][x] = screen[rows - rotation - r - 1][x]

    #Move the saved items back into their place
    for r in range(rotation):
        screen[r][x] = tmp[r]
    return screen

def rotate_row(screen, y, rotation):
    row = screen[y]
    screen[y] = row[-rotation:] + row[:-rotation]
    return screen

def popcount(screen):
    return sum(map(lambda row: sum(row), screen))

def dump(screen):
    pixels = [' ','#']
    for row in screen:
        print(''.join(list(map(lambda x: pixels[int(x)] , row))))
    print(''.join(['=']*len(screen[0])))

def process_instructions(instructions):
    rows = 6
    columns = 50
    screen = [[False for column in range(columns)] for row in range(rows)]

    for instruction in instructions:
        numbers = list(map(int, re.findall('\d+', instruction)))
        if instruction.startswith('rect'):
            screen = rect(screen, numbers[0], numbers[1])
        elif instruction.startswith('rotate column'):
            screen = rotate_column(screen, numbers[0], numbers[1])
        elif instruction.startswith('rotate row'):
            screen = rotate_row(screen, numbers[0], numbers[1])
        else:
            print('Ignoring instruction: ', instruction)

    dump(screen)

    return popcount(screen)


def main():
    instructions = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']
    instructions = open('input8.txt').read().strip().split('\n')
    print(process_instructions(instructions))

if __name__ == '__main__':
    main()
