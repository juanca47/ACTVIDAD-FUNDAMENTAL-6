# data_io.py
import pandas as pd

def cargar_dataset(ruta_csv):
    df = pd.read_csv(ruta_csv)
    return df

def limpiar_dataset(df):
   
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])


    df = df.drop_duplicates()

    
    df = df.dropna()

    return df
