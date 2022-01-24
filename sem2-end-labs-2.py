# Author: CMOB 1/24/2022

def better_than_average(class_points, your_points):
    
    class_total = 0
    # for each value in the list, add it all to the class total
    for index, value in enumerate(class_points):
        class_total += value
    # finds the average of the total divided by the amount of elements in the list    
    average = class_total / len(class_points)
    # if the average is less than the points, respond True, if it is greater, respond False
    if average <= your_points:
        return True
    else:
        return False
    
print(better_than_average([2,3,4], 5) == True)
print(better_than_average([5,6,9], 5) == False)
print(better_than_average([9,9,9], 10) == True)