# Leksjon 7 - Løkker

## Løsningsforslag til oppgaver

### Oppgave 1

```python
venner = ["Mohammad", "Silje", "Aisha", "Fredrik", "Sara"]

for navn in venner:
  print("Hei " + navn + "!")
```

### Oppgave 2

Her er to måter denne oppgaven kan løses på. Felles for begge er at vi bruker en
`range` opp til 20, siden de ti første oddetallene er f.o.m. 1, t.o.m. 19.

I den første metoden bruker vi en test og `%` til å finne ut om hvert tall vi
går gjennom gir 1 i rest når vi deler det på 2. Hvis det er sant er tallet et
oddetall, og vi skriver det til konsoll.

```python
for i in range(20):
  if i%2 == 1:
    print(i)

```

En annen måte er å starte på 1 og skrive annenhvert tall til konsoll. Det kan vi
gjøre på følgende måte:

```python
for i in range(1,20,2):
  print(i)
```

### Oppgave 3

```python
a = 0

while a < 5 :
  print(a)
```

Her vil det høyeste tallet som skrives være 0. Grunnen til dette er at vi aldri
øker `a` i løkken. Dermed vil `a` alltid være 0, og vilkåret alltid være sant.
Vi har laget en evighetsløkke som printer 0 for hver runde i løkken.

```python
b = 2

while b < 23:
  if b%5 == 0:
    print(b)
  b += 1
```

I denne løkken vil det høyeste tallet som skrives til konsollen være 20. I
løkken tester vi om `b` er delelig på 5 (gir 0 i rest når vi deler det på 5), og
skriver det til konsoll hvis dette er sant. Siden vi øker `b` med 1 for hver
runde, vil tallene som skrives være 5, 10, 15 og 20.
