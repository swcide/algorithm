'''

Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어
결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.

단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리,
모든 연산은 왼쪽에서 순서대로 이루어진다.

1. 인덱스 끼리 더했을 때
2. 인덱스 끼리 곱했을 떄

값을 비교해서 더 큰값을 넣는다!
'''

#-------------------solution--------------------------
'''

곱하기 혹은 더하기를 해서 가장 큰수를 반환해라!
라고 하면 4 + 9 = 13, 4 ✕ 9 = 36 이니까 당연히 ✕ 를 항상 해야 하는 거 아니야?!

라고 해서 모든 값을 ✕ 해버리면 최대의 값이 나오지 않습니다.
왜냐면 1 혹은 0 같은 경우는 곱하는 것보다 더하는 게 좋기 때문입니다!
3 x 1 = 3 보다, 3 + 1 = 4 를 하는 게 더 큰 수를 가질 수 있으니까요!

자, 그러면 이제 총 계산된 값을 구하기 위한 합계 변수를 두겠습니다.
이제 반복문을 돌면서 합계 변수에 더하거나 곱해 나갈텐테,
마찬가지로 합계가 1 이하일 때 더하는 게 좋습니다. (1 x 2 보다는 1 + 2 가 더 크기 때문입니다!)

다시 정리하면, 합계와 현재 숫자가 1보다 작거나 같다면 더합니다. 그 외에는 전부 곱하면 되구요!

'''


def find_max_plus_or_multiply(array):
    multiply_sum =0

    for i in array:
        if i <= 1 or multiply_sum <= 1:
            multiply_sum += i
        else:
            multiply_sum *= i




    return multiply_sum

input = [0, 3, 5, 6, 1, 2, 4]
result = find_max_plus_or_multiply(input)
print(result)
