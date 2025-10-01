'''7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.'''

try:
    file_name = input("Enter file name: ")
except:
    print("Invalid file name")
    quit()
file = open(file_name, "r")
sliced_string = "X-DSPAM-Confidence:"
count = 0
float_total = 0
for line in file:
    line_2 = line.rstrip()
    if not line_2.startswith(sliced_string):
        continue
    count += 1
    float_number = float(line_2[line_2.find(":") + 2:])
    float_total += float_number

avg_spam_confidence = float_total / count
print("Average spam confidence:", avg_spam_confidence)