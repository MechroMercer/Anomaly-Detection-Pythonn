from pyod.models.knn import KNN
from pyod.models.iforest import IForest
from pyod.models.ocsvm import OCSVM

def detect_anomalies(df, model_name='knn', contamination=0.05):
    X = df.select_dtypes(include=["float64", "int64"]).dropna()

    if model_name == 'knn':
        model = KNN(contamination=contamination)
    elif model_name == 'iforest':
        model = IForest(contamination=contamination)
    elif model_name == 'ocsvm':
        model = OCSVM(contamination=contamination)
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    model.fit(X)
    labels = model.predict(X)
    scores = model.decision_function(X)

    result_df = df.copy()
    result_df["anomaly"] = labels
    result_df["score"] = scores
    return result_df