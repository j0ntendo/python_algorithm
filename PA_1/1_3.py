# this python program will,,,,

# input n(number of elements in a) and k(the position of the sums)
n, k = map(int, input("enter the # of numbers in the list + ").split())
# input the list of elements that i want to use
a = list(map(int, input().split()))
# use set() to only get different values not repeated
res = set()

# get the first digit of the sum ( iterates from start to end)
for i in range(n):
    # get the second digit of the sum( iterates from after the first digit to end)
    for j in range(i+1, n):
        # get the third digit of the sum ( iterated from after the second digit to end)
        for m in range(j+1, n):
            # add the sum to the list
            res.add(a[i]+a[j]+a[m])

# convert to list
res = list(res)
# sort it from descending order
res.sort(reverse=True)
# print the kth index that i wanted
print(res[k-1])



# function version
# def find_kth_sum(n, k, a):
#     res = set()
#
#     for i in range(n):
#         for j in range(i+1, n):
#             for m in range(j+1, n):
#                 res.add(a[i] + a[j] + a[m])
#
#     res = list(res)
#     res.sort(reverse=True)
#     return res[k-1]
#
# # Input from the user
# n, k = map(int, input("Enter the number of elements in the list and k: ").split())
# a = list(map(int, input("Enter the list of elements: ").split()))
#
# # Call the function and print the result
# result = find_kth_sum(n, k, a)
# print("The kth sum is:", result)
