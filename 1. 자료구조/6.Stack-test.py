# 연습문제1
# : 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]

    return data

for index in range(10):
    push(index)

pop()

print(stack_list)