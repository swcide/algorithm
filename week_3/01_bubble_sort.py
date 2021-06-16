from builtins import print

input = [4, 6, 2, 9, 1]

"""
for i in range(5 - 1):         # 4번만 비교하면 되니까!
		for j in range(5 - i - 1): # Q. 여기서ㅓ왜 5 - i - 1 일까요? 
		    print(j)               # A. array[j] 와 array[j + 1] 을 비교할거라,
                               #    마지막 원소까지 가지 않아도 되기 때문이에요!

"""
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1): # 맨 마지막은 비교 할 필요가 없어서
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!





