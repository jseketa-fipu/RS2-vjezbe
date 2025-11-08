# Exercise 01 - task 01 lambda functions

# PEP-8 recommendation:
# https://peps.python.org/pep-0008/#programming-recommendations
# Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier:
# # Correct:
# def f(x): return 2*x

# # Wrong:
# f = lambda x: 2*x

# The first form means that the name of the resulting function object is
# specifically ‘f’ instead of the generic ‘<lambda>’.
# This is more useful for tracebacks and string representations in general.
# The use of the assignment statement eliminates the sole benefit a lambda
# expression can offer over an explicit def statement (i.e. that it can be
# embedded inside a larger expression)


# 1) square the number
def square():
    return lambda x: x**2


kvadriraj = square()


# 2) sum two numbers and square the sum
def sum_then_square():
    return lambda a, b: (a + b) ** 2


zbroji_pa_kvadriraj = sum_then_square()


# 3) square the length of a string
def square_length():
    return lambda string: len(string) ** 2


kvadriraj_duljinu = square_length()


# 4) multiply y by 5 and then raise it to x
def multiply_and_raise():
    return lambda x, y: (y * 5) ** x


pomnozi_i_potenciraj = multiply_and_raise()


# 5) return True if number even, else return None
def even_number():
    return lambda x: True if x % 2 == 0 else None


paran_broj = even_number()

print("\n")
print(kvadriraj(5))
print(zbroji_pa_kvadriraj(2, 3))
print(kvadriraj_duljinu("duljina niza"))
print(pomnozi_i_potenciraj(10, 3))
print(paran_broj(13))
