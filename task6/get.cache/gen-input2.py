import numpy as np
import os
import sys
import random


directory = sys.argv[1]
file_type = sys.argv[2] 
number_of_files = int(sys.argv[3])
min_lines = int(sys.argv[4])
percentage_duplicates = int(sys.argv[5])
#caching_mechanism = sys.argv[6]

nr_duplicates = 0
nr_lines = random.randint(min_lines,min_lines+10)

percentage_duplicates = random.randint(int((nr_lines*percentage_duplicates)/100),int((nr_lines*percentage_duplicates)/100)+4 )

#defining the cache 
cache = True
caching_mechanism =""
print(len(sys.argv))
if (len(sys.argv)==7):
    caching_mechanism = sys.argv[6]

if(caching_mechanism =="nocache"):
    cache = False    
ok =0




def binToHexa(n):
    
    
    num = int(str(n), 2)
      
  
    hex_num = hex(num)
    return(hex_num)


print(nr_lines)
print(percentage_duplicates)
# For the creation of in files
if (file_type == "in"):
    for i in range(1, number_of_files+1):
        file_template = (sys.argv[1]+"/file" + str(i)  + ".mat."  + file_type)
        
        j=0
        nr_duplicates = 0
        there_are_dupes = False
        
        if cache == True:
            ok = 1
        
        with open(file_template,'a') as f:
            string = ""
            
            #start of the caching mechanism for in files
            if(ok ==1):
                while ( nr_duplicates < percentage_duplicates and j<nr_lines):
                    with open("cache.in",'r') as cache:
                            for line in cache:
                                string = str(line)
                                f.write(string)
                                j += 1
                                nr_duplicates +=1
                    cache.close()
                    
                there_are_dupes = True
             #end of the caching mechanism  
            
            
            while (j < nr_lines):
                nr_duplicates = 0
                string =""
                a= random.randrange(4,17,4)
                b= random.randrange(4,17,4)
                x=1
                y=1
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
                
                j += 1
               
                if(there_are_dupes == False):
                    while ( nr_duplicates < percentage_duplicates and j<nr_lines):
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
           there_are_dupes = False
           if cache == True:
                ok = 1
        
           
           with open(file_template,'a') as f:
               string = ""
               
               #start of the caching mechanism for in.x files
               if(ok == 1):
                    while ( nr_duplicates < percentage_duplicates and j<nr_lines):
                         with open("cache.in.x",'r') as cache:
                                for line in cache:
                                    string = str(line)
                                    f.write(string)
                                    j += 1
                                    nr_duplicates +=1
                         cache.close()
                    
                    there_are_dupes = True
               nr_duplicates = 0
               # end of the caching mechanism
               
               while (j < nr_lines):
                   string =""
                   array_bits = np.array([])
                   a= random.randrange(4,17,4)
                   b= random.randrange(4,17,4)
                   x=1
                   y=1
                 
                   string = string + str(a) + "X" + str(b) +": "   
                
                   while(x<=a):
                       while(y<=b):
                           bit = random.randint(0,1)
                           array_bits = np.append(array_bits,bit)
                           y += 1
                       
                       x += 1
                       y = 1
                       
                
                  
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
                        while ( nr_duplicates < percentage_duplicates and j<nr_lines):
                            there_are_dupes = True
                            f.write(string)
                            f.write('\n')
                            nr_duplicates = nr_duplicates +1
                
                   j = j+nr_duplicates
                   nr_duplicates = 0


    
