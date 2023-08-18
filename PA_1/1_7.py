# this algorithim function will output the digit
# that's the greatest when you sum the digits?

def digit_sum(x):
    # create a list with the input
    L = list(map(int,input("input list: ").split()))

    # init variables
    max_sum = 0
    max_num = 0

    # iterate thorugh list
    for num in L:
        # sum the digit
        summ = sum(map(int,str(num)))
        # chk if the sum is greater than the max sum/num
        if summ > max_sum:
            max_sum = summ
            max_num = num

    return max_num


# test code
x = int(input("How many numbers?: "))
result = digit_sum(x)
print("The digit with the greatest digit sum is:", result)


