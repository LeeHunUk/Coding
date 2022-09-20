"""
    $ 정렬이란?
      - 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
    
    $ 버블 정렬이란?
      - 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

    $ 삽입 정렬이란?
      - 두번째 인덱스에서 시작
      - 해당 인덱스 앞에 있는 데이터부터 비교해서 key 값이 더 작으면, 데이터값을 뒤 인덱스로 복사
"""
# 버블 정렬
def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        
        if swap == False:
            break
    return data

import random

data_list = random.sample(range(100), 50)
print(data_list)
print("==============================")
print (bubblesort(data_list))
print("==============================")

# 삽입 정렬
def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data

import random

data_list1 = random.sample(range(100), 50)
print(data_list1)
print("==============================")
print (insertion_sort(data_list1))