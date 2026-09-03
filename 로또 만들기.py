# 로또 번호 추출기
# 1 ~ 45 중복없이 6개 2,3,15,20,34,40,16(15수정)
# 오름차순 정렬 2,3,16,20,34,40
# 1. 추첨하기 - 자동 추첨 (random)
# 2. 이력보기
# 3. 종료하기
# 2번을 누르게 되었을 때 최근 5개 순서대로 추출하기.
# 3번을 누르면 추첨 종료

# 추천 로또 번호 : 1 2 3 4 5 6
# # 과거 데이터를 추출한다.
# 추천된 과거 이력 (5개 - 없는 경우 '이력이 없습니다.')
# 1회 : 1 2 3 4 5 6
# 2회 : 2 3 4 5 6 7

# 자동/수동 선택
# 자동 - 6자리 자동추첨
# 수동 - 내가 입력하다가 나머지는 자동

import random

print("로또 자동 입력사이트에 오신 것을 환영합니다!")

while True:
    print("원하시는 번호를 눌러주세요! 1. 자동 번호 추출 / 2. 수동 번호 입력 / 3. 로그아웃")
    selectnum = int(input())

    # 메뉴를 선택할 때마다 로또 번호 초기화
    lotto = []

    if selectnum == 1:
        while len(lotto) < 6:
            num = random.randint(1, 45)

            if num not in lotto:
                lotto.append(num)

        lotto.sort()

        print("오늘의 추천 번호는 ", end="")

        for j in range(6):
            print(lotto[j], end=" ")

        print("입니다!")
        print()

    elif selectnum == 2:

        while len(lotto) < 6:
            print("포함하고 싶은 숫자를 입력해주세요!",end="")
            print(f"지금까지 {len(lotto)}개 입력하셨어요!")
            print("(나머지는 랜덤으로 돌리고 싶다면 0을 눌러주세요!)")

            ziknum = int(input())

            # 0 입력 → 나머지 랜덤
            if ziknum == 0:
                while len(lotto) < 6:
                    rannum = random.randint(1, 45)

                    if rannum not in lotto:
                        lotto.append(rannum)

                break

            # 1~45 사이의 숫자이고 중복이 아닐 경우
            elif 1 <= ziknum <= 45:
                if ziknum not in lotto:
                    lotto.append(ziknum)
                else:
                    print("이미 입력한 숫자입니다!")
                    print()

            # 1~45 범위를 벗어난 경우
            else:
                print("1부터 45까지의 숫자만 입력해주세요!")
                print()

        lotto.sort()

        print("오늘의 추천 번호는 ", end="")

        for j in range(6):
            print(lotto[j], end=" ")

        print("입니다!")
        print()

    elif selectnum == 3:
        print("로그아웃 합니다.")
        break

    else:
        print("잘못된 입력입니다!")