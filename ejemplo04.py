sueldo = int(input("Ingrese el sueldo de la persona\n"))

if sueldo <= 100:
    print("Correcto")
else:
    if (sueldo >= 101) and (sueldo <= 110):
        print("Sobresaliente")
    else:
        print("Incorrecto")
