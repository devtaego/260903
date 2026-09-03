# 별찍기2 (이중 for문)

print("몇 줄 별 만드실건가요?")
j = int(input())

for i in range(j):          # 층
    for n in range(i + 1):  # 별 개수
        print("*", end="")
    print()

print("몇 줄 역별 만드실건가요?")
l = int(input())
for k in range(l,0,-1):             # 층(줄) : n, n-1
    for m in range (l-k):
        print(" " ,end="")
    # print(" " * (l - k),end="")     # 공백 개수
    for j in range(k):
        print("*", end="")          # 별 개수
    print()

print("몇 줄 피라미드 만드실건가요?")
m = int(input())
for i in range(1,m+1):
    # for n in range(m-1,-1,-1): # 잘못 생각했던 부분 이렇게 되면 결국 m-1~0 즉 (m - 1) - 0 + 1 = m번 공백 반복
    for n in range(m-i):
        print(" " ,end="")
    print("*"*(2*i-1))

