import hashlib
import sys
import os
import mimetypes
import typing



#clasa care verifica daca calea fisierului in care sunt cautate cuvinetele este valida
class FileManagement :
    def __init__(self,path: str) -> None:
        self.path = path
       
    
    def directory_valid(self) -> None:
        if os.path.exists(self.path): 
            print("the path:" , self.path , "exists") 
        else: 
            {print("error: Path", self.path , "does not exist") , sys.exit()}
        
        if os.listdir(self.path) == []:
            {print("error: No files found in the directory.") , sys.exit()}
        else:
            print("Some files found in the directory.")
        
     
       
       
    def file_valid(self, file: str) -> int:
        if mimetypes.guess_type(self.path+file)[0] == 'text/plain':
            return 1
        else:  
            return 0
        
               
   
                    

class FileReconfigure :  #clasa in care se configureaza hashingul fisierelor

    def hashing_file(dir , file):
        file_hash = hashlib.sha256()
        with open(dir + file, 'rb') as f: 
            fb = f.read(BLOCK_SIZE) 
            while len(fb) > 0: 
                file_hash.update(fb) 
                fb = f.read(BLOCK_SIZE) 
        file_hash_permanent.append(file_hash.hexdigest())
        print(file_hash.hexdigest())
        
    def write_hex_code_for_files(path ,hexa , counter: typing.Dict):
        with open(path, 'a') as out:
            out.write(hexa + ' ')
            for key in counter:
                out.write(str(counter[key]))
                out.write(' ')
                    
            out.write('\n')
   
    def write_hex_code_for_directory(path ,hexa , counter: typing.Dict):
        with open(path, 'a') as out:
            out.write('directory' + ' ')
            for key in counter:
                out.write(str(counter[key]))
                out.write(' ')
        
    
    def write_number_of_stings(path ,counter: typing.Dict):
        with open(path, 'a') as out:
                for key in counter:
                    out.write(str(counter[key]))
                    out.write(' ')
                    
                out.write('\n')
        
        
       
                
                
class  PatternSearch:  #metoda de cautare a stringurilor 
        
        def __init__(self,path: str,file :str,count_words: typing.List)-> None:
            self.path = path
            self.file = file
            self.count_words= count_words
            self.count_file = count_file
        
        
        def def_count_words(self,count: typing.Dict)-> None:
            self.count_words= list(count)
        

        
        
        def search(self, pattern: typing.List )-> None :
            
            
                with open(self.path+self.file) as f:
                    for line in f:
                        for pattern in self.count_words:
                            count[pattern] += line.count(pattern)
                            count_file[pattern] += line.count(pattern)   
                            
class ShowResults :  #metoda de afisare a rezultatelor

  

    def show(count: typing.Dict) -> None :
        for key in count:
            if(count[key] == 0):
                print(f"the word {key} doesn't appear ")
            elif(count[key] == 1):
                print(f"the word {key} appears one time")
            else:
                print(f"the word {key} appears {count[key]} times")
    def show_file(path, file_hash,count: typing.Dict, file):
        keys = list(count)
        with open(path) as s:
            for line in s:
                if file_hash in line:
                    print(f"In the file {sys.argv[1]+file} the words given as parameters appear the following amount of times")
                    words = line.split(' ')
                    for i in range(0,len(keys)):
                        print("The word " +keys[i]+" appears "+ words[i+1])
                if line.startswith('directory') and file_hash == file_hash_permanent[len(file_hash_permanent)-1]:
                    print(f"In the directory {sys.argv[1]}  the words given as parameters appear the following amount of times")
                    words = line.split(' ')
                    for i in range(0,len(keys)):
                        print("The word " +keys[i]+" appears "+ words[i+1])
   
directory = sys.argv[1]
files= os.listdir(directory)
BLOCK_SIZE = 65536 # The size of each read from the file
file_hash_permanent =[]
print(files)



my_file =FileManagement(sys.argv[1])
my_file.directory_valid() # verifica daca directorul curent este valid(exista)



count = {}
count_file = {}


for i in range(2,len(sys.argv)):
	count[sys.argv[i]] = 0
	count_file[sys.argv[i]] = 0
    

keys = list(count)
print(keys)
                    
        
        
file_code_in_file = False
       
for i in range(0,len(files)):
    FileReconfigure.hashing_file(directory,files[i])
    

    
    
for i in range(0,len(file_hash_permanent)): 


    
    filing = FileManagement(sys.argv[1])
    if ( filing.file_valid(files[i]) == 1) :    #verifica daca fisierul curent este de tip plain text
        print(f"the file {files[i]} is plain text")
        
    else:
        continue 
    for j in range(2,len(sys.argv)):
	    count_file[sys.argv[j]] = 0
  
    with open("/home/sebastian/Desktop/LinuxScripts/task5/hashing", 'r') as h:
        for line in h:
            if(file_hash_permanent[i] in line):
                file_code_in_file = True     #verifica daca hashul fisierului in care cauta stringuri-le se afla in fisierul hashing
                
    if(file_code_in_file == False):                                 # daca hashul fisierului nu se afla in fisierul hashing , Cauta numarul de stringuri prin metoda PatternSearch
        search = PatternSearch(sys.argv[1],files[i],[])             
        search.def_count_words(count)
        print(search.count_words)
        search.search(search.count_words)
        print(f"in the file {files[i]} the words given a parameters appear the following amount of times:")
        ShowResults.show(count_file)
        
                
        FileReconfigure.write_hex_code_for_files("/home/sebastian/Desktop/LinuxScripts/task5/hashing",file_hash_permanent[i],count_file)   
        FileReconfigure.write_number_of_stings("/home/sebastian/Desktop/LinuxScripts/task5/storage",count_file) 
        
        if(i == len(file_hash_permanent)-1):
             FileReconfigure.write_hex_code_for_directory("/home/sebastian/Desktop/LinuxScripts/task5/hashing",file_hash_permanent[i],count)   
             FileReconfigure.write_number_of_stings("/home/sebastian/Desktop/LinuxScripts/task5/storage",count) 
             print(f"In the directory {sys.argv[1]} the words given as parameters appear the following amount of times:")
             ShowResults.show(count) # afiseaza rezultatele pentru intregul

      
     
    else :                                                                                                          #daca hashul fisierului se afla in hashing , ia numarul de apariti de
        ShowResults.show_file("/home/sebastian/Desktop/LinuxScripts/task5/hashing",file_hash_permanent[i],count,files[i])# stringuri din aceasta metoda a clasei ShowResults
         
    file_code_in_file = False
    


