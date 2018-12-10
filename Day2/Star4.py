"""
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given
the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and
 fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing
character from either ID, producing fgij.)

Your puzzle answer was qysdtrkloagnfozuwujmhrbvx.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.
"""
import difflib
import re

with open(u'star3_input.txt', 'r') as f:
    box_ids = f.readlines()


def m_count(l_d):
    """Tis the season to take the list results from the handy function ndiff
    Looks for counts of + and - characters in the diff output which provides the number of mismatched letters between
    the compared strings * 2
    Returns True when there is a single place difference
    """
    rep_count = 0
    for item in l_d:
        if re.match('[-+]', item):
            rep_count += 1
    if rep_count/2 == 1:
        return True
    else:
        return False


# iterates through all the box ids, comparing with all others
for i in range(len(box_ids[:])):
    for j in range(i, len(box_ids)):
        b1 = box_ids[i]
        b2 = box_ids[j]
        diff = difflib.ndiff(b1, b2)
        l_diff = list(diff)
        if m_count(l_diff):
            print ''.join([k.strip() for k in l_diff if not re.match('[+-]', k)])


