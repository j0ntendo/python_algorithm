# this python algorithm will get the average of the grades,
# get every combination sum of three grades and then output the
# position of the grade thats closest to the average




T = int(input()) # get the number of students
grades = list(map(int, input().split())) # get the list of grades

# calculate the average
avg = round(sum(grades)/T)
# get a min_val
min_val = float("inf")

# get the position of the closest score to the average

for pos, x in enumerate(grades):  # iterate through the grade and its position
    diff = abs(x - avg)  # calc diff
    if diff < min_val:  # chk if diff is less than the min_val
        min_val = diff  # set the diff val to the min_val
        score = x  # create score variable
        res = pos + 1 # create result variable
    elif diff == min_val:  # for when there is duplicate grades(people with same score)
        if x > score:  # chk if grade is greater than score
            score = x  # set grade to score
            res = pos + 1  # set the result

print(avg, res)


