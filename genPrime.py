# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:38:13 2021

@author: Bastien
"""

import math as m

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5) 
  f = 5
  
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def erathosthene(n):
    
    res = [True] * n
    res_p = []
    res[0] = False
    res[1] = False
    
    if n < 2:
        return []

    for i in range(2, n):      
        if res[i]:
            res_p.append(i)
            for j in range(i + i, n, i):
                res[j] = False
                
    return res_p

table =erathosthene(1000)
count = 0

for n in table:
    print(n)