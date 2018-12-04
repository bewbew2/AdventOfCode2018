import re
import numpy as np

with open(u'star5_input.txt', 'r') as f:
    patches = f.readlines()


def split_patches(p):
    return re.match(r"\#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,2})x(\d{1,2})", p)


def patch_update(px, py, phx, phy):
    global patch
    ihx = int(phx)
    ihy = int(phy)
    ix = int(px)
    iy = int(py)

    for i in range(ihx):
        for j in range(ihy):
            patch[i+ix][j+iy] += 1
    return True


def init_patch_count(mx, my):
    zx = int(mx)
    zy = int(my)

    pc = np.zeros((zx, zy), dtype="int")
    return pc


def count_patch(cp):
    """ this gonna be ugly big hammer
    """
    a_sum = 0
    for row in cp:
        for item in row:
            if item > 1:
                a_sum += 1
    return a_sum


def intact_patch(px, py, phx, phy):
    global patch
    intact = True
    ihx = int(phx)
    ihy = int(phy)
    ix = int(px)
    iy = int(py)

    for i in range(ihx):
        for j in range(ihy):
            if patch[i+ix][j+iy] == 1:
                pass
            else:
                intact = False
    return intact


max_x = 0
max_y = 0
max_hx = 0
max_hy = 0

for elf in patches:
    p_s = split_patches(elf)
    p_id = p_s.group(1)
    p_x = p_s.group(2)
    p_y = p_s.group(3)
    p_hx = p_s.group(4)
    p_hy = p_s.group(5)

    max_x = max(p_x, max_x)
    max_y = max(p_y, max_y)
    max_hx = max(p_hx, max_hx)
    max_hy = max(p_hy, max_hy)

print max_hx, max_hy
print 'max x dim', max_x + max_hx
print 'max y dim', max_y + max_hy
patch = init_patch_count(max_x + max_hx, max_y + max_hy)

for elf in patches:
    p_s = split_patches(elf)
    p_id = p_s.group(1)
    p_x = p_s.group(2)
    p_y = p_s.group(3)
    p_hx = p_s.group(4)
    p_hy = p_s.group(5)
    patch_update(p_x, p_y, p_hx, p_hy)

print patch.shape
print "Area of duplicate patches: {}".format(count_patch(patch))

for elf in patches:
    p_s = split_patches(elf)
    p_id = p_s.group(1)
    p_x = p_s.group(2)
    p_y = p_s.group(3)
    p_hx = p_s.group(4)
    p_hy = p_s.group(5)
    if intact_patch(p_x, p_y, p_hx, p_hy):
        print "id #{} is intact!".format(p_id)





