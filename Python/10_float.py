x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

y_string = format(y, ".2g")
print("Now 'y' is => ", y_string)

print(y_string == str(x))

print(" " * 18)
print("*" * 18)
print(" " * 18)

tolerance = 0.1
print(abs(x - y) < tolerance)