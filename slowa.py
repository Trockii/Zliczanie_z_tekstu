import sys
import codecs
import re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

tekst = open("tekst.txt", "r", encoding="utf-8")
zawartosc = tekst.read().lower()
zawartosc = re.sub(r'[^\w\s]', '', zawartosc)
slowa = zawartosc.split()


licznik = {}
for slowo in slowa:
    if slowo in licznik:
        licznik[slowo] +=1
    else:
        licznik[slowo] = 1

szukane_slowo = input("wpisz słowo: ")

if szukane_slowo in licznik:
    print(f"słowo '{szukane_slowo}' występuje {licznik[szukane_slowo]} razy.")
else:
    print(f"niestety słowo '{szukane_slowo}' nie występuje w tekście.")