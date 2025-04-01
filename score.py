
import json
import numpy as np
import pandas as pd
import joblib
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('model')
    model = joblib.load(model_path)  # (xgb_model, logistic_model)
    global xgb_model, logistic_model
    xgb_model, logistic_model = model

def run(raw_data):
    try:
        data = json.loads(raw_data)['data'][0]
        df = pd.DataFrame(data)

        # Obtener probabilidades de XGBoost
        xgb_probs = xgb_model.predict_proba(df)[:, 1].reshape(-1, 1)

        # Aplicar regresión logística sobre las probabilidades
        final_probs = logistic_model.predict_proba(xgb_probs)[:, 1]

        # Aplicar umbral dinámico
        umbral = 0.12225308317350525
        final_preds = [1 if p > umbral else 0 for p in final_probs]

        return json.dumps(final_preds)

    except Exception as e:
        return json.dumps(str(e))
