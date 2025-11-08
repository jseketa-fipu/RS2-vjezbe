from shop.proizvodi import dodaj_proizvod, Proizvod, ProizvodType, ProizvodOrderType
from shop.narudzbe import napravi_narudzbu

proizvodi_za_dodavanje: list[ProizvodType] = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100},
]
for proizvod in proizvodi_za_dodavanje:
    # ** unpacks dict as keyword arguments (key->value)
    dodaj_proizvod(Proizvod(**proizvod))

# show the stock
Proizvod.ispis()

# list of items to be ordered
naruceni: list[ProizvodOrderType] = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
]
narudzba = napravi_narudzbu(naruceni)
if narudzba:
    narudzba.ispis_narudzbe()
    print("\nNakon narudžbe:")
    Proizvod.ispis()
