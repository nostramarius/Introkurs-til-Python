# Leksjon 1 - Kom i gang med Python

## Løsningsforslag til oppgaver

### Oppgave 1

```Python
print("Hei Per!")
```

### Oppgave 2

```Python
print("Hei Per!")
print("Hei Pål!")
print("Hei Espen!")
```

### Oppgave 3

Hvis du skriver noe feil, for eksempel glemmer hermetegn, parenteser eller
feilstaver print, vil ikke programmet kjøre. I konsollen vil du i stedet få opp
en feilmelding. Denne feilmeldingen gir deg informasjon om hvor i koden din det
ble møtt på et problem og hva slags problem det er snakk om. Noen ganger kan du
også få hint fra Python om hva som kan være problemet.

Under ser du tre eksempler på feilmeldinger. I den første er `print` feilstavet,
og vi får en `NameError`. Dette betyr at python ikke kjente igjen
funksjonsnavnet vi oppga. Som du ser var vi nærme nok til at python klarer å
foreslå at vi kanskje mente `print` i stedet for `prnt`.

```
>>> prnt("Hei verden!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```

I dette eksempelet har vi glemt parenteser rundt teksten vi ønsker å skrive til
konsollen. Igjen får vi beskjed om hvor feilen oppstod, men denne gangen får vi
en `SyntaxError`. Dette betyr at noe er feil med hvordan du har satt sammen ord
og tegn. Du kan sammenligne dette med rettskriving og tegnsetting i tekster
(mangler stor bokstav etter punktum, har ikke punktum etter en setning, osv.).
Forskjellen på et menneske som leser teksten din og en datamaskin som leser
koden din, er at datamaskinen ikke klarer å fortsette når du har slike feil.
Heldigvis for oss, foreslår python også her hva som kan være feilen.

```
>>> print "Hei verden!"
  File "<stdin>", line 1
    print "Hei verden!"
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

I det tredje eksempelet har vi glemt hermetegn rundt teksten vi vil skrive.
Igjen får vi en `SyntaxError`. Denne gangen foreslår også python hva som kan
være feil, men her ser vi at forslaget ikke stemmer. Dette er viktig å merke
seg, så vi ikke blindt følger det som blir foreslått, men undersøker det selv.

```
>>> print(Hei verden!)
  File "<stdin>", line 1
    print(Hei verden!)
          ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

> [!NOTE] Andre typer feil Det finnes mange andre feiltyper i python, som du
> sikkert vil møte på etterhvert. Når de oppstår, pass på at du leser
> feilmeldingen og undersøker hva som kan være feil. Ofte er det små ting, som
> feilstavinger og at du har glemt et tegn som er problemet. Senere i dette
> kurset vil vi også jobbe med innrykk. Feil i dette vil som regel føre til en
> `IndentationError`.
