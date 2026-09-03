# 별찍기2 (이중 for문)

print("몇 줄 별 만드실건가요?")
j = int(input())
for i in range(0, j):
    print("*"*(i+1))

print("몇 줄 역별 만드실건가요?")
l = int(input())
for k in range(l,0,-1):
    print(" " * (l - k),end="")
    print("*"*k)