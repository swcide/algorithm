"""
https://www.acmicpc.net/problem/10250
너무길어 링크로 대체..


"""

"""
예제 입력 1   출력
2
6 12 10     402

30 50 72    1203


높이 만큼 층을 생성하고 
넓이 만큼 호수를 생성한다! 

일단 높이에 *100을 해서 앞자리를 맞춘후 
넓이만큼 += 1을 해주면 방의 개수가 완성된다.
"""


import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    h,w,N = map(int,input().split())
    list_h = []
    num= 1
    while w>=num:                # 반복문 종료 조건 >=로 한이유는 마지막 인덱스가 들어가지 않기 때문
        for i in range(1,h+1):   #반복문을 돌려 층수를 구해준다
            floor = i*100
            list_h.append(floor + num) #층수에 방번호를 더한것을 append
        num += 1
    print(list_h[N-1])              # 순차적으로 인덱스로 들어가기 때문에 손님 입장 번호 -1 (인덱스 0 부터시작)

"""    
전체 방의 갯수를 구한다.
이때 순차적으로 102호보다 201호를 선호하니
101,201,203
순으로 구하는 for문을 작성 

"""


# 101~109, 201~209 순으로 전체 구하기
# for i in range(1,h+1):
#     for j in range(1,w+1):
#         print((i*100)+j)

