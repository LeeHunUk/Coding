"""
 $ 해쉬 구조
   - Hash Table : 키에 데이터를 저장하는 데이터 구조
   - 파이썬은 딕셔너리 타입을 사용 
 $ 장단점
   - 장점 : 데이터 저장/읽기 속도가 빠르다.
   -  : 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
   - 단점 : 일반적으로 저장공간이 좀 더 필요하다. 
   -  : 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
 $ 주요 용도
   - 검색이 많이 필요한 경우
   - 저장, 삭제, 읽기가 빈번한 경우
   - 캐쉬 구현시
"""

# Hash Table 만들기
hash_table = list([0 for i in range(10)])
print(hash_table)
print("=============")

# 해쉬 함수 만들기
def hash_func(key):
  return key % 5

# 해쉬 테이블 저장
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord():문자의 ASCII(아스키)코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))
print("=============")

# 값 저장
def storage_data(data, value):
  key = ord(data[0])
  hash_address = hash_func(key)
  hash_table[hash_address] = value

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01077773333')

# 실제 데이터 저장, 읽기
def get_data(data):
  key = ord(data[0])
  hash_address = hash_func(key)

  return hash_table[hash_address]

print(get_data('Andy'))