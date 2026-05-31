import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# ── PASO 1: Datos del problema ────────────────────────────────────
t = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])        # Días
h = np.array([2.5, 3.1, 4.0, 5.2, 6.8, 8.5,
              11.0, 14.2, 18.3, 23.5])                  # Alturas (cm)

# ── PASO 2: Definir el modelo exponencial ─────────────────────────
def modelo_exponencial(t, a, b):
    return a * np.exp(b * t)

# ── PASO 3: Ajustar los parámetros con curve_fit ─────────────────
params, covarianza = curve_fit(modelo_exponencial, t, h, p0=[1, 0.1])
a_opt, b_opt = params

print("=" * 45)
print("         RESULTADOS - TALLER 2")
print("=" * 45)
print(f"  Parámetro a = {a_opt:.4f}")
print(f"  Parámetro b = {b_opt:.4f}")
print(f"  Modelo ajustado: h(t) = {a_opt:.4f} · e^({b_opt:.4f}·t)")
print("=" * 45)

# ── PASO 4: Predicción en el día 12 ──────────────────────────────
dia_pred = 12
altura_pred = modelo_exponencial(dia_pred, a_opt, b_opt)
print(f"  Predicción día 12: {altura_pred:.2f} cm")
print("=" * 45)

# ── PASO 5: Graficar datos reales vs curva ajustada ───────────────
t_curva = np.linspace(1, 13, 300)
h_curva = modelo_exponencial(t_curva, a_opt, b_opt)

plt.figure(figsize=(9, 6))

# Curva ajustada
plt.plot(t_curva, h_curva, color='royalblue', linewidth=2.5,
         label=f'Curva ajustada: h(t) = {a_opt:.2f}·e^({b_opt:.2f}t)')

# Datos reales
plt.scatter(t, h, color='red', s=100, zorder=5, label='Datos reales')

# Predicción día 12
plt.scatter(dia_pred, altura_pred, color='green', s=150, zorder=5,
            marker='*', label=f'Predicción día 12: {altura_pred:.2f} cm')
plt.axvline(x=dia_pred, color='green', linestyle='--', alpha=0.5)
plt.axhline(y=altura_pred, color='green', linestyle='--', alpha=0.5)

plt.xlabel('Tiempo (días)', fontsize=12)
plt.ylabel('Altura (cm)', fontsize=12)
plt.title('Ajuste Exponencial del Crecimiento de Planta\nh(t) = a · e^(bt)', fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()