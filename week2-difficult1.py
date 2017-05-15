# Python -> regex and parsing -> validating postal codes
# https://www.hackerrank.com/challenges/validating-postalcode

import re

a = raw_input()

print len(re.findall(r'(?=(\d)\d\1)',a)) < 2 and bool(re.match(r'^[1-9][0-9]{5}$',a))