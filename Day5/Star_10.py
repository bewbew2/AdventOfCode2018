#with open('sample.txt', 'r') as f:
with open('star9_input.txt', 'r') as f:
    inp = f.readlines()
    inp_len = len(inp[0])

#print inp

s = inp[0].strip()
junk = []

for a in range(65,91):
    x = chr(a)
    y = chr(a+32)
    junk.append(x + y)
    junk.append(y + x)
print junk

new = 'a'
old = ''
count = 0
min_len = 1e12


for probe in junk:
    s = s.replace(probe[0], '')
    s = s.replace(probe[1], '')
    new = 'a'
    old = ''
#    print s
    while new != old:
        old = len(s)
        for j in junk:
            s = s.replace(j, '')
        new = len(s)
    if len(s) < min_len:
        min_len = len(s)
        min_letter = probe
#        print(str(min_len), probe)
    s = inp[0].strip()

print('shortest has {} char using {}'.format(min_len, min_letter))
# print s
# print len(s)

