#import polskich znaków w konsoli
import sys
import codecs
import re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

#tworzenie zmiennych
tekst = open("tekst.txt", "r", encoding="utf-8") #połączenie tekstu zewnętrznego
zawartosc = tekst.read().lower() #połączenie tekstu zewnętrznego
zawartosc = re.sub(r'[^\w\s]', '', zawartosc) #ta linia umożliwia aby słowa mogły zaczynać się z małej lub dużej
slowa = zawartosc.split() #rodzielamy słowa

#dodajemy licznik do każdego podzielnego słowa, jeśli pojawia się drugi raz, dodaj +1
licznik = {}
for slowo in slowa:
    if slowo in licznik:
        licznik[slowo] +=1
    else:
        licznik[slowo] = 1

szukane_slowo = input("wpisz słowo: ") #input na wpisanie słowa którego użytkownik potrzebuje

#print który wyświetla słowo oraz jego liczebność w tekscie, dodatkowo odpowiedz zwrotna, gdyby słowa miało nie być
if szukane_slowo in licznik:
    print(f"słowo '{szukane_slowo}' występuje {licznik[szukane_slowo]} razy.")
else:
    print(f"niestety słowo '{szukane_slowo}' nie występuje w tekście.")