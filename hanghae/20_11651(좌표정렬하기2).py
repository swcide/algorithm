"""문제
2차원 평면 위의 점 N개가 주어진다.
좌표를 y좌표가 증가하는 순으로,
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음
출력하는 프로그램을 작성하시오.
"""

"""
예제 1           출력
5
0 4             1 2 
1 2             1 2
1 -1            2 2
2 2             3 3
3 3             0 4

일단 x 의 크기를 비교 작은 순으로 정렬 
x의 크기가 같으면 y크기순으로 비교
"""
import sys
input = sys.stdin.readline

n = int(input())
list_a = []
for _ in range(n):
    x,y = map(int,input().split())
    list_a.append([x,y])
print(list_a)

list_a.sort(key=lambda a: (a[1],-a[1]))
