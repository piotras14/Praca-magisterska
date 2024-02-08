import pandas as pd

path = "E:/Studia/Praca dyplomowa/kod/zinterpolowana_baza_danych.csv"
dane = pd.read_csv(path) 

dane['timestamp'] = pd.to_datetime(dane['timestamp'], format='%Y-%m-%d %H:%M:%S')
dane_filtr = dane[dane['timestamp'].dt.hour == 11]
wyniki = dane_filtr[dane_filtr.iloc[:, 2] == 0]

daty_do_usuniecia = wyniki['timestamp'].dt.date.unique()
nowe_dane = dane[~dane['timestamp'].dt.date.isin(daty_do_usuniecia)]


nowe_dane.info()
zapis = "E:/Studia/Praca dyplomowa/kod/obrobiona_baza_danych.csv"
nowe_dane.to_csv(zapis, index=True)