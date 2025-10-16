import urllib.request, urllib.error, urllib.parse, ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter URL: ")


#use URLLIB python to perform get request with online url
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup) will show you html file in order, while print(html) will show you html file messy version
tags = soup('span')
counter = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('Contents:', tag.contents[0])
    counter += int(tag.contents[0])
    print('Attrs:', tag.attrs)
print(counter, "total")