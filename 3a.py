def is_possible_triangle(sides):
    if len(sides) != 3:
        return False
    sides.sort()
    return sides[0] + sides[1] > sides[2]

def get_sides(line):
    sides_str = list(filter(lambda x : x is not '', line.split(' ')))
    return list(map(lambda x: int(x), sides_str))

def main():
    lines = open('input3.txt').read().strip().split('\n')
    print(sum( 1 for x in filter(lambda line: is_possible_triangle(get_sides(line)), lines) if x ))


if __name__ == '__main__':
    main()
