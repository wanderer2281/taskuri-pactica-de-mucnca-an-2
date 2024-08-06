import numpy as np
import os
import sys
import random


directory = sys.argv[1]
file_type = sys.argv[2] 
number_of_files = int(sys.argv[3])
min_lines = int(sys.argv[4])
percentage_duplicates = int(sys.argv[5])
nr_duplicates = 0

def binToHexa(n):
    
    
    num = int(str(n), 2)
      
  
    hex_num = hex(num)
    return(hex_num)



# For the creation of in files
if (file_type == "in"):
    for i in range(1, number_of_files+1):
        file_template = (sys.argv[1]+"/file" + str(i)  + ".mat."  + file_type)
        
        j=0
        nr_duplicates = 0
        with open(file_template,'a') as f:
            there_are_dupes = False
            while (j < min_lines):
                string =""
                a= random.randint(1,64)
                b= random.randint(1,64)
                x=1
                y=1
                #f.write(str(a) + "X" + str(b) + ":")
                string = string + str(a) + "X" + str(b) +": "
                while(x<=a):
                    while(y<=b):
                        bit = random.randint(0,1)
                        #f.write(str(bit))
                        string = string + str(bit)
                        y += 1
                    x += 1
                    y = 1
                
                f.write(string)
                f.write('\n')
                #while (nr_duplicates < min_lines*percentage_duplicates/100):
                    #f.write(string)
                    #f.write('\n')
                    #nr_duplicates +=1
                #j = j + nr_duplicates
                j += 1
                if(there_are_dupes == False):
                    while ( nr_duplicates < int((min_lines*percentage_duplicates)/100)):
                        there_are_dupes = True
                        f.write(string)
                        f.write('\n')
                        nr_duplicates = nr_duplicates +1
                
                j = j+nr_duplicates
                nr_duplicates = 0
#For the creation of in.x files
elif (file_type == "in.x"):
    for i in range(1, number_of_files+1):
           file_template = (sys.argv[1]+"/file" + str(i)  + ".mat."  + file_type)
            
           j=0
           nr_duplicates = 0
           with open(file_template,'a') as f:
               there_are_dupes = False
               while (j < min_lines):
                   string =""
                   array_bits = np.array([])
                   a= random.randint(10,25)
                   b= random.randint(10,25)
                   x=1
                   y=1
                   #f.write(str(a) + "X" + str(b) + ":")
                   string = string + str(a) + "X" + str(b) +": "   
                   #f.write(string)
                   while(x<=a):
                       while(y<=b):
                           bit = random.randint(0,1)
                           array_bits = np.append(array_bits,bit)
                           y += 1
                       
                       x += 1
                       y = 1
                       
                   #for k in range(0, len(array_bits)):
                        #string = string + str(array_bits[k]) + f" [{k}] "
                   
                   
                   #string = string + "  ::: "
                  
                   k=0
                   l=0
                   while (k<len(array_bits)):    
                        dec_number = 0
                        tens = 1000
                        if(k+3 < len(array_bits)):
                            while (l< k+4):
                                dec_number = dec_number+ array_bits[l] *tens 
                                tens = tens/10
                                l += 1
                        else :
                            while (l< len(array_bits)):
                                 dec_number = dec_number + array_bits[l] *tens
                                 tens = tens/10
                                 l += 1
                        dec_number = int(dec_number)
                        hex_number = binToHexa(dec_number)
                        hex_digit  = hex_number[len(hex_number)-1]
                        if(hex_digit.isnumeric() == False):
                            hex_digit = hex_digit.upper()
                        #string = string + str(dec_number) +" ["+str(l)+ " ]   , " +"hex number"+str(hex_digit) + " , next number,   " 
                        string = string + str(hex_digit)  
                        k = k+4
                        
                              
                       
                       
                       
                   #string = string + str(array_bits)
                   f.write(string )
                   f.write('\n')
               
                
                   j += 1
                   
                   if(there_are_dupes == False):
                        while ( nr_duplicates < int((min_lines*percentage_duplicates)/100)):
                            there_are_dupes = True
                            f.write(string)
                            f.write('\n')
                            nr_duplicates = nr_duplicates +1
                
                   j = j+nr_duplicates
                   nr_duplicates = 0

    
