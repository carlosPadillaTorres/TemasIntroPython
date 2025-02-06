
from io import open
import math

lectura = ""
texto=open("archivo.txt","r") # W hace que si no existe lo crea, si existe lo sobreescribe
                              # con a se agrega contenido al archivo
                              # con r se lee el archivo
#texto.write("Hola, Mundo2\n")
#lectura = texto.read()
lectura = texto.readlines()

print(type(lectura))
#print(lectura)

for i in lectura:
    print(i)

texto.close()