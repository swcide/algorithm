'''
Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
[2, 3, 5, 7, 11, 13, 17, 19]


'''



# def find_prime_list_under_number(number):
#     answer = []
#     for n in range(2,number+1):
#         for i in range(2,n):
#             print(n%i ,n,"%",i)
#             if n%i ==0:
#                 break
#         else: answer.append(n)
#
#     return answer
'''
1차 개선

숫자가 19가 들어왔다고 해볼게요. 

2, 3, 4, 5, 6, 7, 8, 9, ... 19까지 한 번씩 다 나누면서 나머지가 0인지 확인합니다. 

그러나 2와 3으로 나누어 떨어지지 않는다면,
 2 X 3 인 6으로도 당연히 안 나누어 떨어집니다. 
 즉, 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라,
  2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보도록 개선해봅시다.

그러면, 뭐가 소수인지는 어떻게 알 수 있을까요? 바로, 
직전에 찾은 소수들을 이용하면 됩니다.

'''
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):
#         for i in prime_list:
#
#             if n % i == 0:
#                 print(n % i, n, "%", i)
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list

'''
2차 개선

한 번 소수의 특징을 다시 생각해볼게요.

주어진 자연수 N이 소수이기 위한 필요충분 조건은 
N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
 수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 
 둘 중 하나는 반드시 N의 제곱근 이하이기 때문입니다.

이를 이용해서 i * i ≤ n 일 때까지만 비교하시면 됩니다!

'''
input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)