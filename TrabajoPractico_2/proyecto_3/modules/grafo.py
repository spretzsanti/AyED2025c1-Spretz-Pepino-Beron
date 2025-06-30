from modules.vertice import Vertice

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0


    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    
    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        # Conexión bidireccional
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
        self.listaVertices[a].agregarVecino(self.listaVertices[de], costo)
    
    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __len__(self):#metodo necesario para usar el len en el test
        return self.numVertices 
