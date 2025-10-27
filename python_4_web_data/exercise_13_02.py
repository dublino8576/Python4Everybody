import urllib.request, urllib.error, urllib.parse, ssl
from bs4 import BeautifulSoup

#Following Links in HTML Using BeautifulSoup

'''
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
'''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter url: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
#print("soup",soup)
a_tags = soup('a')
counter = 1
#use while loop to repeat action until the forth name is found
while counter < count:
    print("Retrieving: ", a_tags[position - 1].attrs["href"])
    new_url = a_tags[position - 1].attrs["href"]
    new_html = urllib.request.urlopen(new_url, context=ctx).read()
    new_soup = BeautifulSoup(new_html, "html.parser")
    new_a_tags = new_soup('a')
    a_tags = new_a_tags
    counter += 1
    
    if counter == count:
        print(a_tags[position - 1].contents[0])

