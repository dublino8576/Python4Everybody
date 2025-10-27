#JSON DATA PARSING

'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2303397.json (Sum ends with 71)
'''
import urllib.request, json

url = input("Enter URL: ")

json_file = urllib.request.urlopen(url).read().decode()
#returns bytes so need to be decoded first
json_parsed = json.loads(json_file)
#transforms it into python dictionary
comments = json_parsed["comments"]
counter = 0
for comment in comments:
    counter += comment["count"]
    
print("Total", counter)