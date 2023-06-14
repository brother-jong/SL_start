'''
리스트를 만들고, 반복문으로 출력하시오.
'''
import random
num1 = list(range(1, 10))
print("num1: ", num1)

for i in num1:
    print(i, end=', ')
    
'''
1~100 사이의 정수 중 랜덤으로 10개의 수를 뽑아서 리스트(num2)에 저장하시오.
'''
print()

num2 = [] # 빈리스트 생성
for i in range(10):
    num2.append(random.randint(1,100)) #append 기억
print("생성된 리스트: ", num2)