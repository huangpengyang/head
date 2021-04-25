try:
    a = [1, 2]
    print(a[100])
except IndexError:
    print('超出索引范围')
print(11)
print(22)