# 연습1 : 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수 : key % 8
# 2. 해쉬 키 생성 : hash(data)

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')

print(read_data('Dave'))
print(hash_table)
print("==============")

# 충돌 해결 알고리즘 (좋은 해쉬 함수 사용하기)
# 1. Chaining 기법 - 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용
# 연습 2 : 위의 코드에 Chaining 기법으로 충돌해결 코드 추가

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

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

# hash 값이 달리질 수도 있음 
save_data('Data', '0102030200')
save_data('Dd', '01033232200')

print(read_data('Data'))
print(hash_table)
print("==============")

# 2. Linear Probing 기법 - 충돌이 일어나면 다음 주소부터 맨 처음 나오는 빈공간에 저장
# 연습 3 : 위의 코드에 Linear Probing 기법으로 충돌해결 코드 추가

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1]= value
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None