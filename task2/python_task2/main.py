print("n=")
n= input()
n = int(n)
string=[]
nr=[0]
for i in range(0,n):
    nr.append(0)
    
i=0
for i in range(0,n):
    cuvant = input("Input cuvant: ")
    string.append(cuvant)
   

with open("output-onlinefiletools.txt","r") as f:
    for line in f :
        words=line.split()
        for w in words:
            for j in range(0,n):
                if string[j] in w:
                    nr[j] = nr[j] +1
for i in range(0,n) :        
    print("Cuvantul ",string[i],"apare de" , nr[i])

         
