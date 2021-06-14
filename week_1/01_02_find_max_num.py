input = [3, 5, 2, 3, 4, 6, 1, 2, 4]

'''
두 코드의 차이 !!
시간복잡도에대해 자세히 알진 못하지만 아마 시간복잡도가 적은듯?

'''

def find_max_num(array):
    max_num = array[0]

    for i in array:
        if i > max_num:
            max_num = i

    return max_num

result = find_max_num(input)
print(result)
