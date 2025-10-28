#CALLING A JSON API

'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/opengeo.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first plus_code from the JSON. An Open Location Code is a textual identifier that is another form of address based on the location of the address.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Open Street Map Data.

http://py4e-data.dr-chuck.net/opengeo?
This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to provide the address that you are requesting as the q= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/opengeo.py
'''
import urllib.request, urllib.parse, json
service_url = "http://py4e-data.dr-chuck.net/opengeo?"
while True:
    address = input("Enter location: ")
    if len(address) < 1: break
    address = address.strip()
    location_dictionary = dict()
    location_dictionary["q"] = address

    print(location_dictionary["q"])
    #encode location into the service url to get the approriate query url
    url = service_url + urllib.parse.urlencode(location_dictionary)
    file = urllib.request.urlopen(url).read().decode()
    #print(file)
    try:
        js = json.loads(file)
    except:
        js = None
    if not js or "features" not in js:
        print("===DOWNLOAD ERROR===")
        print(file)
        break
    if len(js["features"]) == 0:
        print("===OBJECT NOT FOUND===")
        print(file)
        break
    #use dumps to show indentations and make json pretty
    #it is just a print as it transforms dictionary into a string and cannot work with this
    print(json.dumps(js, indent=4)) 
    #looking at print you can easily find path to plus_code
    location = js["features"][0]["properties"]["plus_code"]
    print(location)
