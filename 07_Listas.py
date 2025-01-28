'''
    Una lista es una secuencia de elementos
    Se crea con []
'''

lista1 = ["Dario",33,9.5,True,"Germán",20.8]

print(lista1)           # Imprime lista
print(lista1[:])        # Imprime todos los elementos de la lista
print(lista1[2])        # Imprime el tercer elemento de la lista
print(lista1[-2 ])      # Imprime el penúltimo elemento de la lista
print(lista1[1:3])      # Imprime los elmentos de la lista del elemento en la posición 1 al de la posición 3
print(lista1[3:])       # Imprime los útlios tres elementos

lista1.append("Vargas")
print(lista1)

lista1.insert(2,"Nadia")
print(lista1)

lista1.extend(["uno",1.1,False])
print(lista1)

lista1.remove(33)
print(lista1)

lista1.pop() # Extrae el último de la lista
print(lista1)

lista2=["tres","cuatro"]
print(lista2)

lista3=lista1+lista2
print(lista3)

print(lista2*4)
lista4=[2,1,5,4,3]
print(lista4)

print(lista4.sort())

del lista4[0]
print(lista4)