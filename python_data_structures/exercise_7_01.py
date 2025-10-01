'''Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''

file_name = open("words.txt")
read_file_name = file_name.read()
file_upper = read_file_name.upper()
print(file_upper)