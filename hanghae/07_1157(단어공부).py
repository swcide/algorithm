"""
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.


"""
word = input()

a = word.upper()
alpha_index = [0]*26
answer = []

for i in a:
    index = ord(i)-ord('A')
    alpha_index[index] += 1

max_index = max(alpha_index)

for i in range(len(alpha_index)):
    if alpha_index[i] == max_index:
        answer.append(i)

if len(answer)>1:
    print('?')
else:
    print(chr(answer[0]+65))


"""
어마무시하게 수정했다.

처음에는 모든 알파벳이 담겨있는 list를 만들고
input받은 word를 하나하나 대입해 가면서 체크 한뒤에 새로운 list에 append 해서
다시 또 그 안의 중복 된 알파벳을 체크하려 하였으나 
중복된 구간이 계속 생겨서 갈아엎었다..

곰곰히 생각해본 결과 알파벳의 index에 값을 저장하고
가장 큰 index번호를 리턴 하는게 좋을것 같다고 생각해 인덱스 번호를 chr로 바꿔 리턴 하려 했으나
?의 경우를 생각 하지 않았다!

당장에 생각나는건 리스트를 새로 만들어 length가 1이 넘으면 ?를 넘겨주는 식으로 했다..
근데시간이 무지오래걸린다..
다른 사람들걸 보면서 좀 더 참고해야겠다.

"""


