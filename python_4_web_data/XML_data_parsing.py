'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2303396.xml (Sum ends with 74)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

#EXTRACTING DATA FROM XML INTO PYTHON

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
file = urllib.request.urlopen(url).read()
tree = ET.fromstring(file)
#tree that can be read by python and dissected easily with find, findall methods and has methods such as get and text to find text nodes or attribute nodes
comment_list = tree.findall("comments/comment")
counter = 0
for comment in comment_list:
    count = int(comment.find("count").text)
    counter += count
print("total", counter)