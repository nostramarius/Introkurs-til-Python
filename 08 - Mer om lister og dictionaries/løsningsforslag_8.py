# ============================================#
#  Leksjon 8 - Mer om lister og dictionaries  #
#                                             #
#  Løsningsforslag til oppgaver               #
# ============================================#

# Oppgave 1
min_ønskeliste = ["Bålstekepanne", "Sokker", "Vinterjakke", "Akebrett"] # Oppretter listen


min_ønskeliste.append("Spikkekniv") # .append() brukes til å legge til noe på slutten av listen
min_ønskeliste.insert(0, "Tennstål") # .insert() brukes til å plassere på en bestemt indeks. Argumentene er først plassering, så element


min_ønskeliste.pop(-2) # .pop() fjerner et element fra listen. Argumentet -2 viser til det nest siste elementet.


# Oppgave 2
min_info = {
    "fornavn": "Per",
    "etternavn": "Persen",
    "alder": 15,
    "favorittfag": "Gym"
}


print(min_info) # Skriver hele dict til konsoll


fornavn = min_info["fornavn"]
etternavn = min_info["etternavn"]
print(fornavn, etternavn)
# print(min_info["fornavn"], min_info["etternavn"])


min_info["antall_søsken"] = 2 # Oppretter nøkkelen "antall_søsken" og gir den verdien 2


min_info["favorittfag"] = "Programmering" # Endrer verdien til nøkkelen "favorittfag" fra Gym til Programmering


min_info.pop("alder") # Fjerner nøkkelen "alder", og verdien den har, fra dictionarien
