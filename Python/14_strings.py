string = "Ella sabe programar en python"
print("hello" in string)
print("sabe" in string)

size = len(string)
print(size)
print(string.upper())
print(string.lower())
print(string.count('a'))

print(string.swapcase())
print(string.startswith("Ella"))
print(string.endswith("python"))
print(string.replace("python", "Rust"))

text = "Este es un titulo"
print(text.capitalize())
print(text.title())
print(text.isdigit())
print("344".isdigit())