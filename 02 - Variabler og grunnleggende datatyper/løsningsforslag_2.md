# Leksjon 2 - Variabler og grunnleggende datatyper

## Løsningsforslag til oppgaver

### Oppgave 1

#### 1

```python
mitt_heltall = 123
mitt_desimaltall = 3.14
min_tekst = "Hei verden!"
min_liste = ["Marie", "Albert", "Galileo", "Katherine"]
min_ordbok = {"Marie": 1867, "Albert": 1879, "Galileo": 1564, "Katherine": 1918}

print(mitt_heltall)
print(mitt_desimaltall)
print(min_tekst)
print(min_liste)
print(min_ordbok)
```

#### 2

Output:

```
123
3.14
Hei verden!
['Marie', 'Albert', 'Galileo', 'Katherine']
{'Marie': 1867, 'Albert': 1879, 'Galileo': 1564, 'Katherine': 1918}
```

#### 3

- **Heltall (int)** skrives som normalt.
- **Desimaltall (float)** skrives som normalt. Desimaltegnet er punktum.
- **Teskt (str)** skrives som normalt. Hermetegnene tas ikke med.
- **Lister (list)** skrives ut med firkantklammer (`[]`) rundt hele og hermetegn
  rundt tekst.
- **Ordbøker (dict)** skrives ut med krølleklammer (`{}`) rundt hele og
  hermetegn rundt tekst.

### Oppgave 2

```python
mat = "pizza"
antall = 2

print("Jeg elsker", mat, "!")
print("Denne uka har jeg spist", mat, antall, "ganger.")
print("Jeg skal spise", mat, "igjen i morgen.")

antall = 3

print("Da har jeg spist det", antall, "ganger.")
```

**Output:**

```
Jeg elsker pizza !
Denne uka har jeg spist pizza 2 ganger.
Jeg skal spise pizza igjen i morgen.
Da har jeg spist det 3 ganger.
```
