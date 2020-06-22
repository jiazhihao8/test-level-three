# 1)Topic - File Operators in python  (10 marks)
# Write a program to print the lines of a text file in
# reverse order. Text file is File2.txt
# The text file - File2.txt has been attached
file=open("/Users/apple/Desktop/test level 3/File2.txt","a+")
a=file.read()
a=a[::-1]
file.write(a)
file.close()
