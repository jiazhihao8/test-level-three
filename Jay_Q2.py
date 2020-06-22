# 2)Topic - Exception Handling    (5 marks)
# Fill in the blanks! What type of error will it throw?
# I am trying to open a text file named - file.txt and it is not present in the folder.
# Hint: you can use Reference.jpg that I uploaded on 25th May

try:  
       
    fileptr = open("file.txt","r")  
except FileNotFoundError:  
    print("We can not found that file ")  
else:  
    print("The file opened successfully")  
    fileptr.close()  
