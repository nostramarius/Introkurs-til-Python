# =======================================#
#  Leksjon 10 - Få input fra brukeren    #
#                                        #
#  Løsningsforslag til oppgaver          #
# =======================================#

# Oppgave 1
print("Oppgave 1")
print("---------")

print("Hva heter du?")
navn = input(": ")
print("Hei " + navn + "! Hyggelig å møte deg.")

print("Hvor gammel er du?")
alder = input(": ")
print("Det betyr at du er", int(alder) + 3, "år gammel om 3 år.")

print("Hvor bor du?")
sted = input(": ")
print(sted, "høres ut som et fint sted!")
print("")

# Oppgave 2
print("Oppgave 2")
print("---------")

kjører = True

while kjører:
    print("Meny")
    print("-----------------")
    print("1: Få en hilsen")
    print("2: Avslutt programmet")
    print("")

    valg = input(": ")
    if valg == "1":
        print("Hei på deg!")
        print("")
    elif valg == "2":
        kjører = False
    else:
        print("Vennligst velg et av alternativene i menyen.")
        print("")

print("")
print("Takk for nå")

print("")

# Oppgave 3
print("Oppgave 3")
print("---------")

brukere = {"Per14": 1234, "Anna16": 4242, "Linnea32": 4321}

b_navn = input("Brukernavn: ")
pin = int(input("Pinkode: "))

if b_navn in brukere:
    if brukere[b_navn] == pin:
        print("Velkommen", b_navn)
    else:
        print("Feil pinkode. Vennligst prøv igjen.")
else:
    print("Bruker ble ikke funnet.")
