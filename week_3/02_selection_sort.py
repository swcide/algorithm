"""
[4, 6, 2, 9, 1]  # 정렬되지 않은 배열

1단계 : [4, 6, 2, 9, 1]
        4와 6과 2와 9와 1을 차례차례 비교합니다.
	      그 중 가장 작은 1과 맨 앞 자리인 4를 교체합니다!
       [1, 6, 2, 9, 4] 이렇게요!

자, 그러면 이제 가장 작은 숫자인 1이 맨 앞으로 왔습니다.
가장 작은 걸 가장 맨 앞으로 옮기기로 했으니까요!
그러면, 맨 앞자리를 제외하고 다시 한 번 반복하면 됩니다.

2단계 : [1, 6, 2, 9, 4]
           6과 2와 9와 4를 차례차례 비교합니다.
           그 중 가장 작은 2와 두번째 앞 자리인 6을 교체합니다!
       [1, 2, 6, 9, 4] 이렇게요!

3단계 : [1, 2, 6, 9, 4]
              6과 9와 4를 차례차례 비교합니다.
              그 중 가장 작은 4와 세번째 앞 자리인 6을 교체합니다!
       [1, 2, 4, 9, 6] 이렇게요!

4단계 : [1, 2, 4, 9, 6]
                 9와 6을 비교합니다!
                 그 중 가장 작은 6과 네번째 앞 자리인 9을 교체합니다!
       [1, 2, 4, 6, 9] 이렇게요!

"""
"""
for i in range(5 - 1):     # Q. 여기서 왜 5 - 1 일까요?
		for j in range(5 - i): # A. 맨 마지막 비교는 하지 않아도 되기 때문입니다!
		    print(i + j)       #    위의 예시에서 4번째 비교를 하면
                           #    [1, 2, 4, 6, 9] 로 변경이 되는데,
                           #    굳이 9와 9를 비교할 필요가 없기 때문이에요! 
                           #    앞에 다 최솟값이 갔으니 알아서 잘 가 있겠지? 하는 느낌입니다.

"""
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i+j]<array[min_index]:
                min_index = i+j
        array[i], array[min_index] =array[min_index],array[i]

    return array


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!