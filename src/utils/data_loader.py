def load_csv_data(file_path):
    """Standard utility for loading HR data CSVs"""
    import pandas as pd
    return pd.read_csv(file_path)
