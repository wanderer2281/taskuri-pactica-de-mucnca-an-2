import os
import sys
import mimetypes
import typing

#verifica daca calea fisierului in care sunt cautate cuvinetele este valida
class file_management :
    def __init__(self,path:str)-> None:
        self.path = path
    def file_valid(self)-> None:
        if os.path.exists(self.path) : print("the path:",self.path,"exists") 
        else : {print("error: Path",self.path,"does not exist") , sys.exit()}
        
        if os.path.isdir(self.path): 
            print("the path leads to a directory")
        else: print("the path leads to a file")
        
        if os.path.isdir(self.path) and mimetypes.guess_type(self.path)[0] != 'text/plain' : 
                { print("error: Path",self.path,"is not valid"),sys.exit() }
        else : 
                print("the path:",self.path,"is valid")
       
        
        
    
    def file_type(self)-> None:
        if mimetypes.guess_type(self.path)[0] == 'text/plain':
               print("the file is plain text")
        else : print("the file is not plain text")
               
   
                    
#cauta cuvintele date ca parametrii              
class  pattern_search:
        
        def __init__(self,path:str,count_words:typing.List)-> None:
            self.path = path
            self.count_words= count_words
        
        
        def def_count_words(self,count:typing.Dict)-> None:
            self.count_words= list(count)
            
            
            
        
        def search(self, pattern:typing.List)-> None :
               with open(self.path) as f:
                    for line in f:
                        for pattern in self.count_words:
                            count[pattern] += line.count(pattern)

# afiseaza rezultatele
class show_results :
    def show(count:typing.Dict) -> None :
        
        for key in count:
            print("the word" ,end=' ')
            print (key,' appears ' ,end=' ')
            print(count[key]," times in the text file")

        print(count)
      

count={}
for i in range(2,len(sys.argv)):
	count[sys.argv[i]] = 0




print("It works")

my_file =file_management(sys.argv[1])
my_file.file_valid()
my_file.file_type()
print("It works")

search = pattern_search(sys.argv[1],[])
search.def_count_words(count)
print(search.count_words)
search.search(search.count_words)

showing = show_results
showing.show(count)

