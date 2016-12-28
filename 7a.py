import re
from functools import reduce

def has_ABBA(component):
    for i in range(len(component) - 3):
        if component[i] == component[i+3] and component[i+1] == component[i+2] and component[i] != component[i+1]:
            return True
    return False

def supports_tls(ip):
    hypernet_sequences = re.findall('\[.*?\]', ip)
    non_hypernet_sequences = re.split('\[.*?\]', ip)

    hypernet_sequences_contains_abba = reduce(lambda x,y: x or has_ABBA(y), hypernet_sequences, False)
    non_hypernet_sequences_contains_abba = reduce(lambda x,y: x or has_ABBA(y), non_hypernet_sequences, False)

    return non_hypernet_sequences_contains_abba and not hypernet_sequences_contains_abba

def main():
    #print(supports_tls('abba[mnop]qrst'))
    #print(supports_tls('abcd[bddb]xyyx'))
    #print(supports_tls('aaaa[qwer]tyui'))
    #print(supports_tls('ioxxoj[asdfgh]zxcvbn'))
    lines = open('input7.txt').read().strip().split('\n')
    print(len( list( filter(supports_tls, lines) ) ))


if __name__ == '__main__':
    main()
