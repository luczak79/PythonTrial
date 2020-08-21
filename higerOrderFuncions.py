def zmiennik_wiadomosci(tablica, n, akcja):
  for i in tablica:
    print(akcja(i))

zmiennik_wiadomosci([-5, 5, -6, -10], 5, abs)