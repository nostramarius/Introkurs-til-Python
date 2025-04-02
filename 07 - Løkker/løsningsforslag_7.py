# ===============================#
#  Leksjon 7 - Løkker            #
#                                #
#  Løsningsforslag til oppgaver  #
# ===============================#

# Oppgave 1
print("Oppgave 1")
print("---------")

venner = ["Mohammad", "Silje", "Aisha", "Fredrik", "Sara"]

for navn in venner:
    print("Hei " + navn + "!")

print("")

# Oppgave 2
print("Oppgave 2")
print("---------")

# Metode 1 - Skrive tallene som gir 1 i rest når de divideres på 2
for i in range(20):
    if i % 2 == 1:
        print(i)

print("")

# Metode 2 - Skrive annenhvert tall fra 1 til 20
for i in range(1, 20, 2):
    print(i)

print("")

# Oppgave 3
print("Oppgave 3")
print("---------")

# Det høyeste tallet som skrives vil være 0
# Avkommenter denne for å vise hva som skjer (evighetsløkke)
# a = 0
#
# while a < 5 :
#   print(a)

# Det høyeste tallet som skrives vil være 20
b = 2

while b < 23:
    if b % 5 == 0:
        print(b)
    b += 1
