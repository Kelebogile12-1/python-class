#A module is basically a file containing a set of function to include in your application.
# Core Module 
#date.time 

import datetime 
import math 

#PIP modules 
import camelcase
import numpy as np


today = datetime.date.today()
month = datetime .date.today().month
day = datetime.date.today().day
time = datetime.datetime.now().time()
print(today)
print(month)
print(day)
print(time)
print(math.sqrt(25))
print(math.sqrt(9))
print(math.sqrt(64))
print(math.pi)

#PIP is an installer package and manage external module or libraries are not built in python .
c=camelcase.CamelCase()
text="hello world"
print(c.hump(text))



