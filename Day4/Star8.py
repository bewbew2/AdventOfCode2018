""" This is a crummy program that sort of solves day 4. Requires some digging to find the answer.
    but it works!
"""


import time
import re


class Guard(object):
    def __init__(self, name):
        self.name = name
        self.record = [0] * 60

    def sleep_record(self, rec, entry):
        return self.record

    def nap_total(self, nap_time):
        return


def guard_name(v):
    return v.split()[1].replace('#', '')


def time_record(t):
    return time.strptime(t, "%Y-%m-%d %H:%M")


def nap_duration(t1, t2):
    return t2.tm_min - t1.tm_min


def init_guards(gg):
    """
    # initialize structures with the list of guards
    # initialize a dict for each guard's naptime minutes
    # initialize a dict for the total sleeping time
    """
    g_rec = {}
    g_min = {}
    z_nap = [0] * 60
    for key, value in gg.items():
        if 'Guard' in value:
            g_id = guard_name(value)
            g_rec.update({g_id: 0})
            g_min.update({g_id: z_nap[:]})
    return g_rec, g_min


guard_id = 0
with open(u'star7-8_input.txt', 'r') as f:
    guard_duty = f.readlines()

timetable = [re.match(r"^\[(.+)\].+", tm).group(1) for tm in guard_duty]

guard_stat = [re.match(r"^\[.+\] (.+)", gd).group(1) for gd in guard_duty]

d = dict(zip(timetable, guard_stat))

m_total, minute_count = init_guards(d)
# print m_total
# print minute_count

for key, value in sorted(d.items()):
    if 'Guard' in value:
        guard_id = guard_name(value)
    elif 'falls' in value:
        nap_start = time_record(key)
    elif 'wakes' in value:
        nap_end = time_record(key)
        dur = nap_duration(nap_start, nap_end)
        m_total.update({guard_id: (m_total.get(guard_id) + dur)})
        #        print guard_record.values()

        a = minute_count.get(guard_id)
        for i in range(nap_start.tm_min, nap_end.tm_min):
            a[i] += 1

print sorted(m_total, key=m_total.__getitem__, reverse=True)
m = sorted(m_total, key=m_total.__getitem__, reverse=True)[0]

print "Guard #{} slept {} minutes".format(m, m_total[m])
worst_record = minute_count[m]
print worst_record
max_recurrences = max(worst_record)
answer1 = worst_record.index(max_recurrences)

print answer1
print answer1 * int(m)

sorted(time.strptime(timetable[0], "%Y-%m-%d %H:%M"))

w = []
g = []
for mint in minute_count:
    print u"guard: " + str(mint), (sorted(minute_count.get(mint), reverse=True)[0])

    w.append(sorted(minute_count.get(mint), reverse=True)[0])
    asdf = sorted(minute_count.get(mint), reverse=True)[0]
    print (sorted(minute_count.get(mint), reverse=True))
    print minute_count.get(mint).index(asdf)
   # g.append(minute_count.get(mint).index(w))

#print minute_count

print sorted(w, reverse=True)
print g

