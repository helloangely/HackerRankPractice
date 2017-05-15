# algorithms -> strings -> bear and steady
# https://www.hackerrank.com/challenges/bear-and-steady-gene

import sys

N = int(raw_input())
S = list(raw_input())

def substring_len(s):
    #Get count of letters
    letter_count = {'A':0,'T':0,'G':0,'C':0}
    for i in range(len(s)):
        letter_count[s[i]] += 1

    for k,v in letter_count.items():
        if v > N/4:
            letter_count[k] = int(letter_count[k] - N/4)
        else:
            letter_count[k] = 0


    change_count = 0
    for v in letter_count.values():
        change_count += v
    if change_count == 0:
        return 0


    min_length = len(s)
    start = 0
    end = 0
    hasFound = False

    substring_count = {'A':0,'T':0,'G':0,'C':0}

    while True:
        if end >= len(s):
            return min_length
        hasFound = True
        for k,v in substring_count.items():
            if substring_count[k] < letter_count[k]:
                hasFound = False
        if hasFound == True:
            if end - start < min_length:
                min_length = end - start
            substring_count[s[start]] -= 1 
            start += 1
            continue
        if hasFound == False:
            substring_count[s[end]] += 1
            end += 1
            continue

print(substring_len(S))
