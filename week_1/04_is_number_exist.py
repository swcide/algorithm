
'''.
다음과 같은 숫자로 이루어진 배열이 있을 때,
 이 배열 내에 특정 숫자가 존재한다면 True,
 존재하지 않다면 False 를 반환하시오.
 '''




def is_number_exist(number, array):

    # if number in array:
    #     return True
    # else:
    #     return False

    for element in array:  # array 의 길이만큼 아래 연산이 실행
        if number == element:  # 비교 연산 1번 실행
            return True
    return False

input = [3, 5, 6, 1, 2, 4]
result = is_number_exist(3, input)
print(result)