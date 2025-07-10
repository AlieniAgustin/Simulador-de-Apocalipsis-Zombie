# 🧟‍♂️ Simulador de Apocalipsis Zombie

Una simulación interactiva del avance de una infección zombie sobre una ciudad representada como una matriz. Ideal para practicar manipulación de arrays con **NumPy** y experimentar con modelos simples de contagio.

---

## 🚀 Tecnologías usadas

- **Python 3.x**
- **NumPy**

> 💡 Opción de expansión: podés usar `matplotlib` para visualizar el avance del brote con colores (grilla animada).

---

## 📝 Enunciado del proyecto

Simulamos una ciudad en forma de matriz `NxN`, donde cada celda representa un tipo de entidad:

- `0`: Zona segura 🏠  
- `1`: Zombie 🧟  
- `2`: Humano sano 🧑  
- `3`: Hospital 🏥 (refugio inmune)

### 🧪 Reglas de la simulación:

1. La ciudad se genera aleatoriamente usando probabilidades configurables.
2. En cada turno:
   - Cada zombie infecta a los humanos **adyacentes** (arriba, abajo, izquierda, derecha).
   - Los hospitales son inmunes y bloquean el contagio.
3. La simulación se detiene cuando:
   - No quedan más humanos (`2`)
   - O se alcanza un número máximo de turnos configurado.

### 🧠 Objetivos educativos

Este proyecto fue creado para practicar:

- Creación y manipulación de arrays con NumPy.
- Slicing, broadcasting, indexado condicional y `.reshape()`.
- Simulaciones paso a paso en Python.
- Pensamiento algorítmico simple con impacto visual.

---

## 📸 Ejemplo de salida
Turno 0:
```
[[0 2 1 0]
[2 3 2 0]
[0 1 2 2]
[0 0 0 0]]
```

Turno 1:
```
[[0 1 1 0]
 [2 3 1 0]
 [0 1 1 2]
 [0 0 0 0]]
```

Turno 2:
```
[[0 1 1 0]
 [2 3 1 0]
 [0 1 1 1]
 [0 0 0 0]]
```

Turno 3:
```
[[0 1 1 0]
 [2 3 1 0]
 [0 1 1 1]
 [0 0 0 0]]
```

Turno 4:
```
[[0 1 1 0]
 [2 3 1 0]
 [0 1 1 1]
 [0 0 0 0]]
```

---

## 🧩 Ideas para expandir

- Añadir probabilidades de infección.
- Permitir movimiento de humanos.
- Visualización animada con `matplotlib`.
- Estadísticas finales: % infectados, % sobrevivientes, etc.

---

## 📂 Estructura inicial del código

- `README.md` → Este archivo.

---

## ⚠️ Requisitos

```bash
pip install numpy
