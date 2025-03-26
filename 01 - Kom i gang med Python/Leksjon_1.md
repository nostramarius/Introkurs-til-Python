# Leksjon 1 - Kom i gang med Python

## Om Python

Python er et tekstbasert programmeringsspråk som ofte er anbefalt til
nybegynnere på grunn av språkets enkle syntaks, men er også mye brukt i
industrien. Python passer perfekt for 2D-spill, automatisering, vitenskapelig
analyse, GUI-applikasjoner og servere.

## Installer Python på datamaskinen din

Du kan skrive pythonkode på alle maskiner. Alt du trenger er et program som lar
deg skrive og lagre tekstfiler, men for å kunne kjøre koden din, må du
installere Python på maskinen din. Dette kan gjøres på flere måter, men den
enkleste er å installere det direkte fra Python sin hjemmeside.

1. Gå til <https://python.org/downloads> og last ned siste versjon av Python
2. Åpne installasjonsfilen og følg installasjonsveilederen
   - I løpet av installasjonen vil du få opp et alternativ om å legge Python til
     PATH, godta dette dersom du vil ha mulighet til å bruke Python og kjøre
     pythonfiler fra din maskins terminal.
3. Du kan sjekke at Python er installert ved å søke opp programmet IDLE, eller
   (hvis du har lagt Python til PATH) åpne en terminal og skrive inn `py`.

Det finnes også flere måter å installere Python på. Dette er som regel gjennom å
innstallere IDEer eller andre programmer som inkluderer Python. Et eksempel på
dette er IDEen Thonny, som du kan lese mer om lenger ned.

## Du trenger et sted å skrive kode

Du kan skrive kode i alle tekstbehandlingsprogrammer som bruker plaintext.
Likevel er det anbefalt å bruke en IDE (integrated development environment), da
dette gir deg langt mer støtte og funksjonalitet til å skrive kode. Under kan du
lese om tre gode alternativer. De står i rekkefølge fra minst til mest
innholdsrikt. Vær oppmerksom på at IDEer med mye funksjonalitet _kan_ bli
overveldende for de som er helt nye til IDEer og programmering. Dersom du er
helt ny, men ønsker en IDE med god funksjonalitet som samtidig ikke overvelder
deg med en gang, kan Thonny være et godt utgangspunkt for deg.

> Dette kurset vil ikke gå inn på hvordan man bruker hver enkelt IDE. Til dette
> finnes det mange gode artikler og videoer på internett. Søk for eksempel på
> "Thonny tutorial" eller "How to use IDLE?"

### IDLE

Dersom du laster ned og installerer Python fra
[Pythons egen side](https://python.org), så følger IDLE med. IDLE er en enkel
IDE som er lett å bruke, men mangler en del avanserte funksjoner.

### Thonny

[Thonny](https://thonny.org) er en gratis IDE som også inkluderer en versjon av
Python. Alt du trenger for å komme i gang med Python er altså inkludert når du
laster ned og installerer Thonny. I Thonny får du også en del ekstra verktøy,
sammenlignet med IDLE, som debug-konsoll, variabeloversikt og mulighet til å ha
både editor, konsoll og andre ting i samme vindu.

### VScode

[VScode](https://code.visualstudio.com/) er utviklet av Microsoft og er åpen for
at andre kan lage egne tillegg til programmet. Det gjør at VScode har nærmest
ubegrensede muligheter og egner seg til alle typer programmeringsspråk. For å
jobbe med python i VScode trenger du å installere noen python-spesifikke tillegg
for at kodingen din skal fungere optimalt. Du må også installere python på
maskinen din, i tillegg til VScode. Dette kan du gjøre fra
[Pythons egen side](https://python.org).

## Ditt første program - Hei verden

Det første programmet man pleier å lage når man skal lære et nytt
programmeringsspråk blir kalt "Hello World". Dette er et veldig enkelt program
som skriver en setning til konsoll. I Python gjør man dette på følgende måte:

```python
# Mitt første program
print("Hei verden!")
```

Skriv denne kodelinjen, lagre og kjør programmet. Dersom du har gjort det
riktig, vil du få opp setningen du har skrevet mellom hermetegnene inne i
parentesen. Du kan også prøve å endre på setningen og se at outputen endres.

Dette programmet viser flere ting i Python. Det første er at for å skrive ting
til konsoll, bruker vi funksjonen `print()`. Alle funksjoner i Python avsluttes
med parenteser, og det som står inne i parentesene kalles _argumenter_.
Argumentene til en funksjon påvirker hva som blir outputen til funksjonen. For
`print`, er det første argumentet hva som skal skrives til konsoll. Det finnes
også andre argumenter du kan bruke. Disse kan du lese mer om
[her](https://www.w3schools.com/python/ref_func_print.asp). Vi ser også at tekst
i Python skrives mellom to hermetegn. Du la kanskje merke til den første linjen,
den som begynner med `#`? Alle linjer som begynner med dette tegnet kalles
_kommentarer_ og leses ikke som kode når programmet kjører. Det er nyttig for å
beskrive programmet ditt og for å "ta bort" kodelinjer, uten å slette de, når du
tester programmet ditt.

## Nyttige ressurser når du lærer (altså for alltid)

En ting som er helt sikkert når du lærer deg å skrive kode i et nytt språk, er
at du garantert kommer til å gjøre feil og lure på hvordan du kan få til det du
ser for deg. Når du står i disse situasjonene finnes det mange gode ressurser
tilgjengelig som kan hjelpe deg. Det kan også hende du trenger flere oppgaver og
prosjekter å øve med. Her er en liten liste med nettsider du kan se på:

- **[Pythons egen dokumentasjon](https://docs.python.org/3/)** har informasjon
  om det meste knyttet til språket.
- **[Stack Overflow](https://stackoverflow.com/)** er en side hvor man kan
  stille spørsmål og få hjelp til å løse problemer. Som oftest har noen spurt om
  det du lurer på allerede, så start med å søke etter det du lurer på.
- **[Oppgavesamlingen til kidsakoder.no](https://oppgaver.kidsakoder.no/python)**
  har mange gode øvingsoppgaver, med instruksjoner, som du kan bruke.

Dersom du står fast er ofte det enkleste å søke opp det du lurer på. Det kan
lønne seg å søke på engelsk, da det er språket de fleste rssurser og
diskusjonsforumer benytter.
