# this python algorithm will output the smallest digit in the list

def min_func(l):
    l = list(map(int, l.split()))
    min_val = float("inf")
    for x in l:
        if x < min_val:
            min_val = x

    return min_val

l = input("Input the list: ")
answer = min_func(l)
print(answer)

