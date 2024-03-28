def factorial(n):
    """
    Calcula el factorial de n
    
    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

i = int(input("Intoduce un numero para conocer su factorial => "))
while i != 0:
    print(factorial(i))
    i -= 1