# this python algorithm will output
# the amount of prime numbers from 1 to the input

# Sieve of Eratosthenes algorithm
num = int(input("input the num: "))

# create count list
ch = [0]*(num+1)
count = 0

for i in range(2, num+1):
    if ch[i] == 0:
        count += 1
        for j in range(i, num+1, i):
            ch[j] = 1

print(count)


