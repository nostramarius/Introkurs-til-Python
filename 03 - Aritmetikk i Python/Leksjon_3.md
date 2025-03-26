# Leksjon 3 - Aritmetikk i Python

## Regnearter

I Python kan du regne med tall som du ville gjort på en kalkulator. Dette er de
ulike regneoperatorene du kan bruke:

|    Regneart    | Operator i Python | Eksempel, Input | Eksempel, Output | Beskrivelse                                                                                              |
| :------------: | :---------------: | :-------------: | :--------------: | -------------------------------------------------------------------------------------------------------- |
|    Addisjon    |         +         |      2 + 5      |        7         | Adderer to tall                                                                                          |
|  Subtraksjon   |         -         |     10 - 4      |        6         | Subtraherer to tall                                                                                      |
| Multiplikasjon |        \*         |     4 \* 3      |        12        | Multipliserer to tall                                                                                    |
|    Divisjon    |         /         |      7 / 2      |       3.5        | Dividerer et tall på et annet, gir alltid et desimaltall til svar.                                       |
|  Gulvdivisjon  |        //         |     10 // 3     |        3         | Dividerer et tall på et annet. Dropper _rest_ og gir heltall til svar hvis utgangspunktet var et heltall |
|     Potens     |       \*\*        |    2 \*\* 5     |        32        | Opphøyer det første tallet i det andre                                                                   |
|    Modulus     |         %         |      7 % 3      |        1         | Gir hvor mye du får i _rest_ når du deler det første tallet på det andre                                 |

Hvis du har variabler som er tall (`int` eller `float`), kan du bruke variablene
dine i utregningene.

```Python
tall_1 = 13
tall_2 = 20

svar = tall_1 + tall_2

print(tall_1, "+", tall_2, "=", svar)
```

I koden over lager vi først to variabler, `tall_1` og `tall_2`. Deretter lager
vi en ny variabel, `svar`, som vi setter til å være lik summen av de to tallene.

> **OBS!**  
> I eksempelet over kunne det vært naturlig å bruke `sum` som navnet på
> variabelen som skal inneholde svaret. Dersom du prøver på dette, vil du få en
> feilmelding. Grunnen til det er at `sum` er et reservert nøkkelord som brukes
> i Python. Slike ord får gjerne en farge når du skriver de i en IDE, for å
> signalisere at de gjør noe spesielt og ikke kan brukes som navn på variabler.

## Øke og redusere en variabel

Noen ganger ønsker vi å øke eller redusere en variabel som inneholder et tall.
Som regel ved å legge til eller trekke fra et bestemt tall. Dette kan gjøres på
to forskjellige måter. Den første er ved å regne ut den nye verdien til
variabelen og sette den til dette.

```Python
poeng = 0
print(poeng) # --> 0

poeng = poeng + 1
print(poeng) # --> 1
```

Den andre metoden gir akkurat samme resultat, men bruker en "snarvei" i måten vi
skriver på.

```Python
poeng = 0
print(poeng) # --> 0

poeng += 1

print(poeng) # --> 1
```

Du kan bruke både `+`, `-`, `*` og `/` på denne måten.

```Python
a = 10

a += 2 # --> 12
a -= 2 # --> 8
a *= 2 # --> 20
a /= 2 # --> 5.0
```
