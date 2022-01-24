# Author: CMOB 1/24/2022

def summation(num):
    sum = 0
    x = 0
    while x <= num: #while x is less than original number
        sum += x # add each sequnceing number until x is greater than num i.e 1 + 2 + 3 ...
        x += 1
    return sum

print(summation(8) == 36)
print(summation(1) == 1)
print(summation(22) == 253)