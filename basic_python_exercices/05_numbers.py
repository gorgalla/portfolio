from statistics import mean

enero = int(input("Ingrese el presupuesto de Enero: "))
febrero = int(input("Ingrese el presupuesto de Febrero: "))
marzo = int(input("Ingrese el presupuesto de Marzo: "))
abril = int(input("Ingrese el presupuesto de Abril: "))

promedio = enero + febrero + marzo + abril
promedio = promedio / 4
print(promedio)

# Otra forma
 
mayo = int(input("Mayo: "))
junio = int(input("Junio: "))
julio = int(input("Julio: "))
agosto = int(input("Agosto: "))

mean = mean([mayo, junio, julio, agosto])

print(mean)