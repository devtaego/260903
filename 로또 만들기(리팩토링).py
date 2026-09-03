import random

history = []
count = 0


def make_random_lotto(lotto):
    while len(lotto) < 6:
        num = random.randint(1, 45)

        if num not in lotto:
            lotto.append(num)


def print_lotto(lotto):
    lotto.sort()

    print("오늘의 추천 번호는 ", end="")

    for num in lotto:
        print(num, end=" ")

    print("입니다!")
    print()


def save_lotto(lotto):
    global count

    count += 1
    history.append(lotto.copy())


print("로또 자동 입력사이트에 오신 것을 환영합니다!")

while True:

    print("원하시는 번호를 눌러주세요!")
    print("1. 자동 번호 추출 / 2. 수동 번호 입력 / 3. 이력보기 / 4. 로그아웃")

    selectnum = int(input())

    lotto = []

    # 자동 번호
    if selectnum == 1:

        make_random_lotto(lotto)

        print_lotto(lotto)
        save_lotto(lotto)

    # 수동 번호
    elif selectnum == 2:

        while len(lotto) < 6:

            print("포함하고 싶은 숫자를 입력해주세요!", end="")
            print(f" 지금까지 {len(lotto)}개 입력하셨어요!")
            print("(나머지는 랜덤으로 돌리고 싶다면 0을 눌러주세요!)")

            num = int(input())

            if num == 0:
                make_random_lotto(lotto)
                break

            elif 1 <= num <= 45:

                if num not in lotto:
                    lotto.append(num)

                else:
                    print("이미 입력한 숫자입니다!")
                    print()

            else:
                print("1부터 45까지의 숫자만 입력해주세요!")
                print()

        print_lotto(lotto)
        save_lotto(lotto)

    # 이력 보기
    elif selectnum == 3:

        if len(history) == 0:
            print("아직 회차 정보가 없습니다!")

        else:
            for i in range(len(history)):
                print(f"{i + 1} 회차 추천번호는 : {history[i]} 입니다!")

            print()

    # 종료
    elif selectnum == 4:

        print("로그아웃 합니다.")
        break

    else:
        print("잘못된 입력입니다!")