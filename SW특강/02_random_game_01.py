'''
숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값(1~30)을 비교한다.
몇 번 만에 맞췄는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값이 랜덤 값 보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값이 랜덤 값 보다 작으면 숫자는 크다라고 한다.

사용자가 값을 입력하여 힌트를 받을 때 마다 count를 증가한다.

ex)
게임은 한 번만 한다.
게임은 0을 입력하면 종료한다.
게임은 사용자가 y를 입력하면 시작한다.
'''

# 알고리즘
# 1. 무한 반복
#   0) 게임을 할지 묻는다.
#   1) 게임을 하지 않으면
#       a. 프로그램 종료
#   2) 컴퓨터 랜덤 수 생성
#   3) 사용자로부터 정수 입력 받기
#   4) 입력받은 수와 컴퓨터 수가 같으면
#       a. 프로그램 종료
#
#   5) 컴퓨터 수가 크다면
#       a. 힌트
#   6) 사용자 수가 크다면
#       a. 힌트



import random

playAgain = 'y'

print("지금부터 숫자 추측 게임을 시작합니다.")
while playAgain == 'y':
    comNum = random.randint(1, 30)

    count = 1
    while True:
        guessNum = int(input("추측한 숫자를 입력하세요: "))        
        
        if comNum == guessNum:
            print("{}번 만에 맞추셨네요. 축하드립니다." .format(count)) 
            break
        
        elif comNum > guessNum:
            print("up")
        elif comNum < guessNum:
            print("down") 
        count += 1  # count = count + 1

    playAgain = input("게임을 다시 하시겠습니까?(y/n): ")