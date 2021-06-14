input = "hello my name is sparta"

'''
실패....
'''
# def find_max_occurred_alphabet(string):
#     alpabet_array = [chr(i+97) for i in range(26)]
#     arr = []
#     for i in alpabet_array:
#         if not string.isalpha():
#             for j in string:
#                 if i == j:
#                     arr.append(i)
#
#     check01 = arr[0]
#     for i in arr:
#         if ord(check01)< ord(i)
#
#
#     answer = 0
#
#
#     return answer

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if not i.isalpha():
            continue
        arr_index = ord(i) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence=0
    max_alphabet_index=0

    for index in range(len(alphabet_occurrence_array)):
        # print(alphabet_occurrence_array[index],'index')

        # index 0 --> alphabet_occurence =3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence >max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    answer = chr (max_alphabet_index+ord('a'))

    return answer

result = find_max_occurred_alphabet(input)
print(result)