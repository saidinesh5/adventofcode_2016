from collections import defaultdict
from functools import reduce

def effective_sector_id(room):
    #If it is a real room, it returns the sector id, else 0
    components = room.split('-')
    roomname = components[:-1]
    last_component = components[-1]
    sector_id = int(last_component[: last_component.index('[')])
    checksum = last_component[last_component.index('[') + 1: last_component.index(']')]

    frequencies = defaultdict(int)
    for component in roomname:
        for c in component:
            frequencies[c] += 1

    rankings = list(map(lambda x: (x[1], x[0]), frequencies.items()))
    rankings = sorted(rankings, key = lambda kv: (-kv[0], kv[1]))
    computed_checksum = reduce( lambda x,y: x + y[1], rankings[:5], '')
    if computed_checksum == checksum:
        return sector_id
    return 0

def shift(char, offset):
    return chr( ord('a') + (ord(char) - ord('a') + offset)%26 )

def decrypt(room):
    components = room.split('-')
    roomname = components[:-1]
    last_component = components[-1]
    sector_id = int(last_component[: last_component.index('[')])

    decrypted_components = []
    for component in roomname:
        decrypted_components.append( ''.join(list( map( lambda c: shift(c, sector_id), component )  )) )

    return (' '.join(decrypted_components), sector_id)


def main():
    #print(decrypt('qzmt-zixmtkozy-ivhz-343[zimth]'))

    rooms = open('input4.txt').read().strip().split('\n')
    actual_rooms = filter(lambda room : effective_sector_id(room) > 0 , rooms)
    decrypted_rooms = map(decrypt, actual_rooms)
    for room in decrypted_rooms:
        if 'pole' in room[0]:
            print(room)


if __name__ == '__main__':
    main()
