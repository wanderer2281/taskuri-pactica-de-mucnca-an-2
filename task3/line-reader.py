import sys
import os
import magic
nr =[]
string = []
for i in range(1 , len(sys.argv)):
    if i==1 :
        my_file= sys.argv[i]  #the path to the file
    else : {string.append(sys.argv[i]) ,nr.append(0)}            
if os.path.exists(my_file) : print("the path:",my_file,"exists") 
else : {print("error: Path",my_file,"does not exist") , sys.exit()}
if os.path.isdir(my_file) or magic.from_file(my_file)!="ASCII text": { print("error: Path",my_file,"is not valid"),sys.exit() }
else : print("the path:",my_file,"is valid")
print(magic.from_file(my_file)) 
#if magic.from_file(my_file)=="ASCII text" : print("This file is a text document")
#else:{ print("error: Path",my_file,"is not valid since it is not a text document"),sys.exit() }
if len(string) == 0: { print("error: no parameters have been entered") , sys.exit()}
print(len(sys.argv))
print(my_file) 
for i in range(0,len(string)):
    print(string[i])
    print(i)
print(len(string))
    
    
    
with open(my_file) as f:
    for line in f :
        words=line.split()
        for w in words:
            for j in range(0,len(string)):
                if string[j] in w:
                     nr[j] = nr[j] +1
                     
for i in range(0,len(string)) :        
    print("The Word",string[i],"apears" , nr[i],"times")
