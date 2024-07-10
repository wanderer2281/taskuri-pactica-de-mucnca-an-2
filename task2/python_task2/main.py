import sys
nr =[0]
for i in range(1 , len(sys.argv)):
    print(sys.argv[i])
    
print(len(sys.argv))
print(sys.argv[1]) 
    
for i in range(1,len(sys.argv)):
    nr.append(0)
    
    #output-onlinefiletools.txt
with open(sys.argv[1]) as f:
    for line in f :
        words=line.split()
        for w in words:
            for j in range(2,len(sys.argv)):
                if sys.argv[j] in w:
                     nr[j] = nr[j] +1
                     
for i in range(2,len(sys.argv)) :        
    print("Cuvantul ",sys.argv[i],"apare de" , nr[i])
