lenguajes1={"C", "Pascal", "PHP", "Python"}
lenguajes2={"C++", "Java", "Python"}

print("Lenguajes estructurados")
print(lenguajes1)
print()

print("Lenguajes orientados a objetos")
print(lenguajes2)
print()

conjunto1=lenguajes1 | lenguajes2
print("Todos los lenguajes (Unión)")
print(conjunto1)
print()

conjunto2=lenguajes1 & lenguajes2
print("Intersección de los dos conjuntos de lenguajes (Intersección)")
print(conjunto2)
print()

conjunto3=lenguajes1 - lenguajes2
print("Diferencia de los dos conjuntos de lenguajes (Diferencia)")
print(conjunto3)
print()

conjunto4=lenguajes1 ^ lenguajes2
print("lenguajes del conjunto lenguajes1 o del conjunto lenguajes2 pero no en ambos (Diferencia simétrica)")
print(conjunto4)
print()