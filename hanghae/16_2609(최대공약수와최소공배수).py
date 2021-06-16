"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


"""
from functools import reduce

"""
예제 1    출력 1
24 18       6
            72
"""
dic={
    "name":'name'
}

'''
처음코드 답은 잘 나오는 것 같은데 시간초과 뜬다..

def solution(n):
    list_n = []
    for i in range(2, n + 1):
        if n % i == 0:
            list_n.append(i)
    return list_n

def solution2(a,b):
    list_n =[]

    for i in range(1,a*b):
        for j in range(1,a*b):
            if a*i==b*j:
                list_n.append(a*i)

    print(min(list_n))

a, b = map(int, input().split())

list_a = solution(a)
list_b = solution(b)


ans =[]
for i in list_a:
    for j in list_b:
        if i == j:
            ans.append(i)

print(max(ans))
solution2(a,b)
'''
a, b = map(int, input().split())

for i in range(min(a,b), 0 ,  -1):
    if a% i == 0 and b%i ==0:
        print(i)
        break
for i in range(max(a, b), (a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break


"""
import math
내장함수를 사용한 최소공배수 최대공약수 구하기
 
a, b = map(int, input().split()) 
print(math.gcd(a, b)) 
print(math.lcm(a, b))

"""