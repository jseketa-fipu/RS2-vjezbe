from .proizvodi import Proizvod, ProizvodOrderType, skladiste


class Narudzba:
    def __init__(
        self, naruceni_proizvodi: list[ProizvodOrderType], ukupna_cijena: float
    ) -> None:
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = float(ukupna_cijena)

    def ispis_narudzbe(self) -> None:
        parts = [
            f'{p["naziv"]} x {p["narucena_kolicina"]}' for p in self.naruceni_proizvodi
        ]
        print(
            f'Naručeni proizvodi: {", ".join(parts)}, Ukupna cijena: {self.ukupna_cijena} eur'
        )


def _find_u_skladistu(naziv: str) -> Proizvod | None:
    for p in skladiste:
        if p.naziv == naziv:
            return p
    return None


def napravi_narudzbu(naruceni_proizvodi: list[ProizvodOrderType]) -> Narudzba | None:
    # three checks not needed because of static typing:
    # - must be a list # - list must be only composed of dictionaries
    # - all dictionaries have the needed keys (naziv, cijena, narucena_kolicina)

    # list is not allowed to be empty
    if not naruceni_proizvodi:
        return None

    # check if exists and enough stock is available
    for item in naruceni_proizvodi:
        prod = _find_u_skladistu(item["naziv"])
        if prod is None or prod.dostupna_kolicina < item["narucena_kolicina"]:
            print(f'Proizvod {item["naziv"]} nije dostupan!')
            return None

    # total price - a oneliner
    ukupna_cijena: float = sum(
        float(p["cijena"]) * int(p["narucena_kolicina"]) for p in naruceni_proizvodi
    )

    # update stock numbers
    for item in naruceni_proizvodi:
        prod = _find_u_skladistu(item["naziv"])
        assert prod is not None
        prod.dostupna_kolicina -= item["narucena_kolicina"]

    return Narudzba(naruceni_proizvodi, ukupna_cijena)
