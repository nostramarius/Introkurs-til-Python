# =======================================#
#  Leksjon 9 - Lag dine egne funksjoner  #
#                                        #
#  Løsningsforslag til oppgaver          #
# =======================================#

# Oppgave 1
def subtraksjon(tall_1, tall_2):
    svar = tall_1 - tall_2
    print(tall_1, "-", tall_2, "=", svar)


def multiplikasjon(tall_1, tall_2):
    svar = tall_1 * tall_2
    print(tall_1, "*", tall_2, "=", svar)


def divisjon(tall_1, tall_2):
    svar = tall_1 / tall_2
    print(tall_1, ":", tall_2, "=", svar)


subtraksjon(10, 8)
multiplikasjon(7, 7)
divisjon(24, 6)


# Oppgave 2
from math import pi


def areal_sirkel(radius):
    areal = pi * radius * radius
    print("Radius:", radius, "  Areal:", areal)


def omkrets_sirkel(radius):
    omkrets = 2 * pi * radius
    print("Radius:", radius, "  Omkrets:", omkrets)


areal_sirkel(5)
omkrets_sirkel(5)
