#Two types of functions: -Built in modules
#                        -External modules
import math #math is module name
# import os
# os.abort() 
import _my_module
print(math.sqrt(25))

_my_module.hello()

#now for external modules lets take requests modules for example
#In terminal  pip install requests
#  then we can do
import requests
r = requests.get("https://www.google.com")
print(r.text)

# pip install pandas
import pandas as pd