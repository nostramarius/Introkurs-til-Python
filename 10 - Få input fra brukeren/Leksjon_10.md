# Leksjon 10 - Få input fra brukeren

I mange typer programmer ønsker vi at brukeren av programmet skal kunne legge
inn sin egen informasjon. For å få til dette i Python, bruker vi funksjonen
`input()`. Et eksempel på dette kan være:

```python
print("Hva heter du?")

navn = input()

print("Hei", navn)
```

Koden over vil først printe "Hva heter du?" til konsoll. På neste linje vil
programmet vente til brukeren har lagt inn sin input og trykker `ENTER`. Til
slutt skrives en kort hilsen med den inputen brukeren la inn.

`input()` kan også ta en tekst-string som argument. Denne teksten vil da skrives
til konsoll, og brukerinputen vil legges inn på slutten av denne teksten. Et
eksempel på dette er:

```python
navn = input("Hva heter du? ")

print("Hei", navn)
```

## All input er tekst

All informasjon som kommer inn i programmet gjennom `input()` blir lagt inn som
tekst (str). Dersom det er et tall brukeren skal legge inn, må dette gjøres om
til heltall (int), før det kan brukes til f.eks. utregninger. For å gjøre dette
kan du bruke funksjonen `int()`.

```python
alder = input("Hvor gammel er du? ")

alder = int(alder)    # Her gjør vi om variabelen alder fra tekst til heltall

alder_om_to_år = alder + 2

print("Om to år er du", alder_om_to_år, "år gammel.")
```
