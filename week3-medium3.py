# algorithms -> strings -> sherlock and anagrams
# https://www.hackerrank.com/challenges/sherlock-and-anagrams

from collections import *
for i in range(input()):
    s = raw_input()
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    sum = 0
    for i in check:
        n = check[i]
        sum += (n*(n-1))/2
    print sum
