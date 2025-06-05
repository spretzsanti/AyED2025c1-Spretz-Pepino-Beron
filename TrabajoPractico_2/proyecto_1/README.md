# 🐍Sala_de_emergencia (utiliza una cola de prioridad, el cual a su ves usa el monticulo binario para implementar una cola de prioridad medica) 

Breve descripción del proyecto:

Este proyecto simula la gestión de pacientes en una sala de emergencias, priorizando la atención médica según el nivel de riesgo del paciente (crítico, moderado, bajo), si el nivel de riesgo es el mismo, entonces se despemata por orden de llegada, siendo el paciente con mas riesgo o si tienen el mismo riesgo, el que llego primero, ser el priemro en atenderse y salir de la cola.

---
## 🏗Arquitectura General

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

modules/pacientes.py: Representa a una persona, se le asigna un nombre, apellido y un nivel de riesgo (crítico, moderado, bajo). Tiene métodos para obtener su información y permite compararse con otros pacientes según prioridad y orden de llegada.

modules/monticulo.py: Implementación de un min heap, mantiene elementos ordenados de forma que el de menor valor esté en la raíz. Permite insertar elementos, eliminar el mínimo y construir el heap a partir de una lista.

modules/cola_de_prioridad.py: Envoltorio de alto nivel que utiliza monticulo.py, maneja objetos (como pacientes) con prioridad, permitiendo encolarlos y desencolarlos en orden de urgencia.

tests/test_cola_de_prioridad.py: verifica el correcto funcionamiento de cola_de_prioridad.oy

test/test_monticulo.py: verifica el correcto funcionamiento del monticulo.py

apps/sala_de_emergencia.py:  ciclo de simulación que representa la llegada y atención de pacientes, cada segundo, crea un nuevo paciente y lo encola

main.py: Es el script principal utilizado para probar interactivamente el correcto funcionamiento de todos los métodos de la clase sala_de_emergencia.py verificar la lógica de la cola de prioridad.
---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. **itertools** (`pip install itertools`)
4. **unittest**
5. **time**
6. **datetime**
7. **random**

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar dependencias:
  pip install -r requirements.txt
El archivo requirements.txtse encuentra en la carpeta deps del proyecto.
---
## 🙎‍♀️🙎‍♂️Autores

- Beron Gonzalo
- Spretz Santiago
- Pepino Pablo Jose

---
