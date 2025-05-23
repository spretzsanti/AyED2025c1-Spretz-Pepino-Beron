import datetime
 

class nodoAVL: #Cada nodoAVL es un dato de temperatura y fecha en si
    def __init__(self,fecha:datetime.date,temperatura):
        #Logicas para fechas, habria que revisarlo
        #si la fecha es un string
      
        if not isinstance(fecha,datetime.date):
            raise ValueError("La fecha debe venir en el formato correspondiente (Error en guardar_temp)")
        

        self.temperatura = float(temperatura)
        self.fecha = fecha
        #Logica NODO
        self.izquierda = None
        self.derecha = None
        self.altura = 1 #La altura de un nuevo nodo es 1


    #Esta funcion devuelve los valores, no se pide como tal pero la hago por las dudas
    def datos(self):
        return f"{self.fecha.strftime('%d/%m/%Y')}: {self.temperatura}°C (H:{self.altura})"


        



class AVL: 
    #Constructir
    def __init__(self):
        self.raiz = None

    #Devuelve altura
    def altura(self, nodo):
        if not nodo:
            return 0

        return nodo.altura

    #Devuelve Factod de eq
    def factor_eq(self,nodo): #agregar validaciones
          return self.altura(nodo.izquierda) - self.altura(nodo.derecha)      



    #Actualiza altura de los nodos
    def actualizar_altura(self, nodo):
        if not nodo: # Si el nodo es None
            return   # No hacemos nada y salimos
        # Si el nodo SÍ existe, entonces procedemos con la lógica original:
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))




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
        return self.rot_derecha(z)

    def rot_der_izq(self,z):
         z.derecha = self.rot_derecha(z.derecha)
         return self.rot_izquierda(z)


    #Metodo publico de busqueda
    def buscar(self,fecha_obj:datetime.date):
        
        nodo_encontrado = self._buscar_nodo(self.raiz,fecha_obj)
        if nodo_encontrado:
            return nodo_encontrado.temperatura
        return None # Devuelve None si no se encuentra


    #Metodo privado de busqueda
    def _buscar_nodo(self,nodo_actual,fecha_obj):
        if not nodo_actual or nodo_actual.fecha == fecha_obj:
            return nodo_actual

        if fecha_obj < nodo_actual.fecha:
            return self._buscar_nodo(nodo_actual.izquierda,fecha_obj)
        else: # fecha_obj > nodo_actual.fecha
            return self._buscar_nodo(nodo_actual.derecha, fecha_obj)

    #Metodo publico de insersion
    def insertar(self,fecha:datetime.date, temperatura:float):
        self.raiz = self._insertar(self.raiz,fecha,temperatura)


    #Metodos del propio arbol, privado
    def _insertar(self,nodo_actual,fecha:datetime.date, temperatura:float):

        #Inserciones normales
        if not nodo_actual:
            return nodoAVL(fecha,temperatura)

        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self._insertar(nodo_actual.derecha,fecha,temperatura) 
        
        elif fecha < nodo_actual.fecha:
            nodo_actual.izquierda = self._insertar(nodo_actual.izquierda,fecha,temperatura) 
        else:
            #Esto es para las fechas duplicadas, actualizamos el valor de la temperatura
            nodo_actual.temperatura = temperatura
            return nodo_actual



        #Paso 2
        self.actualizar_altura(nodo_actual)
        #Obtenemos FE
        balance = self.factor_eq(nodo_actual)

        
        #AHorad dependiendo del valor del factor de equolibrio hacemos las rotaciones correspondiente
        #Dos a la izq
        #El nodo está cargado a la izquierda (balance > 1) y se inserto en el subárbol izquierdo de su hijo izquierdo
        if balance > 1 and fecha < nodo_actual.izquierda.fecha:
            return self.rot_derecha(nodo_actual)

        #Dos a la derecha
        if balance < -1 and fecha > nodo_actual.derecha.fecha:
            return self.rot_izquierda(nodo_actual)

        #Izquierda y derecha
        if balance > 1 and fecha > nodo_actual.izquierda.fecha:
            nodo_actual.izquierda = self.rot_izquierda(nodo_actual.izquierda)
            return self.rot_derecha(nodo_actual)
        #Derecha y izquierda
        if balance < -1 and fecha < nodo_actual.derecha.fecha:
            nodo_actual.derecha = self.rot_derecha(nodo_actual.derecha)
            return self.rot_izquierda(nodo_actual)

        return nodo_actual #Si estaba bien




    def obtener_rangos(self,fecha_min:datetime.date,fecha_max:datetime.date):
            temperaturas_encontradas = []
            self._obtener_rangos(self.raiz,fecha_min,fecha_max,temperaturas_encontradas)
            return temperaturas_encontradas

    def _obtener_rangos(self,nodo_actual,fecha_min,fecha_max,temperaturas_encontradas):
            if not nodo_actual:
                return

            #Si la fecha minima es menor a la actual no revisamos aca
            if fecha_min < nodo_actual.fecha:
                self._obtener_rangos(nodo_actual.izquierda, fecha_min, fecha_max, temperaturas_encontradas)
            #Si la fecha esta en rango agregamos la temperatura
            if fecha_min <= nodo_actual.fecha <= fecha_max:
                temperaturas_encontradas.append(nodo_actual.temperatura)
            
            #Si la fecha es mas grande que la actual revisamos al otro lado
            if fecha_max > nodo_actual.fecha:
                self._obtener_rangos(nodo_actual.derecha, fecha_min, fecha_max, temperaturas_encontradas)

    
    #Este lo uso para 
    def obtener_valor_minimo(self,nodo_actual):
        if nodo_actual is None or nodo_actual.izquierda is None:
            return nodo_actual
        actual = nodo_actual
        while actual.izquierda is not None:
         actual = actual.izquierda
        return actual


    
    def eliminar(self,fecha:datetime.date):
        #Al eliminar cualquier nodo puede ser la nueva raiz

        self.raiz = self._eliminar(self.raiz,fecha)

    def _eliminar(self,nodo_actual,fecha):
        if not nodo_actual:
            return nodo_actual

        if fecha <  nodo_actual.fecha:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda,fecha)
        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha,fecha)
        else: #Aca ya lo encontramos
            #Debemos tener en cuenta varios casos, esto se me ocurrio a mi cpz que hay alguna manera mas efectiva de hacerlo






            #Caso 1 nodo con un solo hijo o sin hijos
            if nodo_actual.izquierda is None:
                nodo_temporal = nodo_actual.derecha
                return nodo_temporal #El hijo de la derecha reemplaza al actual, si es none es none
            elif nodo_actual.derecha is None:
                nodo_temporal = nodo_actual.izquierda
                return nodo_temporal

            #Caso 2 nodo con dos hijos, aca vamos a aplicar el concepto de sucesor in-order revisar wiki, buscamos el mejor sucesor para los dos hijos huerfanos jajajajajjaja

            #Buscamos el menor valor del arbol, es decir el "sucesor"
            nodo_temporal = self.obtener_valor_minimo(nodo_actual.derecha)


            #Copiamos el sucesor en el eliminado
            nodo_actual.fecha = nodo_temporal.fecha
            nodo_actual.temperatura = nodo_temporal.temperatura
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, nodo_temporal.fecha)
            #Actualizamos altura
            self.actualizar_altura(nodo_actual)


            #Balance para luego rotar
            balance = self.factor_eq(nodo_actual)

            #Rotaciones, las mismas que al insertar
            if balance > 1 and fecha < nodo_actual.izquierda.fecha:
                return self.rot_derecha(nodo_actual)

                #Dos a la derecha
            if balance < -1 and fecha > nodo_actual.derecha.fecha:
                return self.rot_izquierda(nodo_actual)

                #Izquierda y derecha
            if balance > 1 and fecha > nodo_actual.izquierda.fecha:
                    nodo_actual.izquierda = self.rot_izquierda(nodo_actual.izquierda)
                    return self.rot_derecha(nodo_actual)
                #Derecha y izquierda
            if balance < -1 and fecha < nodo_actual.derecha.fecha:
                    nodo_actual.derecha = self.rot_derecha(nodo_actual.derecha)
                    return self.rot_izquierda(nodo_actual)

            return nodo_actual #Si estaba bien

















        






 




