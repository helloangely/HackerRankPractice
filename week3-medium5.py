# algorithms -> strings -> richie rich
# https://www.hackerrank.com/challenges/richie-rich

import sys

l, kmax = map(int, raw_input().strip().split())
n= raw_input().strip()

def FoldItUp(l, n):

    if l % 2 == 0:
        folded, middle = zip(n[:(l/2)+1], list(reversed(n[(l/2):]))), ''
    else:
        folded, middle = zip(n[:(l/2)], list(reversed(n[(l/2)+1:]))), str(n[l/2])


    ct = 0
    new_list = []
    for x, y in folded:
        if x == y:
            new_list.append([x])
        else:
            ct += 1
            new_list.append([x,y])
    return new_list, middle, ct
            
folded, middle_char, kmin = FoldItUp(l, n)
new_string, changes_made = '', 0

if kmax >= kmin:
    for idx in folded:
        if kmax - kmin > changes_made:
         
            if len(idx) < 2:
                if idx != ['9'] and (kmax-(kmin + changes_made) >=2):
                    new_string += '9'
                    changes_made += 2
                else:
                    new_string += idx[0]
            else:
                kmin -= 1
                if max(idx) == '9':
                    new_string += '9'
                    changes_made +=1
                elif kmax-(kmin + changes_made) >=2:
                    new_string += '9'
                    changes_made +=2
                else:
                    new_string += max(idx)
        else:
          
            new_string += max(idx)
            if len(idx) == 2:
                changes_made += 1
                kmin -= 1
    if middle_char and changes_made < kmax:
        middle_char = '9'
        changes_made += 1
else:
    
    new_string = None

result = str(new_string + middle_char + ''.join(list(reversed(new_string)))) if new_string is not None else '-1'
print result

