import hashlib

def get_hashes(door_id):
    i = 0
    while True:
        m = hashlib.md5()
        m.update((door_id + str(i)).encode(encoding='utf-8'))
        hash = m.hexdigest()
        if hash.startswith('00000'):
            yield hash
        i += 1

def get_password(door_id):
    hash_generator = get_hashes(door_id)
    result = [None]*8
    characters_left = 8

    while characters_left > 0:
        hash = next(hash_generator)
        position = int(hash[5], 16)
        if position >= 0 and position < 8 and result[position] is None:
            result[position] = hash[6]
            characters_left -= 1

    return ''.join(result)

def main():
    #door_id = 'abc'
    door_id = 'ffykfhsq'
    print(get_password(door_id))

if __name__ == '__main__':
    main()
