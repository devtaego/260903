# 리스트/딕셔너리/튜플/셋

nums = [1,2,3]                                           # 리스트 - 순서가 있음, 값을 수정 가능
point = (10, 20)                                         # 튜플 - 순서가 있음, 값 수정 불가능
person = {"name": "김병철", "age": 20, "point": point}    # 딕셔너리 - 이름(key):값(value) 저장
unique_nums = {1,2,3}                                    # 셋(set) - 중복 허용 X

# 리스트 (list)
nums = [10, 20, 30]
print(nums)
print(nums[2]) #30
nums[0] = 15
print(nums)

# 합치기/반복
a = [1,2]
b = [3,4]
print(a+b) # [1,2,3,4]
print(a*3) # 1 2 1 2 1 2

# 리스트 반복문
for i in nums :
    print(i)

# 리스트 슬라이싱
nums = [10,20,30,40,50]
print(nums[1:4])
print(nums[:4])
print(nums[::2])
print(nums[::-1])

nums = ["김병철", "김찬영", "이희창"]
print(nums[-1:]) # 최근 등록된 1인
print(nums[:-1])

# 메서드 - 리스트.메서드()
# 값 추가 - append()
nums = []
nums.append(90)
nums.append(99)
nums.append([10,20]) # extend
print(nums)

scores = [60,50]
passed_score = []
for score in scores:
    if score >= 60:
        passed_score.append(score)

# 원하는 위치 - insert()
nums = [10, 20, 40]

nums.insert(2, 30)

print(nums)

# 여러 값 추가 extend()
nums = [10,20]
nums2 = [30,40]
nums.extend(nums2)
print(nums)

# 값 삭제1
nums = [3, 40]
nums.remove(3)
print(nums)

# 값 삭제2
nums = [3, 40]
last = nums.pop(0)
print(last) # 임시 보관 데이터
print(nums)

# 값 삭제3
nums = [3, 40]
del nums[0]
print(nums)

# 값 삭제4
nums = [3, 40]
nums.clear()
print(len(nums))

# 개수(탐색) - count()
nums = [10,20,30,40]
print(nums.count(20))

# 위치 찾기(탐색)
nums = [10,20,20,40]
print(nums.index(40))

# 순서 정렬 - sort()
nums = [30,10,20]
nums.sort(reverse = False) # False 오름차순 / True 내림차순
print(nums)

nums.sort() # 오름차순 디폴트값
print(nums)

# reverse()
nums = [30,10,20]
nums.reverse()
print(nums)

# 포함 여부 확인 - in / not in - 멤버십 연산자
nums = [10, 20, 30]
print(20 in nums)


# 로또 번호 추출기
# 1 ~ 45 중복없이 6개 2,3,15,20,34,40,16(15수정)
# 오름차순 정렬 2,3,16,20,34,40
# 1. 추첨하기 - 자동 추첨 (random)
# 2. 이력보기
# 3. 종료하기
# 2번을 누르게 되었을 때 최근 5개 순서대로 추출하기.
# 3번을 누르면 추첨 종료

