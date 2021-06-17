"""
문제
자연수 과 정수 가 주어졌을 때 이항 계수
를 구하는 프로그 램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력

를 출력한다.

예제 입력 1
5 2
예제 출력 1
10
"""''

a, b = map(int, input().split())


def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


print(int(factorial(a) / (factorial(b) * factorial(a - b))))

"""
이항개수의 값을 구하는 공식을 활용한다!

    n                               n!
    k   일때 이 값을 구하는 공식은 k!(n-k)! 이라고 한다.
                             
"""
