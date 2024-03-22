def is_prime():
    i = 0
    n = 2
    while i <= 100:
        is_prime = True
        for k in range(2, n):
            if n % k == 0:
                is_prime = False
                break
        if is_prime:
            print(n)
        i += 1
        n += 1
is_prime()