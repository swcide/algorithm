"""
문제
세계는 균형이 잘 잡혀있어야 한다.
양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때,
괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고,
문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉,
괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.


"""

"""
예제 입력 1 
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

예제 출력 1 
yes
yes
no
no
no
yes
yes
"""

"""
TRY 1


"""
while True:
    commend = input()
    stack = []
    if commend == ".":
        break
    for i in commend:
        if i == '(' or i == "[":
            stack.append(i)
        elif i == ')':
            if stack :
                if stack[-1] == "(":
                    stack.pop()
                    print(stack)
            else:
                print("no")
                break
        elif i == ']':
            if stack :
                if stack[-1] == "[":
                    stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")


"""
TRY 2

# while True:
#     commend = input()
#     stack = []
#     if commend == ".":
#         break
#     for i in commend:
#         if i == '(' or i == "[":
#             stack.append(i)
#         elif i == ')':
#             if len(stack) >= 1:
#                 if stack[-1] == "(":
#                     stack.pop()
#                 else:                                #이곳이 추가 됨 .
#                     print("no")
#                     break
#             else:
#                 print("no")
#                 break
#         elif i == ']':
#             if len(stack) >= 1:
#                 if stack[-1] == "[":
#                     stack.pop()
#                 else:
#                     print("no")
#                     break
#             else:
#                 print("no")
#                 break
#     else:
#         if stack:
#             print("no")
#         else:
#             print("yes")
"""

#
# while True:
#     commend = input()
#     stack = []
#     if commend == ".":
#         break
#     for i in commend:
#         if i == '(' or i == "[":
#             stack.append(i)
#         elif i == ')':
#             if len(stack) >=1 and stack[-1] == "(" :
#                 stack.pop()
#             else:
#                 print("no")
#                 break
#         elif i == ']':
#             if len(stack) >=1 and stack[-1] == "[" :
#                 stack.pop()
#             else:
#                 print("no")
#                 break
#     else:
#         if stack:
#             print("no")
#         else:
#             print("yes")


"""
백준 1934 괄호와 같은 문제라고 생각했는데 조건이 더 다양했다.
백준 1934 () 만 보면 됐지만
균형잡힌 세상은 []이 있기 때문에 조건을 두개로 나눠야했다.

elif i == ')':
    if stack :
        if stack[-1] == "(":
            stack.pop()
    else:
        print("no")
        break
elif i == ']':
    if len(stack) >= 1:
        if stack[-1] == "[":
            stack.pop()
    else:
        print("no")
        break

테스트케이스는 통과 됐지만 백준에서 계속 오류가 났다.
(반례를 찾을 수 없었는데 팀장이신 '김연우'님께서 찾아주셨다.. (]) 였다! )

이유를 찾을 수 없어 다른 사람들에게 도움을 구했고 드디어 해결 했다!

원인은 
if stack :
    if stack[-1] == "(":
        stack.pop()
else:
    print("no")
    break

if stack[-1] =="(":
밑에도 else를 추가해줘야했다.

"""