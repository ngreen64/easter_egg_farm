#!/usr/bin/env python3.5
import random
import math
import sys
import uuid

if len(sys.argv) < 1:
    print("No arguments passed to script")
    sys.exit()

if len(sys.argv) < 2:
    print("Usage: script.py <lifetime> <upperlimitforprime>")
    sys.exit()

lifetime = int(sys.argv[1])
upperlimit = int(sys.argv[2])
eggname = uuid.uuid4()

def name_egg():
    eggname

def get_random():
    return random.randint(2,upperlimit)

while lifetime >= 1:
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
    print(name_egg)
    lifetime -= 1
