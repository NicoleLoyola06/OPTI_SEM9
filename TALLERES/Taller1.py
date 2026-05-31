import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# ── PASO 1: Definir la función de costo ──────────────────────────
def costo(vars):
    x, y = vars
    return x**2 + y**2 + 4*x + 3*y

# ── PASO 2: Ejecutar la optimización ─────────────────────────────
x0 = [0, 0]  # Punto inicial
resultado = minimize(costo, x0)

x_opt = resultado.x[0]
y_opt = resultado.x[1]
costo_min = resultado.fun

print("=" * 40)
print("       RESULTADOS - TALLER 1")
print("=" * 40)
print(f"  Valor óptimo de x (Producto A): {x_opt:.4f}")
print(f"  Valor óptimo de y (Producto B): {y_opt:.4f}")
print(f"  Costo mínimo:                   {costo_min:.4f}")
print("=" * 40)

# ── PASO 3: Graficar la función y el punto óptimo ─────────────────
x = np.linspace(-6, 2, 300)
y = np.linspace(-5, 2, 300)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2 + 4*X + 3*Y

plt.figure(figsize=(9, 6))
cp = plt.contourf(X, Y, Z, levels=40, cmap='viridis')
plt.colorbar(cp, label='Valor del Costo C(x,y)')
plt.contour(X, Y, Z, levels=40, colors='white', linewidths=0.4, alpha=0.5)

# Punto óptimo
plt.scatter(x_opt, y_opt, color='red', s=150, zorder=5,
            label=f'Punto óptimo ({x_opt:.2f}, {y_opt:.2f})')
plt.annotate(f'  Mínimo\n  C={costo_min:.2f}',
             xy=(x_opt, y_opt),
             fontsize=10, color='white',
             xytext=(x_opt + 0.5, y_opt + 0.8),
             arrowprops=dict(arrowstyle='->', color='white'))

plt.xlabel('Cantidad Producto A (x)', fontsize=12)
plt.ylabel('Cantidad Producto B (y)', fontsize=12)
plt.title('Optimización de Costo de Producción\nC(x,y) = x² + y² + 4x + 3y', fontsize=13)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()