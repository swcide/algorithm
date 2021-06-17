"""
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에,
최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때,
3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면,
더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때,
봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
"""

"""
예제 1    출력
18          4 
예제 2    출력 
4          -1
예제 3    출력 
6           2
예제 4    출력     
9           3
예제 5    출력
11          3
"""

"""
5배수일 떄와 3의 배수일 떄를 구한다
5의 배수일 떄는 제일 몫이 적은 값
3의 배수일때는 큰 값.

5로 나눈 나머지가 3의 배수일 경우에만 count를 추가
반례 21 .
15 + 6

n 의 조합이 5의 배수 + 3의 배수일떄 가장 적은 값을 구해야 겠다.

n = int(input())
count = 0
for i in range(n):
    if n % 5 == 0:
        count = n // 5
        break
    for j in range(n):
        test = (5 * i) + (3 * j)
        if test == n:
            count = i + j
        elif count==0:
            count = -1
if count == 0:
    if n % 3 == 0:
        count = n // 3

print(count)

-------- 시간초과남!!!!!!!!!!!!!!

"""
n = int(input())
count = 0
for i in range(n):
    if n % 5 == 0:
        count = n // 5
        break
    for j in range(n):
        test = (5 * i) + (3 * j)
        if test == n:
            count = i + j
        elif count==0:
            count = -1

if count == 0:
    if n % 3 == 0:
        count = n // 3

print(count)

"""
시간초과 나지 않는 풀이법
"""
# bag = 0
# while n >= 0 :
#     if n % 5 == 0 :  # 5의 배수이면
#         bag += (n // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         print('zz')
#         break
#     print('일단여기지?')
#     n -= 3
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)
