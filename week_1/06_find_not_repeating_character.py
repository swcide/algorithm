'''
Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
 만약 그런 문자가 없다면 _ 를 반환하시오.


"abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

어캐하면 될까요.... 중복값 찾는건가... 맞나 아닌가..  중복값 찾는걸로 할게요...

'''


# solution


'''

alphabet_occurrence_array 배열에 각 빈도수를 저장하고, 
그 배열을 돌면서 not_repeating_character_array 라는 
배열에 반복되지 않는 문자를 다 집어넣습니다.
그리고 다시 한 번 문자열을 돌면서 해당 문자가 발견된다면 그 값을 반환하면 됩니다!

이 때, 1의 빈도수를 가진 인덱스를 알파벳으로 변환해서 
not_repeating_character_array 에 저장하면 됩니다.

그러면 not_repeating_character_array 에는 ["c", "d"]가 담기게 되는데, 
그 중 첫 번째인 "c" 를 반환하면 될까요? 그렇지 않습니다!

입력된 문자열 내에서 반복되지 않는 첫번째 문자를 찾아서 반환해줘야 하기 때문에 
string 을 다시 반복해서 돌면서 첫 번째 반복되지 않는 문자를 찾아 반환해주시면 됩니다!
'''


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if not i.isalpha():
            continue
        arr_index = ord(i) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character = []
    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]
        if alphabet_occurrence == 1:
            not_repeating_character.append(chr(i+ord('a')))

    print(not_repeating_character)

    index =0
    for i in string:

        if i in not_repeating_character:

            return i

    return"_"




print("정답 = d 현재 풀이 값 =", find_not_repeating_character("abadabac"))
print("정답 = c 현재 풀이 값 =", find_not_repeating_character("aabbcddd"))
print(" 정답 =_ 현재 풀이 값 =", find_not_repeating_character("aaaaaaaa"))