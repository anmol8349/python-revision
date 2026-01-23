import os

# Mode	     Meaning
# "r"	      Read (file must exist)
# "w"	      Write (creates new file / overwrites existing)
# "a"	      Append (adds data at end)
# "x"         Create (error if file exists)
# "b"      	  Binary mode (images, pdf, etc.)
# "t"      	 Text mode (default)
# "r+"      	Read + Write
# "w+"	      Write + Read (overwrites)
# "a+"      	Append + Read

# writing and creating
# f = open('demo.txt','w')
# f.write("Hello Anmol\n")
# f.write("welcome")
# f.close()


# ----------------------------


# reading from file

# f=open("demo.txt","r")
# content=f.read()  #read full file 
# print(content) 



# ------------------------

# read line by line

# for line in f:
#     print(line.strip())
# f.close()

# -------------------------


# -----  Using with (Auto Close)

# with open("demo.txt","r" ) as f:
    # data=f.read() # entire file
    # print(data)
    # print(f.readline())  #one line
    
    # lines = f.readlines()  # List of lines
    # print(lines)
    


# ------------append and seek and tell


# with open("demo.txt", "a") as f:
#     f.write(" New line added!\n")
    
    
# with open("demo.txt", "r") as f:
#     print(f.tell())   # Current position
#     f.seek(5)         # Move pointer   f.seek(offset, whence)  0 = from start 1=from current 2 from end

#     print(f.read())
#     print (f.tell())



# --------  binary files

with open("rj.jpg", "rb") as f:
    data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(data)


