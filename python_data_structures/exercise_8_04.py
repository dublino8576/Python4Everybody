'''Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt'''

try:
    file_name = input("Enter file name: ")
except:
    print("Invalid file name")
    quit()
lst = list()
file_content = open(file_name)
#read line by line with for loop and not read function
#create list to append words to
for line in file_content:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
#sort() in Python mutates in place does not create a copy and returns NONE as it has the same reference in memory
# sorted() creates a copy instead if you want to name a new variable      
print(lst)