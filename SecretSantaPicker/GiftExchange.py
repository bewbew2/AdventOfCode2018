import re
import random
import copy

with open('name_address_list.txt','r') as f:
    source_list = f.readlines()


def random_pick(nm):
    pic = nm[random.randint(0, len(nm)-1)]
    return pic


restricted_dict = {}
address_dict = {}
for row in source_list:
    row_obj = re.match(r"(\S+) \((\S+) (.+)", row)
    name = row_obj.group(1)
    address = row_obj.group(2)
    restricted = row_obj.group(3)
#    if name not in address_dict:
    address_dict.update({name:address})
#    if name not in restricted_dict:
    restricted_dict.update({name:restricted})

givers = address_dict.keys()
receivers = copy.deepcopy(givers)
result = []
message = []
this_restricted = []
for name in givers:
    this_restricted = [p for p in restricted_dict[name].split(" ")]
    this_restricted.append(name)
    qual = [person for person in receivers if person not in this_restricted]
    pick = random_pick(qual)
    receivers.remove(pick)
    message.append("{} you have {}".format(address_dict[name], pick))
    if name not in pick:
        result.append("{} buys for {}".format(name, pick))
    else:
        print "dammit, try again!"
        result = []
        break

for a in result:
    print a

print ' \n'
for a in message:
    print a


