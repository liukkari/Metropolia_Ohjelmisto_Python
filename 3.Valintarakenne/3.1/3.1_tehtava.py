# Tehtävä 3.1

'''Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
    Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
    ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
    Kuha on alamittainen, jos sen pituus on alle 37 cm.'''

kuhan_raja = 37
pituus = float(input("Mikä on kuhan pituus? (cm)\n"))
print()
if pituus < 37:
    erotus = kuhan_raja - pituus
    print(f"Kuha on {erotus}cm alamittainen! Raja on 37cm. Heitä järveen!")
else:
    print("Kuha on tarpeeksi iso! Tänään syödään kalaa!")