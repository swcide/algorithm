"""
Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.

"""

finding_target = 77
finding_numbers = [i for i in range(100)]


def is_existing_target_number_binary(target, array):
    arr_min = 0
    arr_max = len(array)-1
    cen = (arr_min+arr_max)//2
    find_count = 0
    while arr_min <= arr_max:
        find_count += 1
        if array[cen] == target:
            print(find_count)
            return True
        elif array[cen] < target:
            arr_min = cen + 1
        else:
            arr_max = cen -1
        cen = (arr_max+arr_min)//2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

