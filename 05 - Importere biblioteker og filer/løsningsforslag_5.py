# =============================================#
#  Leksjon 5 - Importere biblioteker og filer  #
#                                              #
#  Løsningsforslag til oppgaver                #
# =============================================#

# Oppgave 1
import random  # Importerer hele random-biblioteket

tall_1 = random.randint(1, 10)  # Trekker et tilfeldig tall mellom 1 og 10
tall_2 = random.randint(1, 10)  # Trekker et tilfeldig tall mellom 1 og 10
svar = tall_1 * tall_2  # Multipliserer tallene

print(tall_1, "*", tall_2, "=", svar)  # Skriver tall og svar til konsollen


# Oppgave 2
from math import pi  # Importerer kun `pi` fra `math`

radius = 5

areal = pi * radius * radius  # Regner ut arealet

print("Arealet er", areal)


# Oppgave 3
