"""
First puzzle for AoC2018
"""


def sum_calibration(cal_list):
    """totals the input list
    """
    tot = 0
    for c in cal_list:
        tot = tot + int(c)
    return tot


with open(u'star1_input.txt', 'r') as f:
    calibration = f.readlines()

print u'total = ', sum_calibration(calibration)
