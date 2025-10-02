''' Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

try: 
    file_name = input("Enter file name: ")
    if len(file_name) == 0:
        handle = open("mbox-short.txt")
    else: 
        handle = open(file_name)
except:
    print("Invalid file name")
    quit()
counts = dict()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        time = words[5].split(":")
        time_by_hrs = time[0]
        #get() takes value of this key, but in the first iteration it has no value yet, so it goes default to 0 and here we add 1 so we create a histogram object with minimum frequency for each key of 1 
        counts[time_by_hrs] = counts.get(time_by_hrs, 0) + 1
        
#make it into a list of tuples so that the pairs can be sorted
#this method is called LIST COMPREHENSION
sorted_list = [(key,value) for key,value in counts.items()] 
#.items() is still an object made up of a list, so we have to make it a list that wraps around tuples
# THIS IS CALLED VIEW OBJECT WHICH BEHAVES LIKE A LIST BUT CANNOT BE SORTED 
sorted_list.sort()    
for tuple in sorted_list:
    print(tuple[0], tuple[1])

    
