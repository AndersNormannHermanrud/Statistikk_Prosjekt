# importere pakker og funksjoner vi trenger i oppgave 3
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg # hvis du skal lese eget bilde

from sklearn.datasets import load_sample_image # lese inn bilder fra denne modulen
from sklearn.cluster import KMeans # k-gjennomsnitt klyngeanalyse

if __name__ == '__main__':
    # kodechunk lasteinnbilde

    # Vi laster inn bildet china.jpg
    # Du kan endre filnavn hvis du vil ha ditt eget bilde
    filnavn = 'china.jpg'
    bilde = load_sample_image(filnavn)


    # Vi lager en enkel funksjon som viser bilder på skjermen
    def vis_bilde(bilde, bildetekst):
        ax = plt.axes(xticks=[], yticks=[])
        ax.set_title(bildetekst, size=16)
        ax.imshow(bilde);
        plt.show()


    #vis_bilde(bilde, filnavn)
    # kodechunk blikjent

    # hvilken type er bildet vårt
    print("Bildet har type", type(bilde))

    # bildet er en numpytabell. Hva er formatet?
    print("Formatet til tabellen er", bilde.shape)

    # vi ser på pixel i posisjon (20,10) i bildet
    print("Pixel (10,20) har verdi [R,G,B] =", bilde[10, 20])
    print("En farge har type", type(bilde[10, 20, 0]))

    # Vi henter ut informasjonen om formatet for bruk senere
    bilde_rader, bilde_kolonner, ant_farger = bilde.shape
    bilde_piksler = bilde_rader * bilde_kolonner

    print("Antall rader i bildet er", bilde_rader)
    print("Antall kolonner i bildet er", bilde_kolonner)
    print("Antall piksler i bildet er", bilde_piksler)
    print("Antall fargeverdier per pixel er", ant_farger)
    # kodechunk endreformatbilde

    # Skalar bildet til flyttal mellom 0.0 og 1.0
    data_farger = bilde / 255

    # Vi endrer formatet på dataene til (antall piksler, antall farger)
    data_farger = data_farger.reshape(bilde_rader * bilde_kolonner, ant_farger)

    # Vi ser på formatet til datene
    print("Det nye formatet for dataene er", data_farger.shape)
    print("Typen til en farge er nå", type(data_farger[10, 0]))
    print(bilde[10,20]/255)
    print(data_farger[6420])