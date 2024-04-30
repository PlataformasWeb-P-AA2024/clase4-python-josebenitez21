
diccionario = {}

diccionario['nombres'] = "Jose Luis"
diccionario['apellidos'] = "Benitez Coronel"
diccionario['ciudad'] = "Loja"

print(diccionario.keys())
print("----------------------------------")
print(diccionario['apellidos'])
print("----------------------------------")
print(diccionario.values())

print("----------------------------------")

for x in diccionario.keys():
    print(diccionario[x])