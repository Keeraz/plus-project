# -*- coding: utf-8 -*-
"""plus.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tONigHfiX8QPxMigU-au2HaOy9jS_cY5
"""

with open("/content/input.txt",'r') as k:
  input_file = k.read()

input_file

input = input_file.split("\n")

import re

find = re.findall("\d",input[0])

find

number = []
for i in input:
  find = re.findall("\d",i)
  number.append(find)
  print(find)

# a = int(number[0][0])
# b = int(number[0][-1])
# c = a + b
# print(a)
# print(b)
# print(c)

ans = []
for i in number:
  a = int(i[0])
  b = int(i[-1])
  c = a + b
  ans.append(c)
  print(f"{a}+{b}={c}")

ans
