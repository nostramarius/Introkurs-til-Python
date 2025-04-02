# Leksjon 7 - Løkker

Løkker brukes for å gjenta noe i kode. Dette er nyttig hvis du for eksempel har
en liste og ønsker å printe alle tingene i listen hver for seg, du ønsker å
gjenta noe et bestemt antall ganger eller at noe skal gjentas så lenge et
bestemt vilkår er sant. Når vi skriver en løkke, må vi huske at alt som skal
gjentas skal skrives med et innrykk innenfor selve gjentagelseslinjen. Dette ser
du i eksemplene lenger ned. I Python finnes det to typer løkker, `for` og
`while`.

## _for_-løkker

for-løkker kan brukes dersom du ønsker å gjenta noe et bestemt antall ganger
eller for hvert element i en liste, dictionary eller annet. For å gjenta noe et
bestemt antall ganger skriver vi `for i in range(n):`, hvor `n` er antall
gjentagelser og `i` er en midlertidig variabel som teller hvor langt vi har
kommet. Denne tellevariabelen må ikke kalles `i`, men du vil ofte se dette brukt
i eksempler. Dersom vi har en liste, og ønsker å gjenta noe for hvert element i
listen kan vi skrive `for i in <navn på liste>:`.

**_Eksempler_**

```python
# Denne løkken vil printe tallene 0, 1, 2, 3 og 4 under hverandre.
# Det er verdt å merke seg at 5 ikke tas med. Det er fordi Python
# starter å telle på 0.
for i in range(5):
 print(i)

# Løkken under bruker også 'for i in range', men benytter ekstra argumenter.
# De to første er nedre og øvre grense, og det siste er antall "hopp" vi vil
# gjøre per runde i løkken. Resultatet blir at det printes tall f.o.m. 10,
# t.o.m. 19, med intervaller på 2. Altså: 10, 12, 14, 16, 18.
# Merk at 20 ikke tas med. Det er fordi python ikke tar med den øvre grensen,
# kun opp til den.
for i in range(10, 20, 2):
 print(i)

# Denne løkken vil printe det dobbelte av hvert tall i listen.
min_liste = [1, 2, 3, 4, 5]
for tall in min_liste:
 print(tall * 2)

# Denne løkken vil printe én linje per oppføring i dictionarien, f.eks.
# "Per fikk karakteren 4". 'min_dict.items()' må brukes for å få tilgangtil
# til både nøkkel og verdi samtidig.
min_dict = {"Per":4, "Kari": 3, "Åse":5}
for navn, karakter in min_dict.items():
 print(navn, "fikk karakteren", karakter)

# Denne løkken brukes til å telle antall store bokstaver i en tekst.
min_tekst = "HøyEsTeRETt"
antall_store = 0
for bokstav in min_tekst:
 if bokstav.isupper():
  antall_store += 1
print("Teksten inneholder", antall_store, "store bokstaver")
```

## _while_-løkker

while-løkker brukes for å gjenta noe så lenge et vilkår er sant. En while-løkke
vil derfor alltid være skrevet på formen: `while <vilkår>:`

I eksempelet under ser du en while-løkke som printer variabelen `a`, så lenge
den er større enn 0. Linjen `a -= 1` reduserer a med 1 for hver gang løkken
gjentas. Dette betyr at koden vil printe tallene 10, 9, 8, 7, 6, 5, 4, 3, 2 og
1, men ikke 0.

```python
a = 10

while a > 0:
 print(a)
 a -= 1
```

Med while-løkker kan vi også lage løkker som gjentas for evig.

**_Eksempel_**

```python
while True:    # Denne løkken vil printe "Hei!" helt til vi avbryter programmet.
 print("Hei!")

a = 10
while a > 0:    # Denne løkken vil printe tallet 10 helt til vi avbryter programmet.
 print(a)

# Eksempelet under er ofte brukt i programmer hvor vi vil ha en "evighetsløkke",
# men samtidig ha mulighet til å avbryte den.
kjører = True
while kjører:
  avslutt = input("Vil du avslutte? (j/n): ")
  if avslutt.lower() == "j":
    kjører = False
```

Det andre eksempelet over, ligner på det første eksempelet på while-løkker.
Forskjellen er at i det siste eksempelet reduserer vi ikke variabelen `a` for
hver runde i løkken. Dette gjør at `a` alltid vil være større enn 0.

Det siste eksempelet over brukes ofte i spill eller programmer med menyer som
brukeren interagerer med. Her vil programmet fortsette å kjøre helt til brukeren
skriver inn "j" for å avslutte (dette gjøres med `input`-funksjonen som du vil
lære mer om senere i dette kurset). Da vil `kjører` settes til `False`, som gjør
at vilkåret for løkken ikke lenger er sant. Programmet går derfor ut av løkken
og avsluttes.
