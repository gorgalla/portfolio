# CRUD => Create, Read, Update & Delete

num = [1, 2, 3, 4, 5, 6, 7]
print(num[2])
num[-1] = 88
print(num)

num.append(700)
print(num)

num.insert(0, "hola")
print(num)

num.insert(3, "kaixo")
print(num)

tasks = ["to do 1", "to do 2", "to do 3"]
new_list = tasks + num

print(new_list)

position = new_list.index(5)

new_list[position] = 'new'
print(new_list)

new_list.remove("to do 1")
print(new_list)

new_list.pop()
print(new_list)

lista = [8, 3, 5, 1, 7, 2, 6]

lista.sort()
print(lista)