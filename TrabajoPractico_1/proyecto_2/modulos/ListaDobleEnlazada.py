class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
#Funcion para hacer la lista iterable con for
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato 
            actual = actual.siguiente

    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.tamanio += 1

    def insertar(self, dato, indice):
        if indice <= 0:
            self.agregar_al_inicio(dato)
        elif indice >= self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.cabeza
            for _ in range(indice):
                actual = actual.siguiente
            anterior = actual.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self.tamanio += 1

    def extraer(self, indice=None):
        if self.tamanio == 0:
              raise Exception("Lista Vacia")

        if indice is None or indice==-1:
            dato_eliminado = self.cola.dato
            nuevo_ultimo = self.cola.anterior
            nuevo_ultimo.siguiente = None  # Desconectamos el último nodo
            self.cola = nuevo_ultimo      # Actualizamos la cola
            self.tamanio -= 1
            return dato_eliminado
                



        if indice == 0:
            extraido = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif indice >= self.tamanio - 1:
            extraido = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(indice):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            extraido = actual.dato
        self.tamanio -= 1
        return extraido

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior  # antes era siguiente, pero ya invertimos
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra):
        copia = otra.copiar()
        if not self.cabeza:
            self.cabeza = copia.cabeza
            self.cola = copia.cola
        elif copia.cabeza:
            self.cola.siguiente = copia.cabeza
            copia.cabeza.anterior = self.cola
            self.cola = copia.cola
        self.tamanio += len(copia)

    def __add__(self, otra):
        nueva = self.copiar()
        nueva.concatenar(otra)
        return nueva



