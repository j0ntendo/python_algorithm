
# def reverse(x):
#     res = 0
#     while x > 0:
#         t = x % 10         # Get the last digit of x
#         res = res * 10 + t # Add the last digit to the result in reverse order
#         x = x // 10        # Remove the last digit from x
#     return res

def reverse(x):
    x_str = str(x)
    if x_str[-1] == '0':
        return int(x_str[:-1][::-1])
    else:
        return int(x_str[::-1])

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False  # If x is divisible by any number, it's not prime
    return True  # If x is not divisible by any number, it's prime

n = int(input("how many numbers: "))
L = list(map(int, input("input list: ").split()))
for x in L:
    reversed_num = reverse(x)
    if isPrime(reversed_num):
        print(reversed_num, end=" ")





