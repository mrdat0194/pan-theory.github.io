'''
finding goodness of a str with lowercase and number
'''
import re
import operator
from functools import reduce
str = "defGEfX2"
# print(re.findall(r'[a-z]+',str))
# print(re.findall(r'[0-9]+',str))
# [print(len(element)) for element in re.findall(r'[a-z]+',str)]

str_good_mul = reduce(operator.mul,(list(len(element) for element in re.findall(r'[a-z]+',str))),1)
str_good_min = sum(list(len(element) for element in re.findall(r'[0-9]+',str)))
result = str_good_mul - str_good_min
print(str_good_mul)
print(str_good_min)
print(result)


