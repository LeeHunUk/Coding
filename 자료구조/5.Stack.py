"""
 $ 스택
   - 데이터를 제한적으로 접근할 수 있는 구조
   - 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
   - LIFO 후입선출 | 큐와 꺼내는 순서는 반대

 $ 활용
   - 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

 $ 장점
   - 구조가 단순해서, 구현이 쉽다.
   - 데이터 저장/읽기 속도가 빠르다.
 $ 단점
   - 데이터 최대 갯수를 미리 정해야 한다.
   - 저장 공간의 낭비가 발생할 수 있음
"""

# 재귀 함수
def recursive(data):
    if data < 0 :
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)

recursive(4)

# append, pop으로 스택 사용
data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)

data_stack.pop()

print(data_stack)