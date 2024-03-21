def fizzbuzz():
    n = 0
    while n <= 100:
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 5 == 0:
            print("buzz")
        elif n % 3 == 0:
            print("fizz")
        else:
            print(n)
        n += 1
fizzbuzz()
