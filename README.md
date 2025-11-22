📌 Descripción del Proyecto

Este repositorio contiene la Actividad Fundamental 6 de la materia Programación para Inteligencia Artificial.
El objetivo es implementar un modelo de aprendizaje supervisado utilizando el algoritmo de Regresión Lineal, aplicando:

Carga y análisis del dataset

Preprocesamiento y limpieza

Normalización con MinMaxScaler

División del dataset (Train/Test)

Entrenamiento del modelo

Evaluación con métricas de regresión

Visualización de resultados

Desarrollo en un entorno virtual de Anaconda

Arquitectura modular en Python

📊 Dataset utilizado

Advertising Dataset
Archivo: Advertising.csv

Contiene 200 registros con inversión publicitaria en:

TV

Radio

Newspaper

Y la variable objetivo:

Sales (ventas)

Este dataset es ideal para tareas de regresión supervisada.

🧠 Modelo seleccionado
✔️ Regresión Lineal

Implementado con:

from sklearn.linear_model import LinearRegression

✔️ Razones para elegirlo:

Es un modelo supervisado clásico

Fácil de interpretar

Excelente para relaciones lineales

Dataset pequeño y limpio

Totalmente adecuado para la AF6

📁 Estructura del proyecto
AF6/
│
├── main.py
├── data_io.py
├── processing.py
├── Advertising.csv
└── README.md

Archivo	Descripción
main.py	Controla todo el flujo (modelo, gráficas, métricas)
data_io.py	Carga, limpieza y exploración del dataset
processing.py	Normalización y separación de datos
Advertising.csv	Dataset empleado
README.md	Documentación del proyecto
🛠️ Requisitos del entorno

Entorno recomendado (Anaconda):

conda create -n af6 python=3.11 -y
conda activate af6


Instalar dependencias:

conda install numpy pandas scikit-learn matplotlib openpyxl spyder -y

▶️ Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/tu-usuario/AF6


Activar el entorno:

conda activate af6


Abrir Spyder desde ese entorno:

spyder


En Spyder:

Abrir main.py

Verificar que el Working Directory sea la carpeta AF6

Ejecutar con F5

📈 Resultados obtenidos

El proyecto genera:

📌 Matriz de correlación

Relación entre variables de entrada y la salida (Sales).

📌 Gráfica Reales vs Predichas

Demuestra qué tan bien ajusta el modelo.

📌 Gráfica de Residuales

Verifica el comportamiento del error.

📌 Métricas del modelo
Métrica	Valor
MSE	3.79
RMSE	1.95
R²	0.86

El modelo logra explicar el 86% de la variabilidad de las ventas.

🧩 Conclusiones del equipo

La Regresión Lineal resultó eficiente para este conjunto de datos.

La normalización mejoró la estabilidad numérica del modelo.

La estructura modular permitió un desarrollo más claro y mantenible.

Las métricas obtenidas confirman que el modelo generaliza correctamente.

El uso de un entorno virtual garantiza reproducibilidad y organización del proyecto.
