import time
import re

"""
class Guard(object):
    def __init__(self, name):
        self.name = name

    def sleep_record(self, rec, ent):
        for t in range(nap_start.tm_min, nap_end.tm_min):
            sleeping_minute_of_hour[t] = sleeping_minute_of_hour[t] + 1
        self.
        return 

    def nap_total(self,nap_time):
        return 
"""


def guard_name(v):
    return v.split()[1].replace('#', '')


def time_record(t):
    return time.strptime(t, "%Y-%m-%d %H:%M")


def nap_duration(t1, t2):
    return t2.tm_min - t1.tm_min


def guard_dict(gd_input):
    tt = [re.match(r"^\[(.+)\].+", tm).group(1) for tm in gd_input]
    gs = [re.match(r"^\[.+\] (.+)", gd).group(1) for gd in guard_duty]
    return dict(zip(tt, gs))


with open(u'star7-8_input.txt', 'r') as f:
    guard_duty = f.readlines()

# timetable = [re.match(r"^\[(.+)\].+", tm).group(1) for tm in guard_duty]
# guard_stat = [re.match(r"^\[.+\] (.+)", gd).group(1) for gd in guard_duty]

d = guard_dict(guard_duty)
print d
sleepy_guard = {}  # {GuardID : sleepTime}
guard_record = {}  # {GuardID : [list of occurrences of naps at a minute]}
nap_len = 0

for key, value in sorted(d.items()):
    if 'Guard' in value:
        guard_id = guard_name(value)
        if guard_id not in sleepy_guard.keys():
            sleeping_minute_of_hour = [0] * 60
            sleepy_guard.update({guard_id: 0})
    elif 'falls' in value:
        nap_start = time_record(key)
    elif 'wakes' in value:
        nap_end = time_record(key)
        dur = nap_duration(nap_end, nap_start)
        last_nap = sleepy_guard[guard_id]
        nap_time = last_nap + dur

        sleepy_guard.update({guard_id: nap_time})
        for i in range(nap_start.tm_min, nap_end.tm_min):
            sleeping_minute_of_hour[i] = sleeping_minute_of_hour[i] + 1
        guard_record.update({guard_id: sleeping_minute_of_hour})

# for item in sorted(sleepy_guard.items()):
#    print item

print sorted(sleepy_guard, key=sleepy_guard.__getitem__, reverse=True)
m = sorted(sleepy_guard, key=sleepy_guard.__getitem__, reverse=True)[0]
print "Guard #{} slept {} minutes".format(m, sleepy_guard[m])
worst_record = guard_record[m]
print worst_record
max_recurrences = max(worst_record)
answer1 = worst_record.index(max_recurrences) + 1

print answer1
print answer1 * int(m)

sorted(time.strptime(timetable[0], "%Y-%m-%d %H:%M"))
