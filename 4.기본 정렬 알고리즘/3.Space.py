"""
    $ 공간 복잡도
      - 시간복잡도와 공간복잡도 둘 다를 만족시키기는 어려움
      - 최근 대용량 시스템이 보편화되면서, 공간 복잡도보다는 시간 복잡도가 우선
      - 고정 공간 (알고리즘과 무관한 공간): 코드 저장 공간, 단순 변수 및 상수
      - 가변 공간 (알고리즘 실행과 관련있는 공간): 실행 중 동적으로 필요한 공간
"""

# 공간 복잡도 예제1
# n! 팩토리얼 구하기
# 공간 복잡도는 O(1)
def factorial(n):
    fac = 1
    for index in range(2, n + 1):
        fac = fac * index
    return fac

print(factorial(3))

# 재귀 함수로 1까지 호출하였을 경우
# 공간 복잡도는 O(n)
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1