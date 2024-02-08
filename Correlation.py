import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# from yellowbrick.style import set_palette
# set_palette("flatui")

path = "E:/Studia/Praca dyplomowa/kod/obrobiona_baza_danych.csv"
dane = pd.read_csv(path)    # Funkcja wczytująca bazę danych ze ścieżki "path" 
dane = dane.drop(dane.columns[[0,1]], axis = 1)
dane = dane[(dane[['GHI']]!= 0).any(axis=1)]
dane.info()


# dane.info()                 # Funkcja wyświetlająca podstawowe informacje o wczytanych danych
# braki = dane[dane.isnull().any(axis=1)]
# print(braki.to_string())
# index = dane.to_datetime([])

# Interpolowanie brakujących wartości
# dane.interpolate(method="linear", inplace=True)
# dane.bfill(axis ='rows', inplace=True) 
# dane = dane.round(2)

zapis = "E:/Studia/Praca dyplomowa/kod/Ostateczna_baza_danych.csv"
dane.to_csv(zapis, index=False)
# dane.info()

# dane_filtr = dane[dane['timestamp'].dt.hour == 13]
# wyniki = dane_filtr[dane_filtr.iloc[:, 2] == 0]

plt.figure(figsize=(18,8))
corr_matrix = dane.corr(numeric_only=True)
paleta_barw = sns.color_palette("coolwarm", as_cmap=True)
sns.heatmap(corr_matrix, annot=True, cmap=paleta_barw, vmin=-1, vmax=1)
plt.title("Macierz Korelacji")
plt.show()