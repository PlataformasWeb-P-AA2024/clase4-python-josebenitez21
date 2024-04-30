nombre = input("Ingrese nombre de la persona\n")
edad = int(input("Ingrese edad de persona\n"))
sueldo = float(input("Ingrese el sueldo de la persona\n"))

mensajeFinal = "Nombre: %s \nEdad: %d \nSueldo: %.2f\n" %(nombre,edad,sueldo)
print(mensajeFinal)