'''Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt'''

try: 
    file_name = input("Enter file name: ")
    if len(file_name) == 0:
        file_content = open("mbox-short.txt")
    else: 
        file_content = open(file_name)
except:
    print("Invalid file name")
    quit()

count = 0
for line in file_content:
    words = line.split()
    if line.startswith("From") and not line.startswith("From:"):
        print(words[1])    
        count += 1

print("There were", count, "lines in the file with From as the first word")