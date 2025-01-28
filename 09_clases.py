import math

class OperasBas:
        # Declaración de propiedades
    #uno =0  # public
   # _num2=0  # private (con guión bajo al inicio)
    #__res=0   # protected (con doble guión bajo al inicio)

    x1=0
    y1=0
    x2=0
    y2=0
    distancia=0

    # Declaración del constructor (self = this) Siempre lleva self aunque no tengan parámetros
    '''
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    '''
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1

        self.x2=x2
        self.y2=y2

    # Declaración de métodos de clase
    '''
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))
    '''

    def pedirDatos(self):
        self.x1 = int(input("Ingrese la coordenada x del punto A  "))
        self.y1 = int(input("Ingrese la coordenada y del punto A  "))
        self.x2 = int(input("Ingrese la coordenada x del punto B  "))
        self.y2 = int(input("Ingrese la coordenada x del punto C  "))


    def calcularDistancia(self):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        print("Valores : %s, %s, %s, %s, " %(x1,y1,x2,y2))
        self.distancia = math.sqrt( ((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)) )

        print("\nLa distancia entre A y B es: {}".format(self.distancia))

def main():
    #obj=OperasBas(3,4)
    #obj.suma()

    obj=OperasBas(0,0,0,0)
    print("\n\nBienvendio a la calculadora de distancia entre dos puntos\n")
    obj.pedirDatos() 
    obj.calcularDistancia()  


if __name__ =="__main__":
    main()
    

    