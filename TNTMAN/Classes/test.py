map_array = []
for x in range (0, 26):
    for y in range (0, 20):
        map_array.append([x, y])
lim = map_array.count()
for i in range(0, lim):
    print(map_array[i])