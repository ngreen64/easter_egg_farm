#!/usr/bin/env python3.5
import random
import math
import sys
import uuid
from time import sleep
import signal

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)
    
  def exit_gracefully(self,signum, frame):
    self.kill_now = True

if len(sys.argv) < 2:
    print("No arguments passed to script, generating infinite eggs between 1 and 99,999,999,999")
    lifetime = -1
    upperlimit = 99999999999
else:
    lifetime = int(sys.argv[1])
    upperlimit = int(sys.argv[2])
    
def name_egg():
    return uuid.uuid4()

def get_random():
    return random.randint(2,upperlimit)

while lifetime >= 1 or lifetime < 0:
 killer = GracefulKiller()
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
    print('123')
    sleep(1.1)
    lifetime -= 1
    if killer.kill_now:
      break

print("Script exiting gracefully.")
