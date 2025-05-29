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
