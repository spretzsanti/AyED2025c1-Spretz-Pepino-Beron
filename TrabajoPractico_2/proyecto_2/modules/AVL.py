import datetime


class nodoAVL: #Cada nodoAVL es un dato de temperatura y fecha en si
    def __init__(self,fecha,temperatura):
        #Logicas para fechas, habria que revisarlo
        #si la fecha es un string
        if isinstance(fecha,str):
            self.fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date() #Convertimos string en fecha, aca asumo que viene en el formato solicitado pero habria que poner un control
        
        elif isinstance(fecha,datetime.date):
            self.fecha = datetime.date
        
        else:
            raise ValueError("La fecha debe venir en el formato correspondiente")

        self.temperatura = float(temperatura)
        
        #Logica NODO
        self.izquierda = None
        self.derecha = None
        self.altura = 1 #La altura de un nuevo nodo es 1


    #Esta funcion devuelve los valores, no se pide como tal pero la hago por las dudas
    def datos(self):
        return f"{self.fecha.strftime('%d/%m/%Y')}: {self.temperatura}°C (H:{self.altura})"


        



class AVL: 
    def __init__(self):
        self.raiz = None


    def altura(self, nodo):
        if not nodo:
            return 0

        return nodo.altura

    def factor_eq(self,nodo): #agregar validaciones
          return self._altura(nodo.izquierda) - self._altura(nodo.derecha)      

    def actualizar_altura(self,nodo): #actualizamos la altura de los nodos post rotaciones, a partir de la altura de sus hijos izq y der
        nodo.altura = 1+ max(self.altura(nodo.izquierda), nodo.altura(nodo.derecha))

    #Rotaciones
    
    #Podemos modificar los nombres para que sean mas representativos?Estan los comentarios igual PRG a PROFE
    def rot_derecha(self, z): #Z es el nodo de arriba del todo pre rotacion
        y = z.izquierda #Nueva raiz
        T2 = y.derecha

        #Rotacion en si
        y.derecha = z
        z.izquierda = T2

        #Actualizamos alturas
        self.actualizar_altura(z) #Altura depende de hijos como tal no cambio la altura
        self.actualizar_altura(y) #Esta altura si cambia ya que depende de hijos que tinen hijos

        return y #Devuelvo la raiz nueva

    def rot_izquierda(self,z):
        y = z.derecha
        T2 = y.izquierda

        #Rotacion
        y.izquierda = z
        z.derecha = T2

        #Act altura
        #Actualizamos alturas
        self.actualizar_altura(z) #Altura depende de hijos como tal no cambio la altura
        self.actualizar_altura(y) #Esta altura si cambia ya que depende de hijos que tinen hijos

        return y #Devuelvo la raiz nueva


    def rot_izq_der(self,z):
        z.izquierda = self.rot_izquierda(z.izquierda)

    def rot_der_izq(self,z):
         z.derecha = self.rot_derecha(z.derecha)


    #Metodos del propio arbol
    def insertar(self,nodo_actual,fecha:datetime.date, temperatura:float):

        #Inserciones normales
        if not nodo_actual:
            return nodoAVL(fecha,temperatura)

        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self.insertar(nodo_actual.derecha,fecha,temperatura) 
        
        elif fecha < nodo_actual.fecha:
            nodo_actual.izquierda = self.insertar(nodo_actual.izquierda,fecha,temperatura) 
        else:
            #Esto es para las fechas duplicadas, actualizamos el valor de la temperatura
            nodo_actual.temperatura = temperatura
            return nodo_actual



        #Paso 2
        self.actualizar_altura(nodo_actual)
        #Obtenemos FE
        balance = factor_eq(nodo_actual)

        
        #AHorad dependiendo del valor del factor de equolibrio hacemos las rotaciones correspondiente
        #Dos a la izq
        #El nodo está cargado a la izquierda (balance > 1) y se inserto en el subárbol izquierdo de su hijo izquierdo
        if balance > 1 and fecha < nodo_actual.izquierda.fecha:
            return self.rot_derecha(nodo_actual)

        #Dos a la derecha
        if balance < -1 and fecha > nodo_actual.izquierda.fecha:
            return self.rot_izquierda(nodo_actual)

        #Izquierda y derecha
        if balance > 1 and fecha > nodo_actual.izquierda.fecha:
            nodo_actual.izquierda = self.rot_izquierda(nodo_actual.izquierda)
            return self.rot_derecha(nodo_actual)
        #Derecha y izquierda
        if balance < -1 and fecha < nodo_actual.izquierda.fecha:
            nodo_actual.derecha = self.rot_derecha(nodo_actual.derecha)
            return self.rot_izquierda(nodo_actual)

        return nodo_actual #Si estaba bien




        






 




