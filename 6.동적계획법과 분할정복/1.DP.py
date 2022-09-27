"""
    $ 동적 계획법
      - 입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 
        보다 큰 크기의 부분 문제를 해결, 최종적으로 전체 문제를 해결하는 알고리즘
    
    $ 분할 정복
      - 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
"""

# 피보나치 수열

# 재귀용법
def fibo(num):
    if num <=1:
        return num
    
    return fibo(num - 1)+ fibo(num - 2)

print(fibo(4))
print("=============")

# 동적 계획법 활용
def fibo_dp(num):
    cache = [ 0 for i in range(num+1) ]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]

print(fibo_dp(10))
print("=============")