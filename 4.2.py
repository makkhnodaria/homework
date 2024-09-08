a = [0, 7, 9, 12, -1, 100]
# a = []

b = 0
for i in range(len(a)):
    if i % 2 == 0:
        b += a[i]
print(b * (a[-1] if len(a) != 0 else 0))
