"""Second puzzle for Advent of code
--- Part Two ---
You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to
 find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of
frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the
middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
What is the first frequency your device reaches twice?

Although it hasn't changed, you can still get your puzzle input.

For my approach, I'll use list address incrementation for summing more and more entries. If we reach the end of the
list without a repeat, we'll continue to the beginning. Keep expanding the

Or I could reverse the list with [list].reverse.
sum = sum + list[]

"""


def sum_calibration(cal_list):
    """totals the input list
    """
    tot = 0
    for c in cal_list:
        tot = tot + int(c)
    return tot


def repeat_counter(sum_list, current):
    if current in sum_list:
        print 'found rep ', current
        return 1
    else:
        return 0


with open(u'star1_input.txt', 'r') as f:
    calibration = f.readlines()

sum_array = [0]
cal_length = len(calibration)
repeat_count = 0
loop = 0
last_sum = 0

while repeat_count == 0:
    for row in range(0, cal_length):
        current_sum = int(calibration[row]) + int(last_sum)
#        print 'current_sum ', current_sum
#        print 'sum array ', sum_array
#        print 'last ',last_sum,' current ', current_sum
        last_sum = current_sum
        repeat_count = repeat_count + repeat_counter(sum_array, current_sum)
        sum_array.append(current_sum)
#        print 'RC ', repeat_count
        if repeat_count > 0:
            break
    loop += 1
    print 'loop', loop, 'last ', calibration[row]

print u'repeated sum: ', current_sum
print u'loops ', loop
print u'rows ', row
print u'total = ', sum_calibration(calibration)

