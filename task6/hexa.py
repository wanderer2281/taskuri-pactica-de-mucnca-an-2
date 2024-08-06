import numpy as np
import os
import sys
import random


def binToHexa(n):
    
    
    num = int(str(n), 2)
      
  
    hex_num = hex(num)
    return(hex_num)
    
    
    
h = binToHexa(1111)
print(h)
#for i in range(0,len(h)):
    #print(h[i])

print(h[len(h)-1])

f = h[len(h)-1]

if(f.isnumeric()) :
    print(f)
else:
    f = f.upper()
print(f)
    
