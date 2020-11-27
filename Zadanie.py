#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przedmiot: Informatyka
# Kierunek studiów: Mechanika i budowa Maszyn
# Semestr: zimowy
# Rok akademicki: 2020/2021
# Data (dzień.miesiąc.rok): 1.11.2020
# Imię: Marcin
# Nazwisko: Krzewiniak
# Numer albumu ZUT: 49566

stringinput1 = input()

znaki = {'a':'(a)', 'e': '(e)', 'o': '(o)', 'y': '(y)', 'i': '(i)', 'u': '(u)', 'A': '(A)', 'E': '(E)', 
         'O': '(O)', 'U':'(U)', 'Y':'(Y)', 'ę':'(ę)', 'ą':'(ą)', 'ó':'(ó)', }

res = ''.join(idx if idx not in znaki else znaki[idx] for idx in stringinput1) 

print(str(res))


# program należy resetować po każdym użyciu.
