import re
assem_seq = []
seq_dict = {}


def union_steps(d):
    r = []
    for key in d.keys():
        r.extend(d[key])
    return r


def available_steps(k, r, a):
    print set(k), set(r)
    a.extend(set(k) - set(r))
    return a


# with open('star13_input.txt', 'r') as f:
with open('7_test.txt', 'r') as f:
    inp = f.readlines()
    req_table = [re.match(r"^.{5}(.).{30}(.)", a).group(1, 2) for a in inp]

pre_reqs = [a[0] for a in req_table]
subsequent = [a[1] for a in req_table]
remain_steps = sorted(subsequent[:])

print 'all subsequent steps ', sorted(set(subsequent))

key_steps = sorted(set(pre_reqs))

for step in sorted(set(key_steps).difference(set(subsequent))):
    assem_seq.append(step)

print "Sequence ", assem_seq

# populate the requirements map for all the remaining steps
for step in sorted(set(subsequent)):
        seq_dict.update({step: sorted([p[1] for p in req_table if p[0] == step])})

print "Seq dict ", seq_dict
len_subs = len(subsequent)

while len_subs > 0:
    remain_steps = union_steps(seq_dict)
    av_steps = available_steps(seq_dict.keys(), remain_steps, assem_seq)
    for k in av_steps:
        try:
            del seq_dict[k]
        except KeyError:
            pass

    len_subs = len(seq_dict)

    print "assem seq ", av_steps


#while len(remain_steps) > 0:
#    assem_seq(d, ).append(available_steps)



#print assem_seq