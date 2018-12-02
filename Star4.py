import difflib
import re
with open(u'star3_input.txt', 'r') as f:
    box_ids = f.readlines()


def mcount(l_d):
    rep_count = 0
    for item in l_d:
        if re.match('[-+]', item):
            rep_count += 1
#    print rep_count

    if rep_count < 5:
        if rep_count > 0:
            return True
    else:
        return False


for i in range(len(box_ids)):
    for j in range(len(box_ids[i:])):
        b1 = box_ids[i]
        b2 = box_ids[j]
        diff = difflib.ndiff(b1, b2)
        l_diff = list(diff)
#        print l_diff
        if mcount(l_diff):
            print 'letters: ', l_diff


