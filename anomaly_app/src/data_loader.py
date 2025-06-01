import pandas as pd

def load_data(file, file_type):
  if file_type == "csv":
    return pd.read_csv(file)
  elif file_type == "excel":
    return pd.read_excel(file)
  elif file_type == "json":
    return pd.read_json(file)
  else:
    raise ValueError("Unsupported file type")
