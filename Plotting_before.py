import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

path = "E:/Studia/Praca dyplomowa/kod/NEW/CasyLeon_by_stations/AV01.csv"
dane = pd.read_csv(path) 

dane['timestamp'] = pd.to_datetime(dane['timestamp'], format='%Y-%m-%d %H:%M:%S')

dane['Data'] = dane['timestamp'].dt.date

# Lista unikalnych lat
lata = sorted(dane['timestamp'].dt.year.unique())

# Tworzenie palety kolorów
colors = cm.viridis(np.linspace(0, 1, len(lata)))

liczba_kolumn = dane.shape[1]

# Iteracja przez kolumny, zaczynając od kolumny GHI (nr 3)
for kolumna in range(1, liczba_kolumn):
    # Stworzenie wykresu
    plt.figure(figsize=(15, 8))

    # Grupowanie danych dla każdego roku i wykreślanie
    for i, rok in enumerate(lata):
        # Pomiń rok 2020
        if rok == 2020:
            continue

        # Filtruj dane dla konkretnego roku
        dane_roku = dane[dane['timestamp'].dt.year == rok]
        
        # Grupuj i obliczaj średnią, tylko dla kolumn numerycznych
        srednie_dzienne = dane_roku.groupby('Data').max(numeric_only=True)

        # Zmiana roku wszystkich dat na stały rok, np. 2000
        srednie_dzienne.index = srednie_dzienne.index.map(lambda d: d.replace(year=2000))

        # Rysuj linię dla tego zestawu danych
        plt.plot(srednie_dzienne.index, srednie_dzienne.iloc[:, kolumna], label=rok, color=colors[i])

    # Dodanie pionowych linii siatki dla każdego początku miesiąca
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.gca().xaxis.grid(True, which='major', linestyle='-', linewidth=0.5)

    plt.xlabel('Miesiąc')
    plt.ylabel(f'Średnia dzienna wartość kolumny {kolumna + 1}')
    plt.title(f'Porównanie średniej dziennej wartości kolumny {kolumna + 1} w różnych latach')
    plt.legend(title='Rok')
    plt.show()