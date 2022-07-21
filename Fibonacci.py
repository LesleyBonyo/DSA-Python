
first = 0
second = 1
print(first)
print(second)
for i in range(second, 20):
    temp = second
    second = second + first
    first = temp
    print(second)
