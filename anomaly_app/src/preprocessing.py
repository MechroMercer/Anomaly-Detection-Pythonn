import pandas as pd
def drop_missing_values(df):
    return df.dropna()

def convert_categorical(df):
    return pd.get_dummies(df, drop_first=True)