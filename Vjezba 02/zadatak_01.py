# Exercise 02 - task 04

# 1) Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža.
# Dodajte metodu ispis koja će ispisivati sve atribute automobila.

# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis.
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama,
# trenutnu godine dohvatite pomoću datetime modula.
from math import pi
from datetime import date
from typing import TypedDict


class Automobil:
    def __init__(
        self, marka: str, model: str, godina_proizvodnje: int, kilometraza: int
    ) -> None:
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self) -> None:
        current_year = date.today().year
        print(f"Auto je star {current_year - self.godina_proizvodnje} godina.")


auto = Automobil("Opel", "Astra", 1992, 247000)
auto.ispis()

# 2) Definirajte klasu Kalkulator s atributima a i b.
# Dodajte metode zbroj, oduzimanje, mnozenje, dijeljenje, potenciranje i
# korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.


class Kalkulator:
    def __init__(self, a: int | float, b: int | float) -> None:
        self.a = a
        self.b = b

    def zbroj(self) -> float:
        return self.a + self.b

    def oduzimanje(self) -> float:
        return self.a - self.b

    def mnozenje(self) -> float:
        return self.a * self.b

    def dijeljenje(self) -> float:
        return self.a / self.b

    def potenciranje(self) -> float:
        return self.a**self.b

    def korijen(self) -> float:
        return self.a ** (1 / self.b)


kalkulator = Kalkulator(3, 4)
print(kalkulator.zbroj())
print(kalkulator.oduzimanje())
print(kalkulator.mnozenje())
print(kalkulator.dijeljenje())
print(kalkulator.potenciranje())
print(kalkulator.korijen())

# 3) Definirajte klasu Student s atributima ime, prezime, godine i ocjene.

# Iterirajte kroz sljedeću listu studenata i za svakog studenta
# stvorite objekt klase Student i dodajte ga u novu listu studenti_objekti:


class StudentType(TypedDict):
    ime: str
    prezime: str
    godine: int
    ocjene: list[int]


studenti: list[StudentType] = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]},
]


class Student:
    def __init__(self, ime: str, prezime: str, godine: int, ocjene: list[int]) -> None:
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self) -> float:
        return sum(self.ocjene) / len(self.ocjene)

    def __repr__(self) -> str:
        return (
            f"Student {self.ime} {self.prezime} ima najbolji prosjek {self.prosjek()}"
        )


studenti_objekti: list[Student] = [
    Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    for student in studenti
]

# actually saves an object to a variable
najbolji_student: Student = max(studenti_objekti, key=Student.prosjek)
# if __repr__ is not used, we get the object
# <__main__.Student object at 0x0000027CF43489D0>
print(najbolji_student)

# 4) Definirajte klasu Krug s atributom r.
# Dodajte metode opseg i povrsina koje će računati opseg i površinu kruga.

# Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.


class Krug:
    def __init__(self, r: int | float) -> None:
        self.r = r

    def opseg(self) -> float:
        return 2 * self.r * pi

    def povrsina(self) -> float:
        return self.r**2 * pi

    def __repr__(self) -> str:
        return f"Krug s radijusom od {self.r} ima povrsinu od {self.povrsina()} i opseg od {self.opseg()}"


krug = Krug(3)
print(krug)

# 5) Definirajte klasu Radnik s atributima ime, pozicija, placa.
# Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija}".

# Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department.
# Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".

# U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i povećava plaću radnika (Radnik) za iznos povecanje.

# Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i give_raise.


class Radnik:
    def __init__(self, ime: str, pozicija: str, placa: float) -> None:
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self) -> None:
        print(f"Radim na poziciji {self.pozicija}")

    def tell_pay(self) -> float:
        return self.placa


class Manager(Radnik):
    def __init__(self, ime: str, pozicija: str, placa: float, department: str):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self) -> None:
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik: Radnik, iznos: float) -> None:
        radnik.placa = radnik.placa + iznos


radnik = Radnik("Pero", "strojovoda", 950.20)
manager = Manager("Mirko", "Sef", 1200, "Odrzavanje")

radnik.work()
manager.work()
manager.give_raise(radnik, 137.45)
print(radnik.tell_pay())
