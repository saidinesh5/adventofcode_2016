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


def main():
    #print(effective_sector_id('qzmt-zixmtkozy-ivhz-343[abxyz]'))
    #print(effective_sector_id('aaaaa-bbb-z-y-x-123[abxyz]'))
    #print(effective_sector_id('a-b-c-d-e-f-g-h-987[abcde]'))
    #print(effective_sector_id('not-a-real-room-404[oarel]'))
    #print(effective_sector_id('totally-real-room-200[decoy]'))

    rooms = open('input4.txt').read().strip().split('\n')
    print(sum(map(effective_sector_id, rooms)))


if __name__ == '__main__':
    main()
