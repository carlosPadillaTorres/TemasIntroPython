

print("Dame dos números para multiplicarlos")

a = int(input('Ingresa el primer número:  '))
b = int(input('Ingresa el segundo número:  '))

result =0
i=0
textoRespuesta=""
while i<b:
    result +=a
    textoRespuesta= textoRespuesta+str(a)
    i+=1
    if(i<b):
        textoRespuesta= textoRespuesta+"+"

print(textoRespuesta,"=",result)
#print("El resultado multiplicar %s por %s es %s" %(a,b,result))