# 🐍Nombre del proyecto (Analisis de algortmos de ordenamiento) 
# Trabajo Práctico Nº1, Aplicaciones de TADs

Breve descripción del proyecto:

Este es un script en el que se comparan algoritmos de ordenamiento. Permite generar listas de números aleatorios y ordenarlas utilizando tres algoritmos distintos: Bubble Sort, Quick Sort y Radix Sort, además de comparar sus resultados con la función nativa sorted() de Python.
---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)

La carpeta deps almacena las extensiones descargas en requirements.txt

La carpeta modules contiene los modulos utilizados en el proyecto:
   * clase BubbleSort: Este script implementa y prueba el algoritmo de ordenamiento Bubble Sort con una lista de números aleatorios.
   * clase Quicksort: Este script implementa y prueba el algoritmo Quicksort con una lista de números aleatorios.
   * clase Radix_sort: Este script implementa y prueba el algoritmo Radix Sort (ordenamiento por raíz) para ordenar números enteros.

La carpeta test contiene los test utilizados para evaluar el correcto funcionamiento del codigo:
   en este caso no se usa porque es evaluado con las fuciones de python
* clase main: que ejecuta los algoritmos de ordenamiento y realiza una grafica comparativa

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
- Beron Gonzalo
- Spretz Santiago
- Pepino Pablo
---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
