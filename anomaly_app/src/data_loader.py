import pandas as pd

def load_data(file, file_type):
    if file_type == 'csv':
        return pd.read_csv(file)
    elif file_type in ['xls', 'xlsx']:
        return pd.read_excel(file)
    elif file_type == 'json':
        return pd.read_json(file)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")