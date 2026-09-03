# for row in range(1,4):
#     for col in range(1,4):
#         print(f"row : {row}, col : {col}")
#
# row = 1
# while row <= 3:
#     col = 1
#
#     while col <= 3:
#         print(f"row : {row}, col : {col}")
#         col += 1
#     row += 1

# 실습 for문 두개를 사용해서 구구단 만들기
# input을 사용해서 2단을 출력하고 싶다.
# 2라고 입력하면 2단 출력

print("구구단 몇단을 출력할까요? (2단 ~ 9단 전체 출력을 원하시면 1을 눌러주세요)")

dan = int(input())
while(True):
    if (dan>=2 and dan<=9):
        print(f"****** {dan}단 ******")
        print()
        for i in range(1,10):
            print(f"{dan} x {i} = ",end="")
            print(dan*i)
        print()
        break

    elif (dan == 1):
        print("2단 ~ 9단 전체 출력합니다.")
        print()
        for i in range(2,10):
            print(f"****** {i}단 ******")
            print()
            for j in range(1,10):
                print(f"{i} * {j} = ",end="")
                print(i*j)
            print()
        break

    else :
        print("2 ~ 9 사이의 정수를 다시 입력해주세요!")
        break




















# 아 팬 제 묵 린