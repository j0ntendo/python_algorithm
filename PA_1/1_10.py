# dice game

L = int(input("How many players?: "))
result = 0
for i in range(L):
    n = input().split()
    n.sort()
    a,b,c = map(int, n)
    if a == b and b == c:
        res = 10000+(a*1000)
    elif a == b or a == c:
        res = 1000+(a*100)
    elif b == c:
        res = 1000 + (b * 100)
    else:
        res = c*100

    if res > result:
        result = res

print(result)






