# main.py
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from data_io import cargar_dataset, limpiar_dataset
from processing import separar_variables, normalizar_minmax, split_train_test

# =========================================================
# 1) Cargar dataset
# =========================================================
RUTA = "Advertising.csv"
OBJETIVO = "Sales"

print("=== 1) CARGA DE DATOS ===")
df = cargar_dataset(RUTA)
print("Dimensiones originales:", df.shape)
print(df.head())
print("\nTipos de datos:\n", df.dtypes)

# =========================================================
# 2) Limpieza
# =========================================================
print("\n=== 2) LIMPIEZA ===")
df = limpiar_dataset(df)
print("Dimensiones despues de limpieza:", df.shape)
print(df.head())

# =========================================================
# 3) Separar X/y
# =========================================================
print("\n=== 3) SEPARAR VARIABLES ===")
X, y = separar_variables(df, OBJETIVO)
print("Features:", list(X.columns))
print("Objetivo:", OBJETIVO)

# =========================================================
# 4) Split Train/Test 70/30
# =========================================================
print("\n=== 4) SPLIT TRAIN/TEST ===")
X_train, X_test, y_train, y_test = split_train_test(X, y, test_size=0.30, random_state=42)
print("Train:", X_train.shape, "Test:", X_test.shape)

# =========================================================
# 5) Normalizacion MinMax
# =========================================================
print("\n=== 5) NORMALIZACION MIN-MAX ===")
print("Antes (train head):")
print(X_train.head())

X_train_norm, X_test_norm, scaler = normalizar_minmax(X_train, X_test)

X_train_norm_df = pd.DataFrame(X_train_norm, columns=X.columns)
X_test_norm_df  = pd.DataFrame(X_test_norm, columns=X.columns)

print("\nDespues (train head):")
print(X_train_norm_df.head())

# =========================================================
# 6) Modelo: Regresion Lineal
# =========================================================
print("\n=== 6) ENTRENAMIENTO REGRESION LINEAL ===")
modelo = LinearRegression()
modelo.fit(X_train_norm, y_train)

print("Intercepto:", modelo.intercept_)
print("Coeficientes:")
for col, coef in zip(X.columns, modelo.coef_):
    print(f"  {col}: {coef:.4f}")

# =========================================================
# 7) Prediccion y metricas
# =========================================================
print("\n=== 7) EVALUACION ===")
y_pred = modelo.predict(X_test_norm)

mse = mean_squared_error(y_test, y_pred)
rmse = (mse ** 0.5)
r2 = r2_score(y_test, y_pred)

print(f"MSE  = {mse:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"R2   = {r2:.4f}")

# =========================================================
# 8) Graficas
# =========================================================
print("\n=== 8) GRAFICAS ===")

# 8.1) Correlacion
plt.figure()
corr = df.corr(numeric_only=True)
plt.imshow(corr, aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Matriz de correlacion")
plt.tight_layout()
plt.show()

# 8.2) reales vs predichas
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Ventas reales")
plt.ylabel("Ventas predichas")
plt.title("Reales vs Predichas")
plt.grid(True)
plt.tight_layout()
plt.show()

# 8.3) residuales
resid = y_test - y_pred
plt.figure()
plt.scatter(y_pred, resid)
plt.axhline(0)
plt.xlabel("Ventas predichas")
plt.ylabel("Residual")
plt.title("Grafica de residuales")
plt.grid(True)
plt.tight_layout()
plt.show()
