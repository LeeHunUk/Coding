# 프로그래밍 연습
# 다음 함수를 재귀 함수를 활용해서 완성해서 1부터 num까지의 곱이 출력되게 만드세요

# 반복문
def multiple(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value

# 재귀 함수
def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)

# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요
import random
data = random.sample(range(100), 10)
print(data)

def sum(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum(data[1:])

print(sum(data))
print("==============")
# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요

# 나의 풀이
my_string = "MOTOR"

print(len(my_string))

def palindrome_test(my_string):
    if len(my_string) <= 1:
        return None
    else:
        if my_string == "".join(reversed(my_string)):
            return my_string
    return palindrome_test(my_string[1:-1])

print(palindrome_test(my_string))
print("==============")
# 실 풀이
def palindrome(string):
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

print(palindrome("OTRRTO"))
print(palindrome(my_string))
print("==============")
"""
1, 정수 n에 대해 
2. n이 홀수이면 3 X n + 1 을 하고,
3. n이 짝수이면 n 을 2로 나눕니다.
4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.
"""

# 나의 풀이
def one_test(num):
    print(num)
    if num == 1:
        return num
    else:
        if num%2 == 1:
            return one_test(int(3*num+1))
        else:
            return one_test(int(num/2))

one_test(30)

# 실 풀이
def func(n):
    print (n)
    if n == 1:
        return n
    
    if n % 2 == 1:
        return (func((3 * n) + 1))
    else:
        return (func(int(n / 2)))
print("==============")
"""
문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오

힌트: 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면,
f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴 찾기
출처: ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Taejon 2001 
"""
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    
    return func(data -1) + func(data - 2) + func(data - 3)

print(func(6))