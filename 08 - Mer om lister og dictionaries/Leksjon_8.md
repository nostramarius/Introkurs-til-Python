# Leksjon 8 - Mer om lister og dictionaries

I denne leksjonen skal vi lære om to kraftige datatyper i Python, lister og dictionaries. Disse lar oss lagre og organisere samlinger av data på en strukturert måte.



## Lister

### Hva er en liste?

En liste er en ordnet samling av elementer. Elementene kan være av forskjellige datatyper (tall, tekst, osv.). Lister opprettes ved å sette elementene listen skal bestå av inn i firkantklammer  (hakeparenteser) `[]`, skilt med komma. Lister kan inneholde flere ulike datatyper, som tekst og tall, også i samme liste. Dette gjør lister ganske fleksible i bruk.



### Opprette en liste

Vi oppretter lister på samme måte som vi oppretter andre variabler, med formen `variabelnavn = variabelverdi`. I eksemplene under vises lister med én datatype og med ulike datatyper.

```python
frukt = ["eple", "banan", "appelsin"]
tall = [1, 2, 3, 4, 5]
blandet = ["Hei", 10, 3.14]
```



### Få tilgang til elementer

Elementer i en liste har en *indeks*, som representerer plasseringen til elementet i listen. Det første elementet i listen har indeks 0, det andre elementer har indeks 1, osv. Vi kan få tilgang til et element ved å bruke indeksen i firkantklammer etter navnet på listen. Eksemplene under bruker listene over.

```python
print(frukt[0]) # Skriver ut "eple"
print(tall[2]) # Skriver ut 3
```

Vi kan også bruke negativ indeks for å på tilgang til elementer. Indeks -1 referer til det siste elementet i en liste, -2 det nest siste, osv.

```python
print(blandet[-1]) # Skriver ut 3.14
print(frukt[-3]) # Skriver ut "eple"
```



### Endre elementer

Vi kan endre verdien til et element ved å tilordne en ny verdi til indeksen. Dette gjør vi ved å refere til den bestemte indeksen i listen og sette en ny verdi på en lignende måte som når vi oppretter variabler.

```python
frukt[1] = "pære"
print(frukt) # Skriver ut ["eple", "pære", "appelsin"]
```



### Legge til elementer

Det er primært to metoder som brukes for å legge til et element i en liste:



`.append()` legger til et element på slutten av listen.

`.insert()` legger til et element på en spesifikk indeks.

```python
frukt.append("kiwi")
print(frukt) # Skriver ut ["eple", "pære", "appelsin", "kiwi"]

frukt.insert(0, "mango")
print(frukt) # Skriver ut ['mango', 'eple', 'pære', 'appelsin', 'kiwi']
```

### Fjerne elementer

Vi har også to metoder for å fjerne elementer fra en liste:

`.remove()` fjerner det første elementet med en spesifikk verdi.

`.pop()` fjerner elementet på en spesifikk indeks.

```python
frukt.remove("pære")
print(frukt) # Skriver ut ["mango", "eple", "appelsin", "kiwi"]

fjernet_frukt = frukt.pop(0)
print(frukt) # Skriver ut ["eple", "appelsin", "kiwi"]
print(fjernet_frukt) # Skriver ut "mango"
```



Tidligere i dette kurset har vi også sett på hvordan vi kan bruke lister i løkker og utføre handlinger på alle eller enkelte elementer i en liste. Dette er med på å gjøre lister svært fleksible og som en datatype som kan brukes på mange ulike måter.



## Dictionaries (Ordbøker)

### Hva er en dictionary?

En dictionary er en samling av nøkkel-verdi-par, på samme måte som en ordbok har et oppslagsord og en definisjon. I en dictionary er hver nøkkel unik, og den brukes til å få tilgang til den tilhørende verdien. Nøkkelen er som regel en tekststreng (str) eller et tall, mens verdien kan være hvilken som helst datatype. Det er viktig å vite at dictionaries, i motsetning til lister, ikke er ordnet. Det vil si at rekkefølgen den er opprettet med ikke beholdes i minnet. Vi må derfor bruke nøkkel, ikke indeks, når vi jobber med dictionaries.



### Opprette en dictionary

Dictionaries kan opprettes på samme måte som alle andre variabler, men variabelverdien er nøkkel-verdi-par med krøllparenteser `{}` rundt. Nøkkel og verdi skilles med kolon `:`, og hvert nøkkel-verdi-par skilles med komma `,`.

```python
person = {"navn": "Ola", "alder": 16, "by": "Oslo"}
```



### Få tilgang til verdier

Vi får tilgang til en verdi ved å bruke nøkkelen i hakeparenteser. Dette ligner på måten vi får tilgang til verdier i en liste på, men her benytter vi nøkkelen, ikke indeks.

```python
print(person["navn"]) # Skriver ut "Ola"
print(person["alder"]) # Skriver ut 16
```



### Endre verdier

Vi kan endre verdien til en nøkkel ved å tilordne en ny verdi.

```python
person["alder"] = 17
print(person) # Skriver ut {"navn": "Ola", "alder": 17, "by": "Oslo"}
```



### Legge til nøkkel-verdi-par

Vi kan legge til nye nøkkel-verdi-par ved å tilordne en verdi til en ny nøkkel på følgende måte:

```python
person["yrke"] = "student"
print(person) # Skriver ut {"navn": "Ola", "alder": 17, "by": "Oslo", "yrke": "student"}
```



### Fjerne nøkkel-verdi-par

`.pop()` fjerner nøkkel-verdi-paret med en spesifikk nøkkel.

```python
person.pop("by")
print(person) # Skriver ut {"navn": "Ola", "alder": 17, "yrke": "student"}
```



### Dictionaries som database (litt mer avansert)

Noen ganger har vi behov for å lagre mye data, og i flere slike tilfeller kan dictionaries være en god struktur, som vi kan organisere til å passe behovet vårt. La oss tenke oss at vi ønsker å utvide eksempelt vi har brukt så langt, til å inneholde flere personer. F.eks. en liste over ansatte på en arbeidsplass eller elever i en klasse. En dictionary for en oversikt over ansatte i en håndverkerbedrift kan se ut som dette:

```python
ansatte= {
    1:{"fornavn":"Per", "etternavn":"Persen", "yrke":"tømrer", "alder":28},
    2:{"fornavn":"Lise", "etternavn":"Lisedotter", "yrke":"flislegger", "alder":32},
    3:{"fornavn":"Tore", "etternavn":"Toresen", "yrke":"elektriker", "alder":19}
}
```

Her brukes nøkkelsen som et ansattnummer, mens verdien er en egen dictionary med oppføringer for fornavn, etternavn, yrke og alder. Her ser vi altså et eksempel på hvordan vi også kan bruke dictionaries som verdier.

Noen aktuelle ting vi kunne tenkt oss å gjøre med denne databasen kunne vært:

```python
for ansatt, info in ansatte.items():
    print(ansatt, info)
```

Her skriver vi ut ansattnummer etterfulgt av all informasjonen. Hvis du skriver av og kjører koden, vil du legge merke til at informasjonen skrives ut i krøllparenteser, slik som det står i koden.  For å unngå dette kan vi referere direkte til de ulike nøklene i informasjonen.

```python
for ansatt in ansatte.keys(): 
    print(ansatt, ansatte[ansatt]["fornavn"], ansatte[ansatt]["etternavn"], ansatte[ansatt]["yrke"], ansatte[ansatt]["alder"])
```

Her printes ansattnummeret etter fulgt av for- og etternavn, uten krøllparenteser. Legg merke til hvordan vi bruker firkantklammer til å "dykke ned" i de ulike nøklene for å få tilgang på det vi er ute etter.

En annen ting det er verdt å merke seg er hvordan `.items()` og `.keys()` er brukt. Disse metodene brukes for å få tilgang til alle nøkkel:verdi-apr (.items) og nøkler (.keys) i dictionarien. `ansatte.items()` og `ansatte.keys()` lager lister med henholdsvis nøkkel:verdiparene og nøklene. Disse brukes igjen i print-funksjonene for å få tilgang til de ulike verdiene. Det finnes også en `.values()` metode som lager en liste med alle verdiene.


