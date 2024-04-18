import pandas as pd
def analisis_estadisticos(lista):
    df = pd.read_csv(lista)

    df["Fi"] = df["fi"].cumsum()
    df["fr"]  = df["fi"] / df["fi"].sum()
    df["Fr"] = df["fr"].cumsum()
    df["pi%"] = df["fr"] * 100
    df["Pi%"] = df["Fr"] * 100

    df.to_clipboard()
    print(df)

analisis_estadisticos("edades-30Alumnos.csv")

