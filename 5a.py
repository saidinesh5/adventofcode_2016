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
    result = ''
    for i in range(8):
        result += next(hash_generator)[5]
    return result

def main():
    #door_id = 'abc'
    door_id = 'ffykfhsq'
    print(get_password(door_id))

if __name__ == '__main__':
    main()
