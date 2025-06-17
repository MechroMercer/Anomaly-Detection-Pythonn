from pyod.models.knn import KNN
from pyod.models.iforest import IForest
from pyod.models.lof import LOF
from pyod.models.auto_encoder import AutoEncoder

MODEL_MAP = {
    "KNN": KNN,
    "Isolation Forest": IForest,
    "LOF": LOF,
    "AutoEncoder": AutoEncoder
}

def get_model(model_name, contamination):
   
    model_class = MODEL_MAP.get(model_name)
    if model_class:
        return model_class(contamination=contamination)
    else:
        raise ValueError(f"Nieznany model: {model_name}")

def detect_anomalies(data, model, contamination=0.1):
    
    X = data.select_dtypes(include=['number']).dropna()

    if X.empty:
        raise ValueError("Brak danych numerycznych po czyszczeniu. Nie można przeprowadzić analizy anomalii.")

    model.fit(X)
    preds = model.predict(X)

    result = data.copy()
    result['anomaly'] = preds
    return result