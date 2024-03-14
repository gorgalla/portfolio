'''
counter = 0

while counter <= 11:
    print(counter)
    if counter == 7:
        break
    counter += 1
'''

i = 0

while i < 20:
    i += 1
    if i < 15: 
        continue
    print(i)