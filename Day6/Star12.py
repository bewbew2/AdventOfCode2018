import numpy as np
import numpy.ma as ma

# dang = np.loadtxt('6_test.txt', dtype=int, delimiter=',', usecols=(0, 1))
dang = np.loadtxt('star11_input.txt', dtype=int, delimiter=',', usecols=(0, 1))


def bound_box(arr):
    return 'heck'


def taxi_distance(t1, t2):
    return abs(t2[0] - t1[0]) + abs(t2[1] - t1[1])


x_col = dang[:, :1]
y_col = dang[:, 1:2]

x_box = np.amax(x_col, axis=None) + 2
y_box = np.amax(y_col, axis=None) + 1
z_box = len(dang)

safe_field = np.zeros((z_box, y_box, x_box), dtype='int')
mine_claims = np.full((z_box, y_box, x_box), False, dtype='bool')

for coord in dang:
    safe_field[0, coord[1], coord[0]] = 1

for i in range(x_box):
    for j in range(y_box):
        k = 0
        for p in dang:
            safe_field[k, j, i] = taxi_distance(p, (i, j))
            k += 1

print safe_field.sum(0)
safe_10k_mask = ma.masked_where(safe_field.sum(0) > 9999, safe_field.sum(0))
print safe_10k_mask
print len(safe_10k_mask.nonzero()[0])


# for i in range(x_box):
#     for j in range(y_box):
#         p_min = np.where(safe_field[:, j, i] == safe_field[:, j, i].min(0))[0]
#         if len(p_min) > 1:
#             mine_claims[p_min, j, i] = False
#         else:
#             mine_claims[p_min, j, i] = True
# # print mine_claims
#
# legit_points = []
# for k in range(z_box):
#     if True in mine_claims[k, 0, :]:
#         pass
#     elif True in mine_claims[k, -1, :]:
#         pass
#     elif True in mine_claims[k, :, 0]:
#         pass
#     elif True in mine_claims[k, :, -1]:
#         pass
#     else:
#         legit_points.append(k)
#
# print 'Legitimate points ', legit_points
#
# area = []
# for k in legit_points:
#     area.append(np.sum(mine_claims[k, :, :]))

# print 'Max Area ', max(area)

"""for i in range(x_box):
    for j in range(y_box):
        min_d = min(safe_field[0:z_box-1, ])
        for k in range(zbox - 1):



fig, ax = plt.subplots()
# for color in ['blue']:
ax.scatter(x_col, y_col, c='blue', alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
"""