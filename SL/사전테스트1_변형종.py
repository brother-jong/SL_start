# 어린이, 보통, 경로, 총 가격
child = 5000
adult = 10000
senior = 7000

# 인원 받기
child_people = int(input("어린이 인원 수를 입력해주세요: "))
adult_people = int(input("보통 인원 수를 입력해주세요: "))
senior_people = int(input("경로 인원 수를 입력해주세요: "))
total_people = child + adult + senior

if total_people >= 10:
    total = ((child_people*child)+(adult_people*adult)+(senior_people*senior))*(0.8)
    print("어린이{}명, 보통{}명, 경로{}명입니다. 총 가격은{}원입니다." .format(child_people, adult_people, senior_people, total))
else :
    total = (child_people*child)+(adult_people*adult)+(senior_people*senior)
    print("어린이{}명, 보통{}명, 경로{}명입니다. 총 가격은{}원입니다." .format(child_people, adult_people, senior_people, total))

if child_people < 13:
    
elif adult_people <= 13:
    
else :
    
# 모르게써요..