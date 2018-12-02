import difflib
import re
with open(u'star3_input.txt', 'r') as f:
    box_ids = f.readlines()


def mcount(_id):
    d = []
    t = []
    for letter in set(_id):
        n = _id.count(letter)
        if n == 2:
            d.append(n)
        if n == 3:
            t.append(n)
    return len(set(d)),len(set(t))


for i in range(len(box_ids)-1):
    for j in range(len(box_ids[i+1:])):
        b1 = box_ids[i]
        b2 = box_ids[j]
        diff = difflib.ndiff(b1, b2)
        l_diff = list(diff)
#        print l_diff
        for item in l_diff[:]:
            if re.match('[-+]', item):
                pass
            else:
                l_diff.pop()
        if len(l_diff)/2 == 2:
            print 'letters: ', l_diff
  #      print len(l_diff)/2


