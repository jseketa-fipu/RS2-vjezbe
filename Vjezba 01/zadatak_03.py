import math
from typing import TypedDict

# 1) even number [20, 50] squared
even_numbers_squared: list[int] = [n * n for n in range(20, 51, 1) if n % 2 == 0]
print(
    even_numbers_squared
)  # [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]

# 2) list of the length of strings that contain letter 'a'
words = [
    "jabuka",
    "pas",
    "knjiga",
    "zvijezda",
    "prijatelj",
    "zvuk",
    "čokolada",
    "ples",
    "pjesma",
    "otorinolaringolog",
]
lengths_with_letter_a = [len(r) for r in words if "a" in r]
print(lengths_with_letter_a)  # [6, 3, 6, 8, 9, 8, 6, 17]

# 3) List of dictionaries {n: n**3 if odd number, else n} for n [1, 10]
cubed: list[dict[int, int]] = [{n: (n**3 if n % 2 else n)} for n in range(1, 11, 1)]
print(
    cubed
)  # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9: 729}, {10: 10}]

# 4) Dictionary comprehension: square root for numbers in [50, 500], step 50.
# Numbers are keys, square roots are values to two decimals.


square_roots = {n: round(math.sqrt(n), 2) for n in range(50, 501, 50)}
print(
    square_roots
)  # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32, 350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}


# Mypy thinks each student is just dict[str, object], so student["bodovi"] is Sequence[object] instead of list[int]. Give it types.
# custom class for a student to use as a type, so the mypy is happy
# if you are squeamish about using a full blown class, you can use
# list[dict[str, Any]]


class Student(TypedDict):
    ime: str
    prezime: str
    bodovi: list[int]


# 5) Surnames are keys, sum of numbers are values. Let it be a list of dicts.
studenti: list[Student] = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]},
]
summed_points = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]
print(
    summed_points
)  # [{'Ivić': 152}, {'Marković': 127}, {'Anić': 55}, {'Petrić': 362}, {'Ivić': 236}, {'Matić': 266}]
