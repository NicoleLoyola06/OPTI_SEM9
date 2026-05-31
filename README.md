# Optimización y Simulación de Sistemas
### Sesión 9 — Librería Python SciPy

**Autora:** Andrea Nicole Loyola Mendoza  
**Asignatura:** Optimización y Simulación de Sistemas  
**Docente:** Mg. Huerta Rojas, Miguel Angel

## Descripción
Este repositorio contiene la solución de los talleres desarrollados
en la Sesión 9, enfocados en el uso de la librería SciPy de Python
para resolver problemas de optimización y ajuste de curvas.


## Talleres

### Taller 1 — Optimización de Costos en Producción
Minimización de la función de costo C(x,y) = x² + y² + 4x + 3y
usando `scipy.optimize.minimize`, con visualización mediante
un mapa de calor que muestra el punto óptimo encontrado.

### Taller 2 — Ajuste de Curva para Predicción de Crecimiento
Ajuste de un modelo exponencial h(t) = a·e^(bt) a datos reales
de crecimiento de una planta usando `scipy.optimize.curve_fit`,
con predicción de la altura en el día 12.

---

## Librerías utilizadas
- scipy
- numpy
- matplotlib

## Instalación
pip install scipy numpy matplotlib

---

## Resultados
Los gráficos generados se guardan automáticamente en la
carpeta /RESULTADOS al ejecutar cada script.
