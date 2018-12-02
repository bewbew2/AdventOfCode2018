
with open(u'star3_input.txt', 'r') as f:
    box_ids = f.readlines()

sorted_ids = []
count_triple = 0
t_c = 0
d_c = 0


def mcount(_id):
    d = []
    t = []
    for letter in set(_id):
        n = _id.count(letter)
        if n == 2:
            d.append(n)
        if n == 3:
            t.append(n)
    return (len(set(d)),len(set(t)))


def id_sort(_id):
    return ''.join(sorted(_id))


for box_id in box_ids:
    sorted_ids.append(id_sort(box_id))

for box in sorted_ids:
    print mcount(box)
    a, b = mcount(box)
    d_c = d_c + a
    t_c = t_c + b


cksum = d_c * t_c
print d_c, t_c, cksum

"""
for box_id in sorted_ids:
    if has_triples(box_id):
        count_triple += 1

for item in sorted_ids:
    print item

print count_triple
"""
