import pandas as pd
from exceptions import DataCleaningError

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        raise DataCleaningError(f"File not found: {file_path}") from e

def save_csv(df, file_path):
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        raise DataCleaningError(f"Failed to save file: {file_path}") from e
