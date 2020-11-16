sum = 0
for i in range(100, 201):
    if i % 2 == 0 and i % 5 != 0:
        sum += 1
print(sum, '个')
