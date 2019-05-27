survived_age = [48.0, 15.0, 40.0, 36.0, 47.0, \
32.0, 60.0, 31.0, 17.0, 36.0, 39.0, 36.0, 32.5, \
39.0, 38.0, 36.0, 52.0, 29.0, 35.0, 35.0, 49.0, \
16.0, 27.0, 22.0, 27.0, 35.0, 3.0, 11.0, 36.0, \
1.0, 19.0, 24.0, 33.0, 43.0, 24.0, 32.0, 49.0, \
30.0, 49.0, 60.0, 23.0, 26.0, 24.0, 40.0, 25.0, \
36.0, 48.0, 21.0, 29.0, 24.0, 44.0, 41.0, 2.0, \
28.0, 40.0, 22.0, 33.0, 35.0, 24.0, 28.0, 17.0, 16.0, 48.0]

non_survived_age = [47.0, 55.0, 36.0, 38.0, 19.0, \
24.0, 36.0, 45.5, 45.0, 46.0, 57.0, 25.0, 58.0, \
46.0, 50.0, 56.0, 58.0, 62.0, 64.0, 39.0, 21.0, \
47.0, 45.0, 18.0, 70.0, 2.0, 36.0, 61.0, 47.0, \
29.0, 40.0, 19.0, 65.0, 50.0, 54.0, 36.5, 31.0]

ave_survived_age = sum(survived_age) / len(survived_age)
ave_survived_age = round(ave_survived_age,2)

ave_non_survived_age = sum(non_survived_age) / len(non_survived_age)
ave_non_survived_age = round(ave_non_survived_age,2)

print("幸存者平均年龄为{}岁".format(ave_survived_age))
print("遇难者平均年龄为{}岁".format(ave_non_survived_age))
