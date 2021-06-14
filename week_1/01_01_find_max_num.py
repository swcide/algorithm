input = [3, 5, 2, 3, 4, 6, 1, 2, 4]


def find_max_num(array):
    a = max(array)
    for i in array:
        for j in array:
            '''
            i의 값이 j보다 작다면 break
            j의 값이 더 크다면 계속해 반복.
            for else.     
            if 문 안의 값이 break가 아닐 시 else를 출력함. 
            '''
            if i < j:
                print(i, ": i", j, ":j")
                '''
                3 : i 5 :j
                5 : i 6 :j
                2 : i 3 :j
                3 : i 5 :j
                4 : i 5 :j
                '''
                break
        else:
            print(i, "else")
            return i


result = find_max_num(input)
print(result)
