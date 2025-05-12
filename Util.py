import pandas as pd
from Dataset import Dataset

def read_youtube_data(dataset: Dataset) -> pd.DataFrame:
    """Load the CSV and perform any initial cleaning."""
    df = pd.read_csv(dataset.value, encoding='latin1')
    df = df.dropna(subset=['subscribers', 'video views'])
    return df

