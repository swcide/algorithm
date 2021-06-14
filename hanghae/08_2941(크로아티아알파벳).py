"""
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

크로아티아 알파벳	    변경
č	                c=
ć	                c-
dž	                dz=
đ	                d-
lj	                lj
nj	                nj
š	                s=
ž	                z=

예를 들어, ljes=njak은
크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고,
d와 ž가 분리된 것으로 보지 않는다.
lj와 nj도 마찬가지이다.
위 목록에 없는 알파벳은 한 글자씩 센다.


예제 1
ljes=njak   >>> 6
예제 2
ddz=z=      >>> 3
예제 3
nljj        >>> 3
예제 4
c=c=        >>> 2

"""

word = input()

croa_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croa_alpha:
    word = word.replace(i, "a")


print(len(word))





"""

word = input()
croa_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
list_a = []
word_index = []

for j in croa_alpha:
    a =word.split(j)
    if len(a)>1:
        list_a.append(a)
        
처음에는 크로아티아 문자로 스플릿을 사용해서 찾아낸 다음에 list에 append하고 
처음 인풋된 문자열에서 크로아티아 문자열을 빼려고 했는데
string은 뺄셈이 안되는 것 같다. 
그래서 문자열을 제거하는 방법을 찾아봤는데 replace()라는 함수가 있더라?
"""

"""
word = input()
croa_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
list_a =[]

for j in croa_alpha:
    a = word.find(j)
    if a > -1:
        list_a.append(a)
for i in croa_alpha:
    word = word.replace(i, "")

print(len(word) + len(list_a))

그래서 find로 크로아티아 문자열을 가지고 있는 경우를 찾아 list에 append 해주고 
그 length와  replace를 사용하여 문자열을 제거한 후에 남은 input문자열의 length를 
더해 찾아내려고 하였으나.

크로아티아 문자가 input된 문자열의 중간에 있을 경우에 제거되고 남은 문자열이
또다시 크로아티아 문자열이 될 경우가 존재할 수 있어 
내가 원하던 값과 다른 length가 리턴되었다...
또 이걸 어떻게 해결해야하나 고민하던 찰나.
아니 생각해보니까 replace는 그냥 다른 문자로 바꿔주는 역할이잖아?
그럼 임의의 1글자의 문자로 바꾸면 length는 똑같지 않나? 라는생각으로
마지막 코드에 도달!


"""








