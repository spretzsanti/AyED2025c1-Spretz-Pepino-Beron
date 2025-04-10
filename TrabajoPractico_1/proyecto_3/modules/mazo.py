# mazo.py

from modulos.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    
    #Cambiar por ListaDobleEnlazada de ejercicio 2, y cpz que tendria que ser privado
    class Nodo():
        def __init__(self,carta,anterior,siguiente):
            self.carta = carta
            self.anterior = anterior
            self.siguiente = siguiente
            

 #Constructor de Mazo
    def __init__(self):
            self.inicio = None
            self.final = None
            self.tamañio = 0
            
    def __len__(self):
        return self.tamañio
    
  
    def vacio(self):
        if self.tamañio == 0:
            return True
        else:
            return False
        
        
    #Le tenes que pasar la carta a poner
    def poner_carta_arriba(self,carta):
        #Cada nodo (Carta, Anterior, Siguiente)
        #Este nodo apunta al que era el inicio ya que antes no tiene nada porque es la primera y le sigue la que era primera antes
        Nodo_nuevo = self.Nodo(carta,None,self.inicio)
        if self.vacio() == True:
            self.final = Nodo_nuevo #Inicio y final son el mismo, re filosofico 
        else:
            #La carta que antes estaba primera ahora tiene una antes que es la nueva
            self.inicio.anterior = Nodo_nuevo
            
        self.inicio = Nodo_nuevo #La carta nueva es el inicio porque se puso arriba
        self.tamañio += 1 #Se agrego una carta +1 en el tamaño del mazo
        
    def sacar_carta_arriba(self):
        if self.vacio() == True:
            raise DequeEmptyError("No hay cartas en el mazo maestro")
        
        #Primera carta
        carta_sacada = self.inicio.carta
        #El inicio es ahora la que estaba despues
        self.inicio = self.inicio.siguiente
        #Tamaño menos uno
        self.tamañio -=1
        if self.vacio() == True:
            self.final = None #Si el mazo quedo vacio por sacar la carta no hay final
        else:
            self.inicio.anterio = None #Ajuste del nuevo inicio
            
        return carta_sacada
    
    #Como poner carta arriba pero al reves
    def poner_carta_abajo(self,carta):
        Nuevo_nodo = self.Nodo(carta,self.final,None)
        if self.vacio() == True:
            self.final = Nuevo_nodo 
        else:
            self.final.siguiente = Nuevo_nodo
        
        self.final = Nuevo_nodo
        self.tamañio +=1
        
    
            
            
            
        
        
            
            
        
