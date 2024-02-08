import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "E:/Studia/Praca dyplomowa/kod/Ostateczna_baza_danych.csv"
dane = pd.read_csv(path)    # Funkcja wczytująca bazę danych ze ścieżki "path" 
dane = dane.drop(dane.columns[[0]], axis = 1)
dane['timestamp'] = pd.to_datetime(dane['timestamp'], format='%Y-%m-%d %H:%M:%S')

dane_2007 = dane[dane['timestamp'].dt.year == 2019].copy()

# Utwórz kolumny dla godziny dnia i dnia roku
dane_2007['godzina'] = dane_2007['timestamp'].dt.hour
dane_2007['dzien_roku'] = dane_2007['timestamp'].dt.dayofyear

# Utwórz wykres 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Dane do wykresu
x = dane_2007['godzina']
y = dane_2007['dzien_roku']
z = dane_2007.iloc[:, 1]  # Zakładając, że GHI to druga kolumna

# Utworzenie siatki (grid) dla X i Y
X, Y = np.meshgrid(np.unique(x), np.unique(y))

# Utworzenie tablicy Z na podstawie wartości z dla każdego punktu w siatce X, Y
Z = np.array([dane_2007[(dane_2007['godzina']==x_val) & (dane_2007['dzien_roku']==y_val)].iloc[:, 1].mean() 
for x_val, y_val in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xticks([0, 12, 24])
ax.set_xticklabels(['00:00', '12:00', '24:00'])

ax.set_xlabel('Godzina dnia')
ax.set_ylabel('Dzień roku')
ax.set_zlabel('GHI')

plt.show()