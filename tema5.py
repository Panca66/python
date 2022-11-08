#ex1
def suma_nr(a,b):
    return a+b
print(suma_nr(2,24))

#ex2
def nr_par(numar):
    if numar%2 == 0:
        return True
    else:
        return False
print(nr_par(18))

#ex3
def nr_caractere(nume,prenume,nume_mijlociu):
    return len(nume)+len(prenume)+len(nume_mijlociu)
print(nr_caractere('paval', 'anca', 'georgiana'))

#ex4
def arie_dreptunghi(L,l):
    return L*l
print(arie_dreptunghi(8,5))

# ex 5
def arie_cerc(raza):
    return 3.14*raza
print(arie_cerc(10))

#ex6
def find_caracter(x):
    if x in my_str:
        return True
    else:
        return False
my_str = 'Ana are mere'
print(find_caracter('o'))

#ex7
# def MyCounter(string):
#     lower = 0
#     upper = 0
#     for letter in string:
#         if(letter.islower()):
#             lower +=1
#         elif(letter.isupper()):
#             upper+=1
#     print(f'Nr de caractere lower case este {lower}',
#         f'Nr de caractere upper case este {upper}')
# string = input('Sirul este: ')
# MyCounter(string)

#ex8
def numere_pozitive(my_list):
    positive_list = []
    for i in my_list:
        if i > 0 :
            positive_list.append(i)
    return positive_list
lista1 = [1, -5, 6, 4, -8]
print(numere_pozitive(lista1))

#ex9
def compare_numbers(a,b):
    if a==b:
        print(f'Numerele sunt egale')
    elif a>b:
        print(f'Primul numar {a} este mai mare decat al doilea numar {b}.')
    else:
        print(f'Al doilea numar {b} este mai mare decat primul numar {a}.')
print(compare_numbers(8,8))

#ex10
def my_function(x, s={}):
    if x in s:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
    else:
        s.add(x)
        print('Am adaugat numarul nou in set.')
        return True
x = 4
s = {1, 2, 3, 4, 5}
print(my_function(x, s))

#ex11
month = input('Doresc sa stiu nr de zile pt luna ...')
def days_in_months(month):
    days_months = {"Ianuarie": 31, "Februarie": 28, "Martie": 31, "Aprilie": 30,
                   "Mai": 31, "Iunie": 30, "Iulie": 31, "August": 31, "Septembrie": 30,
                   "Octombrie": 31, "Noiembrie": 30, "Decembrie": 31}

    return days_months.get(month.capitalize())
print(days_in_months(month))

#ex 12
def calculator(x,y):
    a = x+y
    print(f'Suma: {a}')
    b = x-y
    print(f"Diferenta : {b}")
    c = x*y
    print(f'Inmultirea : {c}')
    d = x/y
    print(f"Impartirea : {d}")
print(calculator(10,2))

#ex 14

def val_max (a,b,c):
    return max(a,b,c)

print(f"Numarul cel mai mare este {val_max(10, 55, 78)}")

#ex 15
def suma_nr():
    x = int(input("Numarul este : "))
    sum = 0
    for x in range(0, x+1):
        sum = sum + x
    print(f" Suma tuturor numerelor pana la numarul ales {x} este : {sum}")
print(suma_nr())

#ex 16

def intersect(a,b):
    return list(set(a) & set(b))
l1 = [1, 1, 2, 3, 3]
l2 = [2, 2, 3, 4]
print(intersect(l1, l2))

#ex

from datetime import datetime
Current_datetime = datetime.now()
print("Data si ora exacta :", Current_datetime)

import pytz
Current_date_China = datetime.now(pytz.timezone('Asia/Shanghai'))
print("Data si ora in China este : ", Current_date_China)

#ex 19

import datetime
today = datetime.date.today()
Christmas_date = datetime.date(2022, 12, 25)
diff = Christmas_date - today
print(diff)






















