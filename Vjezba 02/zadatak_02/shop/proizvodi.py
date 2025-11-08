from typing import TypedDict


class ProizvodType(TypedDict):
    naziv: str
    cijena: float | int
    dostupna_kolicina: int


class ProizvodOrderType(TypedDict):
    naziv: str
    cijena: float | int
    narucena_kolicina: int


class Proizvod:
    def __init__(self, naziv: str, cijena: float, dostupna_kolicina: int) -> None:
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    @staticmethod
    def ispis() -> None:
        for proizvod in skladiste:
            print(
                f"Naziv: {proizvod.naziv}, cijena: {proizvod.cijena}, dostupna kolicina: {proizvod.dostupna_kolicina}"
            )


skladiste: list[Proizvod] = [Proizvod("Kuciste", 12, 20), Proizvod("CPU", 150, 10)]


def dodaj_proizvod(proizvod: Proizvod) -> None:
    skladiste.append(proizvod)
