import re
with open(u'star5_input.txt', 'r') as f:
    patches = f.readlines()


def split_patches(p):
    return re.match(r"\#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,2})x(\d{1,2})",p)


for patch in patches:
    p = split_patches(patch)
    p_id = p.group(1)
    p_x = p.group(2)
    p_y = p.group(3)
    p_hx = p.group(4)
    p_hy = p.group(5)

    print p_id
    print p_hx, p_hy
    print p_x, p_y
