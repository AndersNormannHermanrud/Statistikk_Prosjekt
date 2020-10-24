# importere pakker og funksjoner vi trenger i oppgave 1

# generelt - numerikk og nyttige funksjoner
import numpy as np
import pandas as pd

# plotting
import matplotlib.pyplot as plt
import seaborn as sns

# Fordelinger, modeller for regresjon, qq-plott
from scipy import stats
import statsmodels.formula.api as smf
import statsmodels.api as sm

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.ast_node_interactivity = "last_expr"
if __name__ == '__main__':
    # Lese inn datasettet ved funksjon fra pandas  (df=data frame - vanlig navn å gi et datasett)
    df = pd.read_csv("https://www.math.ntnu.no/emner/IST100x/ISTx1003/Idrett.csv", sep=',')
    df.sort_values(by=['Hoeyde'], inplace=True)  # alt sortert på Hoeyde, bare for gøy

    # Skriv ut de første og siste radene
    print(df)

    # Konverter kjønn og idrettsgren til kategory
    df = df.astype({'Kjoenn': 'category', 'Sport': 'category'})
    print(df["Kjoenn"].value_counts())
    print(df["Sport"].value_counts())
    # kodechunk Steg2-4

    # Steg 2: spesifiser matematisk modell
    formel = 'Blodceller ~ Hoeyde'

    # Steg 3: Initaliser og tilpass en enkel lineær regresjonsmodell
    # først initialisere
    modell = smf.ols(formel, data=df)
    # deretter tilpasse
    resultat = modell.fit()

    # Steg 4: Presenter resultater fra den tilpassede regresjonsmodellen
    print(resultat.summary())