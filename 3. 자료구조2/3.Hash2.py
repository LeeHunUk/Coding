# 빈번한 충돌을 개선하는 기법
# 저장 공간을 확대

# SHA 해쉬 함수 사용
# SHA-1
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()

# hash_object.update(b'test') 와 같음
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA-256
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha256()

# hash_object.update(b'test') 와 같음
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
print("=====================")

# Chaining 기법을 sha256으로 사용

hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0]==index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0]==index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

save_data('da', '0102030200')
save_data('dh', '01033232200')

print(read_data('dh'))
print(hash_table)
print("==============")
