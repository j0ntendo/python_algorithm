# XO algorithm

L = map(int, input("How many questions?: "))
n = map(int, input().split())
score = 0
count = 0

for num in n:
    if num == 1:
        count += 1
        score += num*count

    elif num == 0:
        count = 0


print(score)



