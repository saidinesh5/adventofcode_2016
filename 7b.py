import re
from functools import reduce

def get_ABAs(component):
    result = set()
    for i in range(len(component) - 2):
        if component[i] == component[i+2] and component[i] != component[i+1]:
            result.add(component[i:i+3])
    return result

def supports_ssl(ip):
    hypernet_sequences = re.findall('\[.*?\]', ip)
    supernet_sequences = re.split('\[.*?\]', ip)

    abas_supernet = reduce(lambda x,y: x.union(get_ABAs(y)), supernet_sequences, set())
    abas_hypernet = reduce(lambda x,y: x.union(get_ABAs(y)), hypernet_sequences, set())
    babs = set(map(lambda x: x[1] + x[0] + x[1] , abas_supernet))

    return len(babs.intersection(abas_hypernet)) > 0

def main():
    #print(supports_ssl('aba[bab]xyz'))
    #print(supports_ssl('xyx[xyx]xyx'))
    #print(supports_ssl('aaa[kek]eke'))
    #print(supports_ssl('zazbz[bzb]cdb'))
    lines = open('input7.txt').read().strip().split('\n')
    print(len( list( filter(supports_ssl, lines) ) ))


if __name__ == '__main__':
    main()
