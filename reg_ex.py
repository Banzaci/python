import re

str = 'I am not 65 but i have been 32.'

num = re.findall('[0-9]+', str)

print(num)