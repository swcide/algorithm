"""
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.


"""

"""
예제  1    출력 
2           8
4 2
 

"""

n = int(input())
a = list(map(int, input().split()))

# print(max(a)*min(a))

"""
좀더 어렵게 푸는 방법 이 있을 것 같아 좀 끄적여본다.

"""

