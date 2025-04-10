from modules.Listadobleenlazada import listadoble

lista = listadoble()
lista.mostrar()
#print(lista.esta_vacia())
lista.agregar_al_final(5)
lista.agregar_al_final(0.4)
lista.agregar_al_final("a")
lista.mostrar()
#print(lista.esta_vacia())
<<<<<<< HEAD
print(lista._len_())
=======
print(lista._len_())
a = input("escribi la posicion: ")
#lista.insertar(900,a)
print(lista.extraer(int(a)))
lista.mostrar()
>>>>>>> 5b8907c (seguimos el trabajo del problema 2, insertar y extraer)
