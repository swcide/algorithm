from builtins import range

input = "hello my name is sparta"

'''
str.isalpha() 함수를 이용하면 문자열이 알파벳인지 확인가능!

print("a".isalpha())    # True
print("1".isalpha())    # False

s = "abcdefg"
print(s[0].isalpha())   # True


# 내장 함수 ord() 이용해서 아스키 값 받기
print(ord('a'))               # 97
print(ord('a') - ord('a'))    # 97-97 -> 0
print(ord('b') - ord('a'))    # 98-97 -> 1

print(chr(65))                # A
print(chr(65))                # Z

'''

'''
알파벳 별 인덱스에 값을 추가 한다!

how to??
ord로 뽑은 번호가 input된 알파벳의 인덱스 번호!
그 인덱스 번호에 값을 1씩 추가해주면 될 것 같다.
정답을 보니 소문자만이다.. 
대문자도 포함시키려면 lower 이용하면 될것같다.


'''


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:

        if not i.isalpha():
            continue
        arr_index = ord(i)-ord('a')
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array

print("정답 = [3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =", find_alphabet_occurrence_array("Hello my name is sparta"))
print("정답 = [2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("Sparta coding club"))
print("정답 = [2, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 3, 3, 0, 0, 0, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best sparta"))
