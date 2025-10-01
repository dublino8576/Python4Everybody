'''Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''

#first open a connection to the file with open()
try:
    file_name = open(input("Enter file name to read it: "))
except:
    print("Sorry, invalid file name")
    quit()
#read the file in form of a sequence of strings with \n character separating each line, get rid of new line character to the right
read_file_name = file_name.read().rstrip()
file_upper = read_file_name.upper()
print(file_upper)