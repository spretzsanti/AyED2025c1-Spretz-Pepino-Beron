from modules.Listadobleenlazada import listadoble

lista = listadoble()
lista.mostrar()
#print(lista.esta_vacia())
lista.agregar_al_final(5)
lista.agregar_al_final(0.4)
lista.agregar_al_final("a")
lista.mostrar()
#print(lista.esta_vacia())
print(lista._len_())