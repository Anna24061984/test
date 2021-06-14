#!/usr/bin/env python
import random

a = int(input())
while True:
  b = random.randint(100000, 99999999)
  if b%a==0:
    break

print ("Random value is " + str(b));
