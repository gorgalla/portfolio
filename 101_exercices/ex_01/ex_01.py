def anagrama(s1, s2):
    if len(s1) != len(s2):
        return(False)
    diccionario = {}

    for char in s1:
        print(diccionario)
        diccionario[char] = diccionario.get(char, 0) + 1
    print("\/" * 30)
    for char in s2:
        print(diccionario)
        if char not in diccionario or diccionario[char] == 0:
            return(False)
        diccionario[char] -= 1
    return(True)
s1 = input("Introduce una oración => ")
s2 = input("Introduce una oración => ")

anagrama(s1, s2)

'''
if anagrama(s1, s2):
        print(f"{s1} es un anagrama de {s2}")
else:
     print(f"{s1} NO es un anagrama de {s2}")
'''