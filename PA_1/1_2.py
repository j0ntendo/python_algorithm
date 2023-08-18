# this pythoh algorithm will....


T = int(input("How many Test Cases?: "))  # get the number of test cases
for t in range(1, T+1):
    n, s, e, k = map(int, input().split())  # separate the first line of the test case
    List = list(map(int, input().split())) # get the second line of the test case
    # get the middle part of the list
    middle = List[s-1:e]
    middle.sort()

    smallest = middle[k-1]

    print("#%d, %d" % (t, smallest))
