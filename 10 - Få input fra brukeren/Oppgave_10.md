# Leksjon 10 - Få input fra brukeren

## Oppgaver

### Oppgave 1

Lag et program som spør brukeren om hva hen heter, hvor gammel hen er og hvor
hen bor. Bruk denne informasjonen til å gi en tilbakemelding til brukeren.

### Oppgave 2

Koden under skriver en enkel meny til konsollen så lenge variabelen `kjører` er
sann. Skriv videre på koden slik at den spør brukeren om hva de ønsker å gjøre.
Hvis brukeren skriver inn 1 skal de få en liten hilsen, hvis brukeren skriver
inn 2, skal programmet gå ut av løkken.

```python
kjører = True

while kjører:
  print("Meny")
  print("-----------------")
  print("1: Få en hilsen")
  print("2: Avslutt programmet")
  print("")

  ...

print("Takk for nå")
```

**Tips:** Du trenger `input()` og en test. Står du fast kan du lese mer om denne
måten å bruke while-løkker på i leksjonen om løkker.

### Oppgave 3

Tanken med koden under er at den skal fungere som en innlogging. Vi har en
dictionary med brukernavn og pinkoder, og dersom brukeren legger inn et
matchende sett med brukernavn og pinkode, skal hen slippes inn. Dessverre
fungerer ikke koden som den skal. Dersom du forsøker å logge deg inn, vil du
nemlig aldri slippe inn.

Hva er feilen? Rett opp koden slik at den fungerer.

```python
brukere = {"Per14":1234, "Anna16":4242, "Linnea32":4321}

b_navn = input("Brukernavn: ")
pin = input("Pinkode: ")

if b_navn in brukere:
  if brukere[b_navn] == pin:
    print("Velkommen", b_navn)
  else:
    print("Feil pinkode. Vennligst prøv igjen.")
else:
  print("Bruker ble ikke funnet.")
```
