# 🐍Temperaturas_DB: Base de Datos Climáticos con Árbol AVL

Breve descripción del proyecto:

Este proyecto implementa "Temperaturas_DB", una base de datos en memoria diseñada para gestionar eficientemente mediciones de temperatura. Utiliza internamente un árbol AVL para asegurar un rendimiento óptimo (logarítmico para la mayoría de las operaciones) en la inserción, búsqueda, eliminación y consulta de datos climáticos.Cada medición almacenada consiste en un valor de temperatura expresado en grados Celsius (°C) y su correspondiente fecha de registro en formato "dd/mm/aaaa".

---
## 🏗Arquitectura General

* `modules/AVL.py` Contiene la implementación genérica y reutilizable de la estructura de datos Árbol AVL auto-balanceable. Esta clase maneja la lógica de nodos, rotaciones, inserciones, eliminaciones y búsquedas balanceadas.
* `modules/temperatura_db.py`: Implementa la clase `Temperaturas_DB`. Esta clase actúa como una fachada, utilizando una instancia del árbol AVL para almacenar y gestionar los datos de temperatura, y expone la interfaz de operaciones descrita anteriormente.
* `main.py`: Es el script principal utilizado para probar interactivamente el correcto funcionamiento de todos los métodos de la clase `Temperaturas_DB` permitiendo verificar la lógica de la base de datos.


---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)


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

- Spretz Santiago
- Pepino Pablo
- Veron Gonzalo

---

