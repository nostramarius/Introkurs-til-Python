# Leksjon 5 - Importere biblioteker og filer

## Importere biblioteker

Når du installerer Python på datamaskinen din, følger det mange funksjoner. Noen
av disse har du allerede sett og brukt i dette kurset. Eksempler er:

- `print()` som skriver ting til konsollen
- `int()` som gjør om til datatypen integer (heltall)
- `str()` som gjør om data til datatypen string (tekst)
- `max()` som finner det største tallet

I Python kalles alle disse for _innebygde funksjoner_, da de alltid er
tilgjengelig. I tillegg til disse innebygde funksjonene, kommer Python med mange
(veldig mange) andre funksjoner, som ikke er tilgjengelige med en gang. Disse
funksjonene ligger i egne biblioteker, som er samlinger av funksjoner og andre
ting, som må importeres til programmet før de kan brukes. To eksempler på slike
biblioteker er:

- [**random**](https://docs.python.org/3/library/random.html), som inneholder
  funksjoner som har med tilfeldighet å gjøre
- [**math**](https://docs.python.org/3/library/math.html), som inneholder
  funksjoner og variabler som har med matematikk å gjøre

For å importere biblioteker bruker vi spesialordet `import`.

```python
import random
import math
```

Vi kan også importere flere biblioteker på samme linje som dette:

```python
import random, math
```

En av funksjonene i random-biblioteket er `randint()`. Denne funksjonen trekker
et tilfeldig heltall mellom to grenser vi bestemmer.

```python
import random # Importerer biblioteket random

tall = random.randint(1,6) # Trekker et tilfeldig heltall f.o.m. 1, t.o.m. 6

print(tall) # Skriver tallet som ble trukket til konsollen
```

I eksempelet over ser du hvordan vi bruker funksjonene som ligger i biblioteket.
Vi starter med å skrive navnet på biblioteket, så et punktum og så navnet på
funksjonen. Som alle funksjoner må vi avslutte med parenteser, hvor vi også
skriver inn argumentene funksjonen skal bruke.

> **Importer på toppen av filen**
>
> Når vi importerer biblioteker og funksjoner skriver vi disse linjene på toppen
> av filen.

## Importere enkeltfunksjoner

Noen ganger trenger vi bare en eller noen få funksjoner fra et bibliotek. Da
trenger vi ikke importere hele biblioteket, men kan i stedet for importere kun
den eller de funksjonene vi trenger. Dette gjør vi på følgende måte:

```python
from random import randint
```

Hvis vi vil importere flere funksjoner fra samme bibliotek kan vi skille
funksjonene med `,`:

```python
from random import randint, choice
```

Som du ser bruker vi spesialordet `from` når vi ønsker å importere
enkeltfunksjoner, og formen for å importere er `from bibliotek import funksjon`

Når vi importerer enkeltfunksjoner på denne måten bruker vi ikke
biblioteksnavnet når vi skal bruke funksjonen:

```python
from math import sqrt # Importerer funksjonen `sqrt` (kvadratrot) fra biblioteket math

areal = 81

sidelengde = sqrt(areal) # Vi dropper `math.` foran funksjonsnavnet

print(sidelengde)
```

## Snarveier til biblioteksnavn

Dersom vi skal bruke funksjoner fra et bibliotek mange ganger, og det i tillegg
har et langt navn, kan vi lage en "snarvei" eller "forkortelse" for
biblioteksnavnet:

```python
import random as ran

tall = ran.randint(1,6)
```

Dersom du gjør dette er det viktig at du ikke endrer navnet på biblioteket til
spesialord eller variabler du bruker.

Vi kan også importere hele biblioteket med `from`-metoden og `*` i stedet for
funksjonsnavn.

```python
from math import * # Importerer alle funksjoner fra `math`

radius = 5

omkrets = 2 * pi * radius # I `math` finner vi blant annet variabelen `pi`

print("Omkretsen av sirkelen er", omkrets)
```

Fordelen med dette er at vi slipper å skrive biblioteksnavnet, men vi må da
passe på at vi ikke får konflikter med funksjoner fra andre biblioteker eller
egne funksjons- og variabelnavn.

## Importere andre .py-filer

Når vi skriver store programmer, kan det være en fordel å fordele koden over
flere filer, og så importere disse til en "hovedfil". Dersom du er helt ny til
programmering og Python vil du nok ikke ha behov for dette enda, men her er et
kort eksempel på hvordan det kan gjøres.

Se for deg at du har to filer i samme mappe. Den ene filen heter `venner.py` og
inneholder en liste med navn. Den andre filen heter `main.py` og inneholder
programmet vi ønsker å kjøre. Filene kan se slik ut:

```python
# venner.py

mine_venner = ["Fredrik", "Rikke", "Yasmin", "Mattis"]
```

```python
# main.py

import venner

for venn in mine_venner:
  print(venn)
```

Så lenge filene ligger i samme mappe, kan vi bruke `import` og navnet på filen
for å importere den. Vi tar ikke med `.py` på slutten av filnavnet.

Det er også mulig å importere filer i andre mapper, men det går vi ikke inn på
her.
