# 자료구조
# 기존 방식
# score1 = 90
# score2 = 80
# score3 = 85
# print(score1)
# print(score2)
# print(score3)

scores = [90, 85, 64, 68, 72]

for score in scores:
    print(score,end=" ")
print()

pass_count = 0
for count in scores:
    if count >= 60:
        pass_count += 1
print(f"합격자 수는 {pass_count}명 입니다.!")


print(scores)

# 평균 점수 구하기 - 5명 넣고,
# 5명의 평균 구하기
# 합격자 중에서 평균
total = 0

for i in range(len(scores)):
    total += scores[i]

avg = total / len(scores)
print(round(avg))


# 2차원 리스트
[1,2,3,4,5,6]           # 1차원 0 1 2 3 4 5
[1,2,3,4,[1,2,3,4]]     # 2차원 리스트
# 0 1 2 3 4
print(nums[4][1])

nums = [1,2,3]
new_nums = list(nums)

nums = [1,2,3]
new_nums = nums

# 값 초기화
clear() = 초기화       # 클리어 사용시 (얕은 복사)
# 값을 새로 복사
copy()