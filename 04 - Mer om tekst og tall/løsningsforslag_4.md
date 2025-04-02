# Leksjon 4 - Mer om tekst og tall

## Løsningsforslag til oppgaver

### Oppgave 1

```python
beskjed = "jeg elsker python"

skrik = beskjed.upper() + "!!!"
```



### Oppgave 2

Metoden det er snakk om er .capitalize().

```python
mitt_navn = "per"

hilsen = "Hei " + mitt_navn.capitalize() + "!"

print(hilsen)
```

Dersom Per  hadde hatt et dobbeltnavn, for eksempel Per Arne, ville han oppdaget at kun Per fikk stor bokstav. Dette kommer av at .capitalize() kun gjør første bokstav i hele teksten stor. Det finnes måter å få til det samme på dobbeltnavn, men da må vi kombinere dette med andre metoder. For eksempel kan vi dele opp strenger med metoden .split(). Denne kan være veldig nyttig når vi jobber med tekst. Søk gjerne opp og les mer om denne på egenhånd.



### Oppgave 3

```python
tall_1 = "10"
tall_2 = 5.4
tall_3 = 4
tall_4 = "17.2"

total = float(tall_1) + tall_2 + tall_3 + float(tall_4)
```

Som du ser kan vi addere int og float uten problem, men for `tall_1` og `tall_4` må vi gjøre de om til en passende datatype først.


