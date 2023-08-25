max_value = 0
a = 0
b = 0

for i in range(1, 100+1):
    j = 100 - i
    c = i * j
    if c > max_value:
        max_value = c
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))