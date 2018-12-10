def reactive(a, b):
    x = False
    y = a.lower()
    z = b.lower()
    if y == z:
        if a < b:
            x = True
        elif a > b:
            x = True
    else:
        x = False
    return x


with open('star9_input.txt', 'r') as f:
    inp = f.readlines()
    inp_len = len(inp[0])


chain = [ch for ch in inp[0]]
print reactive('a', 'A')

out_p = []
seq = range(len(chain)-1)
#print seq
loopcount = 0
last = [1]
skip = False

print len(last)
print len(out_p)

while len(last) != len(out_p):
    last = out_p[:]
    print 'loopcount ', loopcount
    for i in seq:
        if not skip:
            c1, c2 = chain[i], chain[i+1]
            if not reactive(c1, c2):
                out_p.append(c1)
                print len(out_p)
            else:
                skip = True
        else:
            skip = False
    loopcount += 1

print out_p
print len(out_p)
print loopcount

