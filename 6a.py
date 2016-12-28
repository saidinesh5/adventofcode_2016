from collections import defaultdict

def get_columns(lines):
    columns = []

    for row in lines:
        for column in range(len(row)):
            if column >= len(columns):
                columns.append([])
            columns[column].append(row[column])

    return columns

def most_common_character(line):
    frequency = defaultdict(int)
    for c in line:
        frequency[c] += 1
    return max(frequency.items(), key = lambda x: x[1])[0]

def process_input(lines):
    return ''.join(list(map(lambda column: most_common_character(column), get_columns(lines))))

def main():
    #lines = ['eedadn', 'drvtee', 'eandsr', 'raavrd', 'atevrs', 'tsrnev', 'sdttsa', 'rasrtv', 'nssdts', 'ntnada', 'svetve', 'tesnvt', 'vntsnd', 'vrdear', 'dvrsen', 'enarar']
    lines = open('input6.txt').read().strip().split('\n')
    result = process_input(lines)
    print(result)


if __name__ == '__main__':
    main()
