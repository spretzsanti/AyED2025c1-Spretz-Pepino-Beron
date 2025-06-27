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
    def buscar(self,fecha_obj:datetime.date):#O(log n) -> por linea 103 "self._buscar_nodo(self.raiz,fecha_obj)"
        
        nodo_encontrado = self._buscar_nodo(self.raiz,fecha_obj)
        if nodo_encontrado:
            return nodo_encontrado.temperatura
        return None # Devuelve None si no se encuentra


    #Metodo privado de busqueda
    def _buscar_nodo(self,nodo_actual,fecha_obj):#O(log n) -> busqueda recursiva en el arbol AVL
        if not nodo_actual or nodo_actual.fecha == fecha_obj:
            return nodo_actual

        if fecha_obj < nodo_actual.fecha:
            return self._buscar_nodo(nodo_actual.izquierda,fecha_obj)
        else: # fecha_obj > nodo_actual.fecha
            return self._buscar_nodo(nodo_actual.derecha, fecha_obj)

    #Metodo publico de insersion
    def insertar(self,fecha:datetime.date, temperatura:float):#O(log n) -> por linea 121 (self._insertar(self.raiz,fecha,temperatura))
        self.raiz = self._insertar(self.raiz,fecha,temperatura)


    #Metodos del propio arbol, privado
    def _insertar(self,nodo_actual,fecha:datetime.date, temperatura:float):#O(log n) -> recorre camino desde la raiz hasta las hojas, las rotaciones son O(1) pero se ejecutan en cada nivel

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


    def obtener_rangos(self,fecha_min:datetime.date,fecha_max:datetime.date):# O(k + log n) -> por linea 173
            temperaturas_encontradas = []
            self._obtener_rangos(self.raiz,fecha_min,fecha_max,temperaturas_encontradas)
            return temperaturas_encontradas

    def _obtener_rangos(self,nodo_actual,fecha_min,fecha_max,temperaturas_encontradas):# O(k + log n) -> k = nodos en el rango [fecha_min, fecha_max]; Debe recorrer todos los nodos dentro del rango (k); Más el costo de llegar al rango (log n)


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

    #Metodo publico para obtener rangos en un orden
    def obtener_datos_en_rango_ordenados(self, fecha_min, fecha_max):# O(k + log n) -> linea 196
        datos_encontrados = []
        self._obtener_datos_en_rango_ordenados(self.raiz, fecha_min, fecha_max,datos_encontrados)
        return datos_encontrados

    def _obtener_datos_en_rango_ordenados(self,nodo_actual, fecha_min, fecha_max,datos_encontrados):# O(k + log n)-> Recorre k nodos en el rango y Más costo de navegación al rango (log n); (similar al anterior)

        if not nodo_actual:
            return

        if nodo_actual.fecha > fecha_min:
            self._obtener_datos_en_rango_ordenados(nodo_actual.izquierda,fecha_min,fecha_max,datos_encontrados)

        #Si esta en rango agregamos a datos encontrados
        if fecha_min <= nodo_actual.fecha <= fecha_max:
            datos_encontrados.append((nodo_actual.fecha, nodo_actual.temperatura))

        if nodo_actual.fecha < fecha_max:
            self._obtener_datos_en_rango_ordenados(nodo_actual.derecha, fecha_min, fecha_max, datos_encontrados)

        

    def contar_nodos(self):#  O(n) -> linea 217
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self,nodo_actual):#  O(n) -> Recorre recursivamente todos los nodos del árbol
        if not nodo_actual:
            return 0


        return 1 +  self._contar_nodos(nodo_actual.izquierda) + self._contar_nodos(nodo_actual.derecha)



    #Este lo uso para temperatura
    def obtener_valor_minimo(self,nodo_actual):# O(log n) -> busca el nodo mas a la izquierda (peor caso recorre la altura del arbol)
        if nodo_actual is None or nodo_actual.izquierda is None:
            return nodo_actual
        actual = nodo_actual
        while actual.izquierda is not None:
         actual = actual.izquierda
        return actual


    
    def eliminar(self,fecha:datetime.date):# O(log n) -> linea 242
        #Al eliminar cualquier nodo puede ser la nueva raiz

        self.raiz = self._eliminar(self.raiz,fecha)

    def _eliminar(self, nodo_actual, fecha):# O(log n) -> Busca el nodo (log n) + busca sucesor (log n)
        if not nodo_actual:
            return nodo_actual

        # 1. Bajamos por la rama correcta
        if fecha < nodo_actual.fecha:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, fecha)
        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, fecha)
        else:
            # 2. Encontramos el nodo a borrar
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            # Caso con dos hijos: buscamos sucesor in-order
            sucesor = self.obtener_valor_minimo(nodo_actual.derecha)
            nodo_actual.fecha = sucesor.fecha
            nodo_actual.temperatura = sucesor.temperatura
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, sucesor.fecha)

        # 3. (Muy importante) Tras borrar en la subrama, actualizamos altura y balance
        self.actualizar_altura(nodo_actual)
        balance = self.factor_eq(nodo_actual)


        # 4. Rebalanceamos si es necesario (mismos casos que en la inserción)
        #    • Rotación simple a la derecha
        if balance > 1 and self.factor_eq(nodo_actual.izquierda) >= 0:
            return self.rot_derecha(nodo_actual)

        #    • Rotación simple a la izquierda
        if balance < -1 and self.factor_eq(nodo_actual.derecha) <= 0:
            return self.rot_izquierda(nodo_actual)

        #    • Rotación doble (izq–der)
        if balance > 1 and self.factor_eq(nodo_actual.izquierda) < 0:
            nodo_actual.izquierda = self.rot_izquierda(nodo_actual.izquierda)
            return self.rot_derecha(nodo_actual)

        #    • Rotación doble (der–izq)
        if balance < -1 and self.factor_eq(nodo_actual.derecha) > 0:
            nodo_actual.derecha = self.rot_derecha(nodo_actual.derecha)
            return self.rot_izquierda(nodo_actual)

        # 5. Finalmente, devolvemos el nodo actual (ya con su subárbol actualizado)
        return nodo_actual

if __name__ == "__main__":
    import datetime
    arbol = AVL()  # Usar la clase AVL, no nodoAVL
    
    # Crear fechas válidas
    date1 = datetime.date(2002, 8, 1)
    date2 = datetime.date(2002, 8, 2)
    date3 = datetime.date(2002, 8, 3)

    # Insertar valores
    arbol.insertar(date1, 24.3)
    arbol.insertar(date2, 4.3)
    arbol.insertar(date3, 40.3)
    
    print(arbol.raiz.fecha)
    print("Altura:", arbol.raiz.altura)

    date4 = datetime.date(2002, 8, 4)
    date5 = datetime.date(2002, 8, 5)
    date6 = datetime.date(2002, 8, 6)
    date7 = datetime.date(2002, 8, 7)
    arbol.insertar(date4, 41.3)
    arbol.insertar(date5, 42.3)
    arbol.insertar(date6, 46.3)
    arbol.insertar(date7, 50.3)
    
    print(arbol.raiz.fecha)
    print("Altura:", arbol.raiz.altura)
    
    # Pruebas básicas
    print("Temperatura en", date1, ":", arbol.buscar(date1))  # Debe ser 24.3
    print("Temperatura en", date2, ":", arbol.buscar(date2))  # Debe ser 4.3
    
    # Obtener rango de fechas
    fecha_min = datetime.date(2002, 8, 1)
    fecha_max = datetime.date(2002, 8, 3)
    print("\nTemperaturas en rango:", arbol.obtener_rangos(fecha_min, fecha_max))
    
    # Eliminar un nodo
    arbol.eliminar(date2)
    print("\nDespués de eliminar", date2)
    print("Temperatura en", date2, ":", arbol.buscar(date2))  # Debe ser None
    
    # Contar nodos
    print("\nTotal de nodos:", arbol.contar_nodos())  # Debe ser 2

    fecha_raiz = datetime.date(2002, 8, 4)
    if arbol.raiz.fecha == fecha_raiz:
        print("La raíz tiene la fecha esperada.")
        print(arbol.raiz.fecha, "==", fecha_raiz)
        print("Altura:", arbol.raiz.altura)
    else:
        print(arbol.raiz.fecha, "=!", fecha_raiz)
        print("La raíz NO tiene la fecha esperada.")
    """
    2002-08-01 -> raíz
    2002-08-02 -> rotación izquierda (raíz pasa a ser 02)
    2002-08-03 -> rotación izquierda (raíz pasa a ser 03)
    2002-08-04 -> rotación doble (raíz pasa a ser 04)
    2002-08-05 -> se inserta sin cambiar raíz
    2002-08-06 -> rotación izquierda (raíz sigue siendo 04)
    2002-08-07 -> rotación izquierda (raíz sigue siendo 04)
    """

    print(arbol.raiz.fecha)
    print("Altura:", arbol.raiz.altura)

#estatico: O(1) / dinamico: Búsqueda/Inserción/Eliminación en O(log n); Consultas por rango en O(k + log n); Operaciones completas (O(n))


            






 




