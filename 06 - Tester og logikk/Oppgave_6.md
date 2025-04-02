# Leksjon 6 - Tester og logikk

## Oppgaver

### Oppgave 1

Hvilke av vilkårene under er sanne og hvilke er usanne?

```python
a = 17
b = 4

a > b
a == b
a <= b
a >= b
a != b

a > b and a%2 == 0
b > a and b == 4
a != b and b%2 == 0
a%2 == 0 or b%2 == 0
b > 3 or b > a
```

### Oppgave 2

Kari er 15 år og broren hennes, Gunnar, er 12 år. Skriv et program som finner ut
om Kari har en lillebror eller storebror. Programmet skal skrive svaret til
konsollen.

Du kan starte programmet ditt slik:

```python
kari_alder = 15
gunnar_alder = 12

if ...
```

### Oppgave 3

I programmet under er det to variabler som viser om lyset i et rom er på eller
ikke og om det er mørkt i rommet eller ikke.

1. Bytt ut `...` i den siste `elif` testen med vilkår som betyr at det er på
   tide å skifte lyspære.
2. Bytt ut `...` i den siste `print`-funksjonen med en passende beskjed.
3. Kjør programmet ditt flere ganger og endre på variablene slik at du får
   testet om alt fungerer som det skal.

```python
lys_på = True
mørkt_i_rommet = False

if lys_på and not mørkt_i_rommet:
  print("Lyset er på og det er lyst i rommet")
elif not lys_på and mørkt_i_rommet:
  print("Lyset er av og det er mørkt i rommet")
elif ...:
  print("På tide å skifte lyspære")
else:
  print("...")
```
