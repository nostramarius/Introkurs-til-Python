# Leksjon 4 - Mer om tekst og tall

Til nå har du sett at vi kan skrive tekst og tall til konsoll, lagre det som
variabler og at vi kan regne med tall i Python. Men vi kan gjøre mye mer med
disse datatypene.

I Python er både tekster og tall _objekter_, og alle objekter har sine egne
egenskaper. Disse egenskapene inkluderer noe vi kan kalle _metoder_ (methods på
engelsk). Dette er en type funksjoner som kun kan brukes på en bestemt type
objekter, for eksempel tekst og tall.

I denne leksjonen skal vi se nærmere på hvordan vi kan jobbe med tekst og tall i Python. Vi skal lære noen nyttige metoder og funksjoner som gjør det enklere å manipulere og konvertere disse datatypene.

## Tekst (string)

Tekst, også kalt strenger, er en sekvens av tegn. Vi har allerede lært hvordan vi kan opprette tekstvariabler og skrive ut tekst til skjermen. Nå skal vi se på noen metoder som hjelper oss å endre tekst.

* **.lower()**
  
  * Denne metoden gjør alle bokstavene i en tekst om til små bokstaver.
  * Eksempel:

```python
tekst = "Hei, Verden!"
små_bokstaver = tekst.lower()
print(små_bokstaver) # Skriver ut "hei, verden!"
```



* **.upper()**
  
  * Denne metoden gjør alle bokstavene i en tekst om til store bokstaver.
  * Eksempel:
    
    

```python
tekst = "Hei, Verden!"
store_bokstaver = tekst.upper()
print(store_bokstaver) # Skriver ut "HEI, VERDEN!"
```



* **str()**
  
  * Denne funksjonen gjør om andre datatyper, som tall, til tekst.
  * Eksempel:
    
    

```python
tall = 123
tekst_tall = str(tall)
print(tekst_tall) # Skriver ut "123" 
print(type(tekst_tall)) # Skriver ut <class 'str'>
```



## Tall (integer og float)

Tall er en annen viktig datatype i Python. Vi har to hovedtyper: heltall (integer) og desimaltall (float). Nå skal vi se på noen funksjoner som hjelper oss å jobbe med tall.

* **int()**
  
  * Denne funksjonen gjør om andre datatyper, som tekst eller desimaltall, til heltall.
  * Eksempel:
    
    

```python
tekst_tall = "456" 
heltall = int(tekst_tall)
print(heltall) # Skriver ut 456 desimaltall = 3.14 heltall_desimal = int(desimaltall) print(heltall_desimal) # Skriver ut 3
```



* **float()**
  
  * Denne funksjonen gjør om andre datatyper, som tekst eller heltall, til desimaltall.
  * Eksempel:
    
    

```python
tekst_tall = "7.89"
desimaltall = float(tekst_tall)
print(desimaltall) # Skriver ut 7.89
heltall = 10
desimaltall_heltall = float(heltall)
print(desimaltall_heltall) # Skriver ut 10.0
```



* **max()**
  
  * Denne funksjonen finner det største tallet i en samling av tall.
  * Eksempel:



```python
tall1 = 10
tall2 = 20
største_tall = max(tall1, tall2)
print(største_tall) # Skriver ut 20
```

   

* **min()**
  
  * Denne funksjonen finner det minste tallet i en samling av tall.
  * Eksempel:



```python
tall1 = 10
tall2 = 20
minste_tall = min(tall1, tall2)
print(minste_tall) # Skriver ut 10
```

   

* **abs()**
  
  * Denne funksjonen finner absoluttverdien til et tall (fjerner minustegnet).
  * Eksempel:



```python
tall = -5 
absoluttverdi = abs(tall) 
print(absoluttverdi) # Skriver ut 5
```



