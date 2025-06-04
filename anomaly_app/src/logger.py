from datetime import datetime

def log_detection(model_name, contamination, num_anomalies):
    with open("detection_log.txt", "a") as f:
        f.write(f"{datetime.now()} - Model: {model_name}, Contamination: {contamination}, Anomalies: {num_anomalies}\n")