
#[]
archivo = open("data/atp_tennis.csv","r")
lineas = archivo.readlines()

lineas = [l.split ("|") for l in lineas]

for x in lineas:
    cadena = "Torneo: %s\nGanador: %s" % (x[9],x[9])
print(cadena)
   

cadena = """ <b>Torneo:</b> %s  <br><b>Ganador:</b> %s""" % (x[9],x[9])
print(cadena)

archivo_generado = open("data/%s.html" % (x[9]),"w")
archivo_generado.writelines("%s\n" % (cadena))
archivo_generado.close()