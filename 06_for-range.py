
range(20)# 0,1,2,3...19
x = range(10,20)
y = range(10,20, 2)

for i in y:
    print(i) # 0,1,2,3...19

print("Impresor de tabla de multiplicar")
valorAMultiplicar = int(input('Ingrese el número de la tabla que desea: '))

range(0,10)
for i in range(1,11):
    print("%s x %s = %s" %(valorAMultiplicar, i,valorAMultiplicar*i))