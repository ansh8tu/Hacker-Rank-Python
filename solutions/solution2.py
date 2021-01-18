#!/bin/python3

import math
import os
import random
import re
import sys

number = int(input())

if (number%2) != 0:
    print('Weird')
elif (number%2) == 0:
    if number >= 2 and number <=5:
        print('Not Weird')
    elif number>=6 and number<=20:
        print('Weird')
    elif number>20:
        print('Not Weird')
