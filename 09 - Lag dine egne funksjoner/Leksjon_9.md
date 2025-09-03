# Leksjon 9 - Lag dine egne funksjoner

Så langt i dette kurset har du lest om og brukt flere ulike funksjoner. Dette er
funksjoner som kommer med Python, både innebygde og de som kan importeres. Men
du kan også lage dine egne funksjoner! Dette er nyttig når det er kode vi ønsker
å bruke flere ganger i programmet. Når vi lager en funksjon skriver vi koden én
gang og gir den et navn.

Måten vi lager våre egne funksjoner på i Python er med spesialordet `def`
etterfulgt av navnet vi vil gi funksjonen. Vi avslutter med parenteser og `:`.

Når vi skal bruke den trenger vi bare å skrive navnet til funksjonen etterfulgt
av parenteser.

```Python
def min_funksjon(): # Lager (definerer) funksjonen
  tall_1 = 10
  tall_2 = 4
  svar = tall_1 + tall_2

  print(tall_1, "+", tall_2, "=", svar)

min_funksjon() # Kjører funksjonen
```

Dersom du skriver av og kjører programmet over, vil det stå "10 + 4 = 14" i
konsollen. Dette er bra hvis det er det regnestykket vi vil finne svar på, men
ikke hvis vi vil ha en funksjon som kan addere sammen hvilke tall som helst.

Her kommer _argumenter_ inn. Vi kan gi funksjonen vår argumenter ved å legge de
inn i parentesene:

```Python
def min_funksjon(tall_1, tall_2): # Lager funksjonen og gir den to argumenter
  svar = tall_1 + tall_2 # Bruker argumentene i utregningen av svaret

  print(tall_1, "+", tall_2, "=", svar)

min_funksjon(10, 4) # 10 + 4 = 14
min_funksjon(7, 90) # 7 + 90 = 97
min_funksjon(12, 12) # 12 + 12 = 24
```

Som du ser over kan kjøre funksjonen flere ganger med ulike argumenter. For hver
gang regner funksjonen ut summen av tallene vi legger inn som argumenter og
skriver regnestykke med svar til konsollen.

Argumentene kan være andre datatyper enn tall. Her er et eksempel som bruker en
liste som argument:

```Python
def hils_venner(venneliste):
  for venn in venneliste:
    print("Hei", venn, "!")


venner = ["Natasha", "Vilde", "Oliver"]

hils_venner(venner)
```

> **Funksjoner på toppen**
>
> Når vi lager våre egne funksjoner er det vanlig å sette disse på toppen av
> filen, under eventuelle biblioteker og funksjoner som vi importerer.
