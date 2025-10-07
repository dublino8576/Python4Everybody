import re
file = open("regex_sum_2303392.txt")
content = file.read()

regex = re.findall(r'[0-9]+', content)
total = list(map(int, regex))
#total = sum([int(num) for num in re.findall(r'[0-9]+', content)])
'''with list comprehension'''
print(sum(total))