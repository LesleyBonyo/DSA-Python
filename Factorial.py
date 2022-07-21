def factorial(num):
    factorial = 1
    if num == 1 | num == 0:
        factorial = 1
    else:
        for i in range(1, num+1):
            factorial = factorial * i
    return factorial


myfact = factorial(7)
print(myfact)
