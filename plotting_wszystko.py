import matplotlib.pyplot as plt
import pandas as pd

path = "E:/Studia/Praca dyplomowa/kod/obrobiona_baza_danych.csv"
dane = pd.read_csv(path)    # Funkcja wczytująca bazę danych ze ścieżki "path" 
dane = dane.drop(dane.columns[[0,1]], axis = 1)
dane['timestamp'] = pd.to_datetime(dane['timestamp'], format='%Y-%m-%d %H:%M:%S')

num_data_columns = len(dane.columns) - 1

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

for i, col in enumerate(dane.columns[1:]):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(dane['timestamp'], dane[col], color=colors[i % len(colors)], alpha=0.3, s=10)  # Zmniejszenie rozmiaru punktów i ustawienie transparentności
    ax.set_xlabel('Czas')
    ax.set_ylabel(col)
    ax.set_title(f'Wykres zależności {col} od czasu')

    # Wyświetlenie wykresu
    plt.tight_layout()
    plt.show()