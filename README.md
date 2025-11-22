📘 Actividad Fundamental N.º 6 – Modelo Supervisado en Python
🎯 Descripción General

Este repositorio corresponde a la Actividad Fundamental N.º 6 de la materia Programación para Inteligencia Artificial (FIME – UANL).
El objetivo es implementar un modelo de aprendizaje supervisado utilizando Regresión Lineal aplicado al dataset Advertising, siguiendo un enfoque modular y reproducible dentro de un entorno virtual de Anaconda.

El sistema implementado incluye:

Lectura y limpieza del dataset Advertising.csv.

Normalización de características mediante MinMaxScaler.

División del dataset en conjuntos Train / Test (70% / 30%).

Entrenamiento del modelo de Regresión Lineal (LinearRegression).

Cálculo de métricas de desempeño: MSE, RMSE y R².

Generación de gráficas: matriz de correlación, reales vs predichas, residuales.

Uso de un entorno virtual para mantener el proyecto ordenado y reproducible.

1. 🧩 Estructura Modular del Código

El proyecto se dividió en tres módulos principales, siguiendo las buenas prácticas vistas en clase y el estilo de trabajo requerido en las Actividades Fundamentales:

Archivo	Responsabilidad Principal
main.py	Flujo de Control. Ejecuta el proyecto completo: carga, normalización, entrenamiento, evaluación y visualización del modelo.
data_io.py	Entrada y Limpieza de Datos. Contiene la lógica para cargar el dataset, explorar las columnas, eliminar duplicados y limpiar información.
processing.py	Procesamiento y Transformaciones. Implementa la normalización con MinMaxScaler y la división Train/Test.
2. 🛠️ Instalación y Entorno (af6)

El proyecto fue desarrollado en un entorno virtual creado con Anaconda utilizando Python 3.11.

🔹 1. Clonar el repositorio
git clone https://github.com/tu-usuario/AF6
cd AF6

🔹 2. Crear y activar el entorno virtual
conda create -n af6 python=3.11 -y
conda activate af6

🔹 3. Instalar dependencias necesarias
conda install numpy pandas scikit-learn matplotlib openpyxl spyder -y

3. ▶️ Ejecución del Proyecto

Una vez activado el entorno y abierto Spyder, basta con ejecutar:

spyder


Luego:

Abrir main.py

Asegurar que el Working Directory corresponde a la carpeta del proyecto

Ejecutar con F5

El programa:

Carga el dataset

Limpia y normaliza los datos

Entrena el modelo

Evalúa su rendimiento

Genera gráficas y métricas en consola

📦 Salida del modelo

El programa imprime:

Coeficientes del modelo

MSE

RMSE

R²

Y genera 3 visualizaciones clave:

Matriz de correlación

Reales vs predichas

Residuales

Ejemplo de resultados obtenidos:

MSE: 3.79

RMSE: 1.95

R²: 0.86

🧠 Conclusiones

Este proyecto demuestra la implementación correcta de un modelo supervisado con Python siguiendo una estructura modular.
Se cumplieron los objetivos de la AF6:

Aplicación del preprocesamiento de datos

Normalización de características

Entrenamiento de un modelo supervisado

Evaluación mediante métricas estándar

Uso de un entorno virtual con Anaconda

Control de versiones mediante Git y GitHub

El modelo de regresión lineal ofreció un rendimiento destacado, explicando aproximadamente el 86% de la variabilidad de las ventas. Las gráficas generadas permitieron analizar el comportamiento del modelo y validar su adecuación al dataset empleado.
