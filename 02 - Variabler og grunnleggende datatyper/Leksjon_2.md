# Leksjon 2 - Variabler og grunnleggende datatyper

## Variabler

Variabler i Python kan inneholde ulik type informasjon. Vi gir som regel
variablene våre navn som beskriver hva de inneholder og skriver de med kun små
bokstaver. Dersom du vil bruke flere ord i et variabelnavn, kan du skille de med
`_`. For å opprette en variabel og gi den en verdi skriver vi:
`variabelnavn = variabelverdi`. Merk at vi bruker et enkelt likhetstegn for å
tildele en variabel en verdi. Senere vil du se at vi bruker dobbelt likhetstegn
til noe annet.

Eks.:

```python
min_alder = 17
mitt_navn = "Per"
antall_søsken = 2
mine_søsken = ["Siri", "Bjarne"]
```

Variabler i Python kan endres underveis i koden din, og i motsetning til enkelte
programmeringsspråk, kan du også endre hva slag datatype variabelen inneholder.
Se mer om datatyper lenger ned.

Fordelen med å bruke variabler er at de kan brukes flere steder i koden, og
dersom du endrer den et sted, vil den endres over alt.

Eks.:

```python
mitt_navn = "Per"
min_alder = 17

print("Hei, jeg heter", mitt_navn, ".")
print(mitt_navn, "er", min_alder, "år gammel.")

mitt_navn = "Ingrid"

print("Hei, jeg heter", mitt_navn, ".")
```

Lag et program med denne koden, så vil du se at navnet som skrives til konsoll
endrer seg.

## Datatyper

I python finnes det flere ulike datatyper. Eksempler på datatyper kan være
heltall og tekst. Hver datatype kan manipuleres og behandles på ulike måter.
Under ser du en oversikt over de vanligste datatypene.

|              Datatype               | Forkortelse |      Eksempel       | Beskrivelse                                                                                                                                                                                 |
| :---------------------------------: | :---------: | :-----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|          Heltall / Integer          |     int     |          5          | Vanlige heltall                                                                                                                                                                             |
| Desimaltall / Floating point number |    float    |        3.42         | Vanlige desimaltall. Merk deg at desimaltegnet i Python er `.`, ikke `,`.                                                                                                                   |
|           Tekst / String            |     str     |    "Hei verden!"    | Tekst skrives alltid mellom to _hermetegn_. Alt mellom hermetegnene anses som tekst, også tall og spesialtegn.                                                                              |
|            Liste / List             |    list     |  \["Per", 2, a, 5]  | En samling av tall, tekst, variabler eller andre ting. Lister har en indeks som beskriver hvor i listen hver ting befinner seg. Det første elementet har indeks 0, det andre indeks 1, osv. |
|        "Ordbok" / Dictionary        |    dict     | {"Per":5, "Kari":3} | En samling av _nøkkel:verdi_ par. Som i en ordbok er nøkkelen "oppslagsordet" og verdien "definisjonen".                                                                                    |
