# 🐍Nombre del proyecto (Juego de cartas: Guerra) 

Trabajo Práctico Nº1, Aplicaciones de TADs

Breve descripción del proyecto:

Ejemplo: “Este es un script en el que se comparan algoritmos de ordenamiento. Permite crear y barajar un mazo completo de 52 cartas, repartirlo entre dos jugadores, y simular turnos donde cada uno revela cartas para determinar un ganador basado en su valor numérico. En caso de empate, inicia guerras con cartas adicionales. Todo esto se gestiona mediante listas doblemente enlazadas.

---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)

La carpeta deps almacena las extensiones descargas en requirements.txt

La carpeta modulos contiene los modulos utilizados en el proyecto:

   * clase Carta: modela una carta de baraja con atributos como valor, palo y visibilidad. Permite convertir el valor de la carta a un número para comparaciones
   * clase JuegoGuerra: Implementa la lógica completa del juego de cartas 'Guerra'. Permite crear y barajar un mazo, repartir cartas entre dos jugadores, simular turnos con enfrentamientos de cartas
   * clase listadoble: define una lista doblemente enlazada básica que permite agregar nodos al inicio o final, verificar si está vacía, mostrar su contenido y obtener su tamaño
   * clase Mazo: modela un mazo de cartas usando una lista doblemente enlazada personalizada. Permite operaciones como poner/sacar cartas de arriba o abajo, verificar si el mazo está vacío, y mostrar sus cartas

La carpeta test contiene los test utilizados para evaluar el correcto funcionamiento del codigo:

   * clase ... 

* clase ...

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

* Beron Gonzalo
* Spretz Santiago
* Pepino Pablo

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
