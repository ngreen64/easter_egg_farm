#!/usr/bin/env python3.5
import random
import math
import sys
import uuid

if len(sys.argv) < 2:
    print("No arguments passed to script, generating infinite eggs between 1 and 100,000,000,000")
    lifetime = -1
    upperlimit = 10000000000
else:
    lifetime = int(sys.argv[1])
    upperlimit = int(sys.argv[2])
    
def name_egg():
    return uuid.uuid4()

def get_random():
    return random.randint(2,upperlimit)

while lifetime >= 1 or lifetime < 0:
 number = get_random()
 root = round(math.sqrt(number))
 prime = "yes"
 X = 2
 while X <= root:
     if number % X == 0:
         prime = "no"
         break
     else:
         X = X + 1
 if prime == "yes":
    print(str(number))
    print(name_egg())
    lifetime -= 1
