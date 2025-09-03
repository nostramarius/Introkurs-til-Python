# Leksjon 10 - Få input fra brukeren

## Løsningsforslag til oppgaver

### Oppgave 1

```python
print("Hva heter du?")
navn = input(": ")
print("Hei " + navn + "! Hyggelig å møte deg.")

print("Hvor gammel er du?")
alder = input(": ")
print("Det betyr at du er", int(alder)+3, "år gammel om 3 år.")

print("Hvor bor du?")
sted = input(": ")
print(sted, "høres ut som et fint sted!")
```

### Oppgave 2

```python
kjører = True

while kjører:
  print("Meny")
  print("-----------------")
  print("1: Få en hilsen")
  print("2: Avslutt programmet")
  print("")

  valg = input(": ")
  if valg == "1":
    print("Hei på deg!")
    print("")
  elif valg == "2":
    kjører = False
  else:
    print("Vennligst velg et av alternativene i menyen.")
    print("")

print("")
print("Takk for nå")
```

### Oppgave 3

Feilen i koden er at variabelen `pin` lagrer det brukeren legger inn som tekst,
mens den sjekkes mot et tall (int) i dictionaryen. De vil derfor aldri være
like. For å rette opp i dette, må vi gjøre om innholdet i `pin` til heltall.
Dette gjør vi med funksjonen `int()`. Her har vi pakket hele `input("Pinkode")`
inn i `int()`-funksjonen, slik at dette gjøres med en gang brukeren legger inn
koden sin.

Et alternativ til dette kunne vært å skrive `if brukere[b_navn] == int(pin):` i
testen som sjekker om brukernavn og pinkode hører sammen. Dette ville gitt samme
resultat og løst problemet.

```python
brukere = {"Per14":1234, "Anna16":4242, "Linnea32":4321}

b_navn = input("Brukernavn: ")
pin = int(input("Pinkode: "))

if b_navn in brukere:
  if brukere[b_navn] == pin:
    print("Velkommen", b_navn)
  else:
    print("Feil pinkode. Vennligst prøv igjen.")
else:
  print("Bruker ble ikke funnet.")
```
