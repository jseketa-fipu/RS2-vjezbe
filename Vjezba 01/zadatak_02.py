# Exercise 01 - task 02
from typing import TypedDict

# 1) map + lambda: kvadriraj duljine nizova
# map(function, iterables)
list_of_strings: list[str] = ["jabuka", "kruška", "banana", "naranča"]
squared_lengths: list[int] = list(map(lambda s: len(s) ** 2, list_of_strings))
print(squared_lengths)  # [36, 36, 36, 49]

# 2) filter + lambda: contains numbers > 5
numbers = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # [21, 33, 45, 9, 10]

# 3) map + lambda → dict: {number: number**2} (do not use comprehension)
numbers = [10, 5, 12, 15, 20]
transform = dict(map(lambda x: (x, x * x), numbers))
print(transform)  # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

# 4) all + map + lambda: are all over 18?
# Mypy thinks each student is just dict[str, object], so student["godine"] is Sequence[object] instead of int.
# Give it types.
# custom class for a student to use as a type, so the mypy is happy
# if you are squeamish about using a full blown class, you can use
# list[dict[str, Any]]


class Student(TypedDict):
    ime: str
    prezime: str
    godine: int


students: list[Student] = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18},
]
all_over_18 = all(map(lambda student: student["godine"] >= 18, students))
print(all_over_18)  # False

# 5) filter + lambda: words longer then 12 characters
rijeci = [
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

min_length = int(input("Unesite minimalnu duljinu riječi: "))
long_words = list(filter(lambda r: len(r) > min_length, rijeci))
print(long_words)
# za 7 -> ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
# za 12 -> ['otorinolaringolog']
