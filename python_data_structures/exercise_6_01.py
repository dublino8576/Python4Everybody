'''Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.'''

text = "X-DSPAM-Confidence:    0.8475"
#Parsing: changing data into other data types
#Extracting: extract the exact chunk of data to be able to perform PARSING

find = text.find(":")
#EXTRACT 
# 1.string from column since number could be not the same in multiple string data sets in data analysis. Column is a pattern that is always there (number could be 1.890 so find("0") may not always work) 
# 2. get all the string after column till the end 
# 3. strip() gets rid of extra space as there might be one extra space or more, this way is more precise
# 4. now you have a string that can be converted to a float

sliced_text = text[(find+1):len(text)].strip()
print(sliced_text)