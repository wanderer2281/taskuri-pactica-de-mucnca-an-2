import hashlib
import sys
import os

directory = sys.argv[1]
files= os.listdir(directory)
BLOCK_SIZE = 65536 # The size of each read from the file
file_hash_permanent =[]
print(files)

class FileReconfigure :

    def hashing_file(dir , file):
        file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(dir + file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        file_hash_permanent.append(file_hash.hexdigest())
        print(file_hash.hexdigest())
        
    def write_hex_code(path ,hexa):
        with open(path, 'a') as out:
                out.write(hexa+ '\n')
                
    
        
        
file_code_in_file = False
       
for i in range(0,len(files)):
    FileReconfigure.hashing_file(directory,files[i])
    
for i in range(0,len(file_hash_permanent)):   
    with open("/home/sebastian/Desktop/LinuxScripts/task5/hashing", 'r') as h:
        for line in h:
            if(file_hash_permanent[i] in line):
                file_code_in_file = True
                
    if(file_code_in_file == False):
        FileReconfigure.write_hex_code("/home/sebastian/Desktop/LinuxScripts/task5/hashing",file_hash_permanent[i])          

    file_code_in_file = False

