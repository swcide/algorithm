

'''
Q. 0과 1로만 이루어진 문자열이 주어졌을 때,
이 문자를 모두 0, 혹은 모두 1로 같게 만들어야 한다.
할 수 있는 행동은 연속된 하나의 숫자를 잡고 모두 뒤집는 것 이다.
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


'''



input = "0101110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    zero =0
    one = 0

    if string[0] == '0':
        one += 1
    elif string[0] == '1':
        zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                one += 1
            if string[i+1] == '1':
                zero += 1

    return min(zero, one)



result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)