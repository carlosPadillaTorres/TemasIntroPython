'''
    Las tuplas son inmutables
    Se declaran con ( )
'''

tupla = ("uno","dos","tres")
print(tupla)

tuplaVariosDatos=(12,True,23.5,"El gato",12+4j)
print(tuplaVariosDatos)

tuplaConTuplas=(1,2,3,4,(1,2,3))
print(tuplaConTuplas)

print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-1])
print(tuplaVariosDatos[0:2])

a,b,c=tupla
print(a,b,c)
