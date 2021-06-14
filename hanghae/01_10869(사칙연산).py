"""
두 자연수 A와 B가 주어진다.
이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를
출력하는 프로그램을 작성하시오.

첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B,
넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
ex
7 3
>>>
10
4
21
2
1

"""

a, b = map(int,input().split())

# def solution(n, n2):
#     a = n + n2
#     b = n - n2
#     c = n * n2
#     d = n // n2
#     e = n % n2
#
#     return print(f"{a}\n{b}\n{c}\n{d}\n{e}")

# solution(a,b)


# a = int(a)
# b = int(b)


print(a +b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)


