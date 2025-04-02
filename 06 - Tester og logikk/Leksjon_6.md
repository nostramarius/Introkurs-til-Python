# Leksjon 6 - Tester og logikk

## Logiske operatorer i Python

_Logiske operatorer_ er måter å sammenligne to eller flere ting på. Dette kan
være om noe er likt eller ikke likt noe annet, om noe er større eller mindre enn
noe annet, osv. Når vi sammenligner noe med logiske operatorer kan utfallet være
en av to muligheter. Enten vil utfallet være _sant_, som i Python skrives
`True`, eller _usant_, som i Python skrives `False`. De logiske operatorene i
Python er:

| Operator |         Navn         | Eksempel | Beskrivelse                           |
| :------: | :------------------: | :------: | ------------------------------------- |
|    ==    |        Er lik        |  a == b  | Sann hvis a er helt lik b             |
|    !=    |       Ikke lik       |  a != b  | Sann hvis a ikke er lik b             |
|    >     |      Større enn      |  a > b   | Sann hvis a er større enn b           |
|    <     |      Mindre enn      |  a < b   | Sann hvis a er mindre enn b           |
|    >=    | Større enn eller lik |  a >= b  | Sann hvis a er større enn eller lik b |
|    <=    | Mindre enn eller lik |  a <= b  | Sann hvis a er mindre enn eller lik b |

I tillegg til disse finnes det tre spesialord i Python som også hører til de
logiske operatorene. Disse er:

| Operator | Eksempel | Beskrivelse                       |
| :------: | :------: | --------------------------------- |
|   and    | A and B  | Sann hvis både A og B er sann     |
|    or    |  A or B  | Sann hvis enten A eller B er sann |
|   not    |  not A   | Sann hvis A er usann              |

I eksemplene for `and` , `or` og `not`, er A og B egne sammenligninger (dette
kaller vi som regel for _vilkår_), som f.eks.:

```python
a = 5
b = 2

a > b and b > 3   # Usann, siden ikke begge vilkårene er sanne
a > b and b > 0   # Sann, siden begge vilårene er sanne
a > b or b > 3    # Sann, siden minst et av vilkårene er sanne
a > b or b > 0    # Sann, siden minst et av vilkårene er sanne

a > b             # Sann, siden a er større enn b
not a > b         # Usann, siden vi snur vilkåret med 'not'
```

## Tester (_if / elif / else_)

En test i programmering brukes når en del av koden kun skal kjøres hvis et
vilkår er sant. Et eksempel på bruk av en test er når vi ønsker å skrive et tall
til konsollen, kun hvis det er et partall. En test i Python starter alltid med
spesialordet `if`, så på norsk omtaler vi det ofte som _hvis-tester_.

```python
tall = 42

if tall % 2 == 0:
  print(tall, "er et partall")
```

I eksempelet over lager vi en variabel, `tall` og gir den verdien 42. Deretter
tester vi om `tall` gir 0 i rest når vi deler det på 2. Dersom denne testen er
sann, betyr det at `tall` er et partall, siden det kun er partallene som gir 0 i
rest når de deles på 2. Dersom tallet er et partall, er testen sann, og
print-funksjonen skriver en beskjed om dette til konsoll. Dersom tallet er et
oddetall vil vilkåret til testen være usann, og programmet hopper over
print-funksjonen.

Tester kan også ha flere deler. I tillegg til `if`, har vi i Python `elif` og
`else`. `elif` er forkortelse for "else if" ("ellers hvis"). Et eksempel på bruk
av alle tre delene kan være:

```python
a = 10
b = 6

if a == b:
 print("a er lik b")
elif a > b:
 print("a er større enn b")
else:
 print("a er mindre enn b")
```

Dersom vi kjører koden over vil vi få opp "a er større enn b" i konsollen.
Testen fungerer på følgende måte:

1. Først testes det om a og b er samme tall. Dersom de er like, vil det printes
   "a er lik b" og programmet avslutter.
2. Hvis den første testen er sann, hopper vi over `elif` og `else` delene, og
   programmet avslutter.
3. Hvis den første testen er usann, går vi videre til `elif` delen og tester det
   som står der.
4. Dersom `elif`-testen er sann printes "a er større enn b", og programmet
   avslutter.
5. Dersom `elif`-testen er usann printes "a er mindre enn b", og programmet
   avslutter.

Grunnen til at vi ikke trenger et vilkår etter `else`, er at `else`-delen av en
test alltid skjer dersom ingen av testene over er sanne. Dette kalles ofte for
et "normaltilfelle" eller "default". I vårt eksempel kan vi tenke at dersom a
ikke er lik b og heller ikke større enn b, så må a være mindre enn b. Vi trenger
derfor ikke teste om dette stemmer.

Ut fra samme tankegang, kan vi sette opp et program som simulerer det å trille
en terning på følgende måte:

```python
from random import randint    # Importerer en funksjon som trekker tilfeldige tall

terningkast = randint(1,6)    # Trekker et tilfeldig tall mellom 1 og 6

# Tester de ulike mulighetene vi kan ha fått på "terningen" og printer resultatet
if terningkast == 1:
 print("Du trillet: 1")
elif terningkast == 2:
 print("Du trillet: 2")
elif terningkast == 3
 print("Du trillet: 3")
elif terningkast == 4:
 print("Du trillet: 4")
elif terningkast == 5
 print("Du trillet: 5")
else:
 print("Du trillet: 6")
```

Dersom vi har testet alle muligheter fra 1 til 5, og ingen av disse har vært
sanne, så vet vi at vi må ha trillet en 6er. Derfor trenger vi ikke å teste om
`terningkast == 6`.

Vi kan også bruke `and` og `or` i testene våre. Et eksempel på dette kan se slik
ut:

```python
a = 5
b = 10

if a%2 == 0 and b%2 == 0:
  print("Begge tallene er partall")
elif a%2 == 0 or b%2 == 0:
  print("Minst et av tallene er partall")
else:
  print("Ingen av tallene er partall")
```

Du vil også kunne komme over tester som ser slik ut:

```python
lys_på = True
mørkt_i_rommet = False

if lys_på:
  print("Lyset er på.")

if not mørkt_i_rommet:
  print("Rommet er lyst.")
```

Når vi bruker `True` og `False` som verdier i variabler, kan vi skrive tester
uten vilkår. I dette eksempelet er begge testene sanne, og begge
print-funksjonene utføres.
