#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for put in my_list:
        average += put[0] * put[1]
        div += put[1]
    return float(average / div)
