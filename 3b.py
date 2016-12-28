def is_possible_triangle(sides):
    if len(sides) != 3:
        return False
    sides.sort()
    return sides[0] + sides[1] > sides[2]

def get_numbers(line):
    sides_str = list(filter(lambda x : x is not '', line.split(' ')))
    return list(map(lambda x: int(x), sides_str))

def get_columns(numbers):
    columns = []

    for row in numbers:
        for column in range(len(row)):
            if column >= len(columns):
                columns.append([])
            columns[column].append(row[column])

    return columns

def get_triplets(column):
    result = []

    for i in range(0, len(column), 3):
        result.append( column[i : i+3] )

    return result

def main():
    #lines = ['101 301 501', '102 302 502', '103 303 503', '201 401 601', '202 402 602', '203 403 603']
    lines = open('input3.txt').read().strip().split('\n')
    numbers = list(map(get_numbers, lines))

    columns = get_columns(numbers)

    result = 0
    for column in columns:
        result += sum( 1 for x in filter(lambda triplet: is_possible_triangle(triplet), get_triplets(column)) if x )

    print(result)


if __name__ == '__main__':
    main()
