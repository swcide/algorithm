"""
Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

"""



finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    if target in numbers:
        return True
    else:
        return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
