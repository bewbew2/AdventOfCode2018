with open('star9_input.txt', 'r') as f:
    inp = f.readlines()
    inp_len = len(inp[0])

print inp

s = inp[0].strip()
junk = []

for a in range(65,91):
    x = chr(a)
    y = chr(a+32)
    junk.append(x + y)
    junk.append(y + x)
print junk
"""
junk = (['aA','bB','cC','dD','eE','fF','gG','hH','iI','jJ','kK','lL','mM','nN','oO','pP','qQ','rR','sS','tT','uU','vV'
    ,'wW','xX','yY','zZ','Aa','Bb','Cc','Dd','Ee','Ff','Gg','Hh','Ii','Jj','Kk','Ll','Mm','Nn','Oo','Pp','Qq','Rr','Ss'
    ,'Tt','Uu','Vv','Ww','Xx','Yy','Zz'])
"""

new = 'a'
old = ''
count = 0

while new != old:
    old = len(s)
    for j in junk:
        s = s.replace(j, '')
    new = len(s)
    count += 1

print('count', count)
print s
print len(s)

