"""
_summary_
    
    Tato cast prechadza vsetky mozne kluce pre to aby doslo k odsifrovaniu danej spravy.
    Kod vsak nie je dostatocne dobry na to aby bol schopny rozslisit spravnu spravu od zle odsifrovanje.
    Preto je nutnne to aby potom clovek si precital vsetky mozne kombinacie a nasledne urcil ktory z klucov je spravny. 
    Jedna sa o taky polovicny bruteforce pre ktory je nutnne na zaver este prekontrolovat potrebny vysledok.
"""

print("Lustenie cezarovej sifry")

# Zadanie znakov:
ZNAKY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Zadanie spravy pre rozsifrovanie
print("Zadaj spravu pre rozsifrovanie: ")
sprava = input().upper()

for kluc in range(len(ZNAKY)):
    preklad = ""
    
    # prekladanie znakov pre spravu
    for znak in sprava:
        if znak in ZNAKY:
            num = ZNAKY.find(znak)
            num = (num - kluc) % len(ZNAKY)  # oprava pretekania a použitie modulo

            preklad = preklad + ZNAKY[num]
        else:
            # pridanie znaku, ktorý netreba prelozit
            preklad = preklad + znak
    
    # zobrazenie slova spolu s ppouzitym klucom
    print("Kluc cislo: {}; sprava: {}".format(kluc, preklad))



