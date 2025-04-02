# Leksjon 6 - Tester og logikk

## Løsningsforslag til oppgaver

### Oppgave 1

```python
a = 17
b = 4

a > b   # Sann
a == b  # Usann
a <= b  # Usann
a >= b  # Sann
a != b  # Sann

a > b and a%2 == 0    # Usann (første vilkår er sant, andre vilår er usant)
b > a and b == 4      # Usann (første vilkår er usant, andre vilår er sant)
a != b and b%2 == 0   # Sann (første vilkår er sant, andre vilår er sant)
a%2 == 0 or b%2 == 0  # Sann (første vilkår er usant, andre vilår er sant)
b > 3 or b > a        # Sann (første vilkår er sant, andre vilkår er usant)
```

### Oppgave 2

```python
kari_alder = 15
gunnar_alder = 12

if kari_alder > gunnar_alder:
  print("Gunnar er Kari sin lillebror.")
elif kari_alder < gunnar_alder:
  print("Gunnar er Kari sin storebror.")
else:
  print("Gunnar og Kari er tvillinger.")
```

### Oppgave 3

```python
lys_på = True
mørkt_i_rommet = False

if lys_på and not mørkt_i_rommet:
  print("Lyset er på og det er lyst i rommet.")
elif not lys_på and mørkt_i_rommet:
  print("Lyset er av og det er mørkt i rommet.")
elif lys_på and mørkt_i_rommet:
  print("På tide å skifte lyspære.")
else:
  print("Der lyst ute og gardinene er trukket fra.")
```
