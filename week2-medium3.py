# python, sets, no idea!
# https://www.hackerrank.com/challenges/no-idea

n, m = map(int, raw_input().split())
narray = map(int, raw_input().split())
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))

print sum(1 if i in a 
          else -1 if i in b 
          else 0 
          for i in narray)