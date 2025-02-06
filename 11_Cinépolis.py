from io import open
import os

class Cinepolis:
    # Declaración de propiedades
    _numBoletos=0
    _numPersonasCompradoras=0
    _nombreComprador=""
    _tarjetaCineco=0
    _totalCompra=0.0
    _totalCorte=0.0

    def _init_(self, numBoletos, numPersonasCompradoras, nombreComprador,tarjetaCineco,totalCompra):
        self._nombreComprador = nombreComprador
        self._numPersonasCompradoras = numPersonasCompradoras
        self._numBoletos = numBoletos
        self._tarjetaCineco=tarjetaCineco
        self._totalCompra= totalCompra

    def realizarCompra(self):
        print("Costo del Boleto: $12\nNota: Se pueden obtener descuentos comprando más de dos boletos y/o con tu tarjeta Cineco")
        self.pedirDatos(True,True,True) # Se mandan los tres parámetros True para pedir todos los datos

        self.aplicarRestriccion() #Verifica que no se sobrepase la cantidad de boletos que se pueden pedir por persona

        self.aplicarDescuentos() #Se calcula el descuento segpun el número de boletos comprados y si tiene tarjeta Cineco

        self.generarTicket()

    def generarTicket(self):
        texto=open("ticket.txt","a") # W hace que si no existe lo crea, si existe lo sobreescribe
        
            #f'{variable:<10}'
        cuentaConCineco=(self._tarjetaCineco==1)
        texto.write(f'\n| {str((self._nombreComprador[:12])):<12} ')
        texto.write(f'| {str(self._numPersonasCompradoras):<16} ')
        texto.write(f'| {str(self._numBoletos):<12}')
        texto.write(f'| {str(cuentaConCineco):<12}')
        texto.write(f'|$ {str(self._totalCompra):<12} |')
        texto.write("\n  ____________________________________________________________________________")
       
    def aplicarDescuentos(self):
        self._tarjetaCineco = self.verificarNumEntero("\n¿Comprarás con tarjeta Cineco? (Obtendrás un descuento)\n1.--Si\n2.--No\nSeleccione una opción numérica del menú: ",2)
        self._totalCompra=round(self._numBoletos*12)
        print(f"Costo antes de descuentos: ${self._totalCompra}")
        if(self._numBoletos>2 and self._numBoletos<6):
            self._totalCompra=round(self._totalCompra*.9) #Multiplicarlo por .9 equivale a quitarle el 10%
        if(self._numBoletos>5):
            self._totalCompra= round(self._totalCompra*.85) #Multiplicarlo por .85 equivale a quitarle el 15%
        if(self._tarjetaCineco==1):
            self._totalCompra=round(self._totalCompra*.9) #Multiplicarlo por .9 equivale a quitarle el 10%
        print(f"El costo de los boletos de {self._nombreComprador} es de: ${self._totalCompra}")
        self._totalCorte+=self._totalCompra

    def aplicarRestriccion(self):
        while((self._numBoletos/self._numPersonasCompradoras) > 7 ):
            print("\nRecuerda, solo se permiten 7 boletos por persona")
            opcionSel = self.verificarNumEntero("Menú:\n1.--Número de compradores\n2.--Número de boletos\n¿Qué le gustaría modficar?(Ingrese un número del menú): ",2)
            if(opcionSel==1):
                self.pedirDatos(False,True,False) #Solo pedirpa el número de compradores
            elif(opcionSel==2):
                self.pedirDatos(False,False,True) #Solo pedirá el número de boletos

    def pedirDatos(self,pedirNombre,pedirNumCompradores,pedirNumBoletos): # En cada variable, si el valor es True, pide el respectivo dato
        if(pedirNombre):
            self._nombreComprador = input("Ingrese el nombre del comprardor por favor: ")
        if(pedirNumCompradores):
            self._numPersonasCompradoras = self.verificarNumEntero('Ingrese el número de personas que comprarán: ',None)
        if(pedirNumBoletos):
            self._numBoletos = self.verificarNumEntero('Ingrese el número de boletos que comprarán en total (hasta 7 por persona): ',None)
        if(self._numPersonasCompradoras>self._numBoletos):
            print("No puede pedir menos boletos respecto al número de compradores. Intente de nuevo")
            self.pedirDatos(False,pedirNumCompradores,pedirNumBoletos)


    def verificarNumEntero(self,mensaje,rango):
        while(True):
            valor=0
            try:
                valor=int(input(mensaje))
                if((rango!= None) and (valor>rango)):
                    print("Valor fuera de rango. Intente de nuevo")
                else:
                    return valor
            except:
                print("\nEl valor ingresado es incorrecto. Tiene que ser un valor numérico entero del menú")
    

    def terminarCompra(self):
        texto=open("ticket.txt","r") # con r se lee el archivo
        lectura = texto.readlines()
        if(len(lectura)==0):
            print("No ha realizado ninguna compra")
            return False
        
        print("\nCompras del día: ")
        for i in lectura:
            print(i,end="")
        texto.close()
        print(f"\n|  Total del día:                                              |${self._totalCorte:<12}")
        print(" ____________________________________________________________________________")
        texto=open("ticket.txt","w")
        texto.write("\n ____________________________________________________________________________")
        texto.write("\n|  Comprador   | No. compradores  | No. boletos | Cineco Card | Total a pagar |")
        texto.write("\n ____________________________________________________________________________")
        texto.close()
        return True



    def menu(self):
        os.system('cls')
        print("Bienvenidos a Cinépolis!")

        opcionSel=0
        while(True):
            opcionSel = self.verificarNumEntero('\n\nMENÚ PRINCIPAL\n1.---- Comprar boletos\n2.--- Terminar de comprar\nSeleccione una opción (ingrese solo un número entero de las opciones mostradas): ',2)
            
            if(opcionSel==1):
                os.system('cls')
                self.realizarCompra()
               
            elif(opcionSel==2): # 2 Significa la selección "Terminar compra"
                os.system('cls')
                if(self.terminarCompra()):
                    break
            
if __name__ == "__main__":
    cinepolis=Cinepolis()
    cinepolis.menu()





'''
        ¿Quiere comprar o terminar?
        ¿Cuántas personas vienen?
        ¿Quiénes compran?

        ¿Cuántos boletos comprarán?
        validar si cumplen con las restricciones
        Si falla pregunta ¿Cambias el número de personas o el número de boletos?

        Vas a pagar con efectivo o con tarjeta Cineco? (para desceunto adicional, en todos los casos)
        Mostrar del costo después de calcularlo

        Después de seleccionar "terminar" almacenar el nombre y el total a pagar 
        luego mostrar la tabla de la información con la info del archivo
        Si no selecciona "terminar" sino "comprar" de nuevo, se le sigue vendiendo al mismo y modificando el archivo en cuestión

        Para un nuevo proceso de venta se reescribe el archivo

        Todo en una clase  en archivo nuevo "Cinépolis"

            def modificarCompra(self):
        print("\nExiste una compra activa")
        opcionSel = self.verificarNumEntero("Menú:\n1.--Nombre del comprador\n2.--Número de compradores\n3.--Número de boletos\n¿Qué dato desea modificar?(Seleccione un valor numérico del menú): ",3)
        if(opcionSel==1):
            self.pedirDatos(True,False,False)
        if(opcionSel==2):
            self.pedirDatos(False,True,False)
        if(opcionSel==3):
            self.pedirDatos(False,False,True)

    '''

