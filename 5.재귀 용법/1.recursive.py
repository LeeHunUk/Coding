"""
    $ 재귀 용법
      - 함수 안에서 동일한 함수를 호출하는 형태
"""

# 팩토리얼을 구하는 알고리즘
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num

for num in range(10):
    print (factorial(num))

# 형태 2
def factorial(num):
    if num <= 1:
        return num
    
    return num * factorial(num - 1)