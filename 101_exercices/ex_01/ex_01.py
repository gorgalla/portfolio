def anagrama(s1, s2):
    # Combrobamos si las longitudes de s1 y s2 son diferentes, si es asi, no son un anagrama.
    if len(s1) != len(s2):
        return(False)
    
    # Creamos un diccionario en el que vamos a almacenar cada uno de los caracteres que componen s1
    diccionario = {}
    # Recorremos s1 caracter por caracter
    for char in s1:
        # Almacenamos cada uno de los caracteres de s1 en el diccionario utilizando el componente .get, sumamos + 1 para asi poder llevar un conteo de que ese caracter no ha sido comparado con s2 toavia
        diccionario[char] = diccionario.get(char, 0) + 1
    # Creamos otro bucle para recorrer caracter a caracter la string s2
    for char in s2:
        # Comprobamos el posible caso de que el caracter de s2 no se encuentre en el diccionario, si es así devolvemos False
        if char not in diccionario or diccionario[char] == 0:
            return(False)
        # Restamos - 1 a char para si determinar que ese carcater coincidente ya se ha comprobado.
        diccionario[char] -= 1
    return(True)

s1 = input("Introduce una palabra => ")
s2 = input("Introduce otra palabra => ")

if s1 == False or s2 == False:
    return(False)
if anagrama(s1, s2):
    print(f"{s1} y {s2} son un anagrama")
else:
    print("No son un anagrama")