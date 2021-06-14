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
    alpabet_array = [chr(i + 97) for i in range(26)]
    count = 0
    answer = ""
    max_alphabet = alpabet_array[0]
    for i in alpabet_array:
        alpha = 0
        for j in string:
            if j == i:
                alpha += 1

        if alpha > count:
            count = alpha
            answer = i

    return answer

result = find_max_occurred_alphabet(input)
print(result)
