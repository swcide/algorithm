"""

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

"""

"""시간초과!!!!!!
# prime_list = []
# a,b = map(int,input().split())
#
#
# for n in range(4, b + 1):
#     for i in prime_list:
#         if n % i == 0 and i * i <= n:
#             break
#     else:
#         prime_list.append(n)
#
# for i in prime_list:
#     if a <= i <= b :
#         print(i)

"""

"""에라토스테네스의 체 이용 풀이"""


# import math
# a = 1
# b = 1000
# end = int(math.sqrt(b))
# for i in range(2,end):
#     print(b % i,"소수 ",i)

# n=1000
# a = [False,False] + [True]*(n-1)
# primes=[]
# print(a)
#
# for i in range(2,n+1):
#     # print(a[i])
#     if a[i]:
#         primes.append(i)
#     for j in range(2*i, n+1, i):
#         print(j)
#         a[j] = False
# print(primes)

"""이거 너무 천재적이다.."""
max =1000000
sieve = [True]*max
sieve2 = [0]*max
sieve[0], sieve[1] = [False]*2
i = 2
while i <= max-1:
    if sieve[i]:
        for j in range(i+i, max, i):  # i+i로 범위를 줄이고  i의 배수를 이용해서 배수일 경우엔 제외한다 !

            if sieve[j]:
                sieve[j] = False
                sieve2[j] =j

    i += 1


m, n = map(int, input().split())

for i in range(m, n+1):
    if sieve[i]:
        print(i)