<<<<<<< HEAD
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
=======
import time
import matplotlib.pyplot as plt
from modulos.ListaDobleEnlazada import ListaDobleEnlazada

def generar_lde(n):
    lde = ListaDobleEnlazada()
    for i in range(n):
        lde.insertar(i, lde.tamanio)  # Inserta al final
    return lde

def medir_tiempo(metodo, *args, repeticiones=3):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        metodo(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones

# 300 tamaños de N desde 100 hasta 30,000
Ns = list(range(100, 30100, 100))
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

print("Midiendo tiempos para 300 tamaños distintos...")

for n in Ns:
    lde = generar_lde(n)

    t_len = medir_tiempo(len, lde)
    t_copiar = medir_tiempo(lde.copiar)
    t_invertir = medir_tiempo(lde.invertir)

    tiempos_len.append(t_len)
    tiempos_copiar.append(t_copiar)
    tiempos_invertir.append(t_invertir)

    print(f"N={n:<5} | len(): {t_len:.6f}s | copiar(): {t_copiar:.6f}s | invertir(): {t_invertir:.6f}s")

# Graficar los resultados
plt.figure(figsize=(14, 8))
plt.plot(Ns, tiempos_len, label='len()', linewidth=2)
plt.plot(Ns, tiempos_copiar, label='copiar()', linewidth=2)
plt.plot(Ns, tiempos_invertir, label='invertir()', linewidth=2)

plt.xlabel('Cantidad de elementos (N)', fontsize=12)
plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
plt.title('Tiempo de ejecución vs N para len(), copiar() e invertir()', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
>>>>>>> cfe0732f3cb16e623fc7fa7b721317a874582eb8
