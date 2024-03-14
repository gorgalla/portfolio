my_list = [1, -1, 2, -2, 3, -3, 4, -4, 7, 2, 9]
new_list = []
new_list = new_list + my_list

# Escribe tu solución 👇

i = 0
for i in new_list:
    if i < 0:
        new_list.remove(i)
        
print(new_list)