texto1 = "Hola"
texto2 = "Mundo"

textoFinal= texto1+" "+texto2
print (textoFinal)

print("El saludo es: %s %s" %(texto1, texto2))

saludoFinal2 = "Saludo: {x} {y}".format(x=texto1,y=texto2) 
print(saludoFinal2)

texto = "desarrollo web profesional UTL"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print("Función find ",texto.find("al"))
print(texto.count("o"))

print(texto.replace("e","a"))

cadenaSeparada =  texto.split(" ")
print(cadenaSeparada)
