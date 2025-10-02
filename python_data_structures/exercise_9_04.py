'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

try: 
    file_name = input("Enter file name: ")
    if len(file_name) == 0:
        file_content = open("mbox-short.txt")
    else: 
        handle = open(file_name)
except:
    print("Invalid file name")
    quit()

counts = dict()
for line in file_content:
    words = line.split()
    if line.startswith("From") and not line.startswith("From:"):
        contact = words[1]
        counts[contact] = counts.get(contact, 0) + 1 

biggest_recurrence = None
most_recurrent_word = None

for word, recurrence in counts.items():
    if biggest_recurrence is None or biggest_recurrence < recurrence:
        biggest_recurrence = recurrence
        most_recurrent_word = word
print(most_recurrent_word, biggest_recurrence)