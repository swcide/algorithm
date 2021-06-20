"""
문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” ,
그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

"""

"""
예제 1                          출력
6
(())())                         NO
(((()())()                      NO
(()())((()))                    YES
((()()(()))(((())))()           NO
()()()()(()()())()              YES
(()((())()(                     NO


예제 2                          출력

3
((                              NO
))                              NO
())(()                          NO


먼저 괄호를 받았을 때
( 라면 stack에 append 해준다.
그뒤에 )가 나오면 pop을 해준다.
매우 간단하다.
입력받은 문자열의 length로 for문을 돌린 뒤
문자열의 인덱스가 "("면  stack에 append해준다.
else일 경우엔 ")" 이므로
if stack: 으로 조건을 건뒤(스택의 값이 널이아닐때)
stack에 있는 값을 pop해준다. 
else의 경우에는 stack의 값이 널이라는 의미이므로 print("NO")를 출력

밑의 else문도 동일하다.
"""

import sys

# input = sys.stdin.readline

n = int(input())

for _ in range(n):
    Bracket = input()
    stack = []
    for i in range(len(Bracket)):
        if Bracket[i] =="(":
            stack.append(Bracket[i])
        else :
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")




