class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listadoble():
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def esta_vacia(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def _len_(self):
        count = 0
        actual = self.cabeza
        while actual is not None:
            count += 1
            actual = actual.siguiente
        return count

    def insertar(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        
        if posicion == "":
            posicion = None

        if posicion is None:
            self.agregar_al_final(dato)
            return
        
        posicion=int(posicion)# esto evita que el isinstance tire valueerror, pero falla si ingresamos una posicion como "a"        
        # Verificar que la posición sea un entero no negativo
        if not isinstance(posicion, int) or posicion < 0:
            raise ValueError("Posición inválida: debe ser un entero no negativo.")    
        if posicion > self._len_():
            raise IndexError("Posición inválida: excede la longitud de la lista.")

        elif posicion == 0:
            self.agregar_al_inicio(dato)

        else:
            actual = self.cabeza
            indice = 0
            while indice < posicion:
                actual = actual.siguiente
                indice += 1
            nodo_anterior = actual.anterior
            nodo_anterior.siguiente = nuevo_nodo  # El nodo anterior apunta ahora al nuevo nodo
            nuevo_nodo.anterior = nodo_anterior     # El nuevo nodo apunta de regreso al nodo anterior
            nuevo_nodo.siguiente = actual            # El nuevo nodo apunta al nodo que se desplazará a la derecha
            actual.anterior = nuevo_nodo               # El nodo que estaba en 'actual' actualiza su puntero anterior
    
    def extraer(self, posicion):
        # Verificar que la posición sea un entero no negativo
        if not isinstance(posicion, int) or posicion < 0:
            raise ValueError("Posición inválida: debe ser un entero no negativo.")    
        if posicion > self._len_():
            raise IndexError("Posición inválida: excede la longitud de la lista.")
        # Verificar que la lista no esté vacía.
        if self.cabeza is None:
            raise IndexError("La lista está vacía, no se puede eliminar ningún elemento.")
        
        # Calcular la longitud de la lista para validar la posición.
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        # Caso 1: Eliminar el primer nodo (posición 0)
        if posicion == 0:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente  # La cabeza se mueve al siguiente nodo
            if self.cabeza:  # Si la lista no queda vacía
                self.cabeza.anterior = None
            else:
                # Si la lista queda vacía, también se actualiza la cola
                self.cola = None
            return nodo_eliminado.dato

        # Caso 2: Eliminar un nodo en posición intermedia o el último
        nodo_actual = self.cabeza
        indice = 0
        # Recorremos la lista hasta el nodo a eliminar
        while indice < posicion:
            nodo_actual = nodo_actual.siguiente
            indice += 1

        # 'nodo_actual' es el nodo que se va a eliminar
        nodo_eliminado = nodo_actual

        # Caso 2.1: Si se trata del último nodo
        if nodo_actual.siguiente is None:
            # Actualizamos la cola para que sea el nodo anterior
            self.cola = nodo_actual.anterior
            self.cola.siguiente = None
        else:
            # Caso 2.2: Nodo en posición intermedia
            # Se conecta el nodo anterior con el siguiente del nodo a eliminar
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior

        # Se retorna el dato contenido en el nodo eliminado
        return nodo_eliminado.dato
