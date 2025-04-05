
# Repositorio: Predicción de Bancarrota con Machine Learning y Azure

Este repositorio contiene un pipeline completo para entrenar, desplegar y consumir un modelo de machine learning que predice si una empresa está en riesgo de bancarrota, usando datos financieros.

---

## Estructura del Repositorio

```
├── Model.ipynb               # Entrenamiento del modelo (XGBoost + Logistic Regression)
├── Deployer.ipynb            # Despliegue del modelo en Azure como servicio web
├── API.ipynb                 # Consumo de la API para hacer inferencias con nuevos datos
├── score.py                  # Script de inferencia usado en el despliegue
├── model_bankruptcy.pkl      # Modelo entrenado serializado
├── umbral_bankruptcy.json    # Umbral dinámico para clasificar predicciones
├── uri.json                  # Endpoint generado al desplegar el modelo
├── prueba.csv                # Datos de prueba sin la columna 'Bankrupt?'
├── README.md                 # Instrucciones detalladas de uso
```

---

## Archivos clave

### `Model.ipynb`
Entrena un modelo XGBoost con regresión logística y guarda:
- `model_bankruptcy.pkl`
- `umbral_bankruptcy.json`

### `Deployer.ipynb`
Despliega el modelo en Azure usando Azure ML SDK y genera:
- `score.py`
- `uri.json`

### `API.ipynb`
Envía un archivo `.csv` al servicio web para obtener predicciones. Usa:
- `uri.json` para conocer la dirección del endpoint
- `prueba.csv` como ejemplo de datos de entrada

---

## Requisitos

- Python 3.10+
- Azure ML SDK
- pandas
- scikit-learn
- xgboost
- requests
- Una cuenta de Azure activa

---

## Dataset original

[Kaggle - Company Bankruptcy Prediction](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction)

---

## Licencia

Este proyecto es únicamente con fines educativos para el curso de Cloud Computing (MA3001B).

---
