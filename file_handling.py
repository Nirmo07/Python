import pandas as pd
from exception import DataCleaningError

def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Loaded DataFrame from CSV:")
        print(df.head())
        return df
    except FileNotFoundError as e:
        raise DataCleaningError(f"File not found: {filepath}") from e

def save_csv(df, filepath):
    try:
        df.to_csv(filepath, index=False)
        print(f"DataFrame successfully saved to {filepath}")
    except Exception as e:
        raise DataCleaningError(f"Failed to save file: {filepath}") from e
