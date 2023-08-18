# this algorithm will output the most common numbers
# when throwing n and m hedron dices.

# receive input
n, m = map(int, input("input two dices(4,6,8,12,20): ").split())

# make a count list
cnt = [0]*(n+m+1)

# create table for n and m
for ver in range(1,n+1):
    for hor in range(1, m+1):
        cnt[ver+hor] += 1

# get the greatest
most = 0
for i in range(2, n+m+1):
    if cnt[i] > most:
        most = cnt[i]
# print the common ones
for i in range(2, n+m+1):
    if cnt[i] == most:
        print(i, end=" ")

