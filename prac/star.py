'''
입력받은 정수 구구단
'''


# gugudan = int(input("정수를 입력하세요 : "))

# print ('구구단',gugudan ,'단')
# print('--------------')
#
# for i in range(1,10):
#     print(gugudan,'x',i ,'=' ,gugudan*i)



'''
별찍기 1 
*
**
***
****
*****
'''
# star1 = int(input('정수를 입력하세요 : '))
#
# for i in range(1,star1+1 ):
#     for j in range(i):
#         print('*',end=",")
#     print("")

'''
별찍기 2   
    *
   **
  ***
 ****
*****
'''

star2 = int(input('정수를 입력하세요 : '))

for i in range(star2+1):
    for j in range(i):
        if i >j:
            print(' ',end='')
    print('*')