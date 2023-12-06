import math
import time
import random
import numpy as np

def find_odd_sq(num):
    if num%2!=0:
        res = num**2
    else:
        res = None
    return res

def countdown(n):
    if n<=0:
        print('We have lift off!!')
    else:
        print(n)
        countdown(n-1)

### running ###
n=10
print(countdown(n))


### while loop ###
def countdownwithwhile(n):
    while n>0:
        print(n)
        n=n-1

    print('We have lift off!!')

print(countdownwithwhile(n))


#### list append ###
sqr_list = []
zero2nine = range(10)
for el in zero2nine:
    sqr_list.append(el**2)

print(sqr_list)
print([el**2+5 for el in zero2nine if el%2==0])


### Dictionary ####
listlen = 1000000
list_of_numbers = [0]*listlen
dict_of_numbers = {}
for i in range(listlen):
    n = random.randint(100, 999)
    list_of_numbers[i]=n
    dict_of_numbers[n] = 1

print(len(list_of_numbers))
print(len(dict_of_numbers))
