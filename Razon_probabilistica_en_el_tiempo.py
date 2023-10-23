import numpy as np
import matplotlib.pyplot as plt

# Elemento 1: Modelado de Incertidumbre
# Suponemos una serie temporal estacionaria con ruido aleatorio.
np.random.seed(0)
time = np.arange(100)
data = 10 * np.random.randn(100)  # Serie temporal con ruido

# Elemento 2: Redes Bayesianas (Opcional)
# Elemento 3: Inferencia Probabilística (Opcional)

# Elemento 4: Aprendizaje Automático Probabilístico (Opcional)
# Elemento 5: Toma de Decisiones Probabilística (Opcional)
# Elemento 6: Robustez y Adaptabilidad (Opcional)
# Elemento 7: Control y Toma de Decisiones (Opcional)

# Implementación simple de ARIMA
def arima_forecast(data, p, d, q, steps):
    history = list(data)
    predictions = []
    for _ in range(steps):
        # Realizamos una predicción simple utilizando la media móvil
        yhat = np.mean(history[-p:])
        predictions.append(yhat)
        history.append(yhat)
    return predictions

# Elemento 4: Aprendizaje Automático Probabilístico (Opcional)

# Elemento 5: Toma de Decisiones Probabilística (Opcional)

# Elemento 6: Robustez y Adaptabilidad (Opcional)

# Elemento 7: Control y Toma de Decisiones (Opcional)

# Realizamos predicciones para los próximos 10 pasos de tiempo
steps = 10
p, d, q = 10, 1, 1  # Parámetros para ARIMA
predictions = arima_forecast(data, p, d, q, steps)

# Elemento 1: Modelado de Incertidumbre
print("Elemento 1: Modelado de Incertidumbre")

# Elemento 2: Redes Bayesianas (Opcional)
# Elemento 3: Inferencia Probabilística (Opcional)

# Elemento 4: Aprendizaje Automático Probabilístico (Opcional)
print("\nElemento 4: Aprendizaje Automático Probabilístico (Opcional)")

# Elemento 5: Toma de Decisiones Probabilística (Opcional)
print("\nElemento 5: Toma de Decisiones Probabilística (Opcional)")

# Elemento 6: Robustez y Adaptabilidad (Opcional)
print("\nElemento 6: Robustez y Adaptabilidad (Opcional)")

# Elemento 7: Control y Toma de Decisiones (Opcional)
print("\nElemento 7: Control y Toma de Decisiones (Opcional)")

# Visualizamos los resultados
plt.plot(time, data, label="Serie Temporal Observada", color='blue')
plt.plot(np.arange(100, 100 + steps), predictions, label="Predicciones", color='red')
plt.legend()
plt.title("Predicción de Series Temporales con ARIMA (Implementación Simple)")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.show()
