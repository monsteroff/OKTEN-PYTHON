###################################################
# Destrukturizasiya
###################################################

"""
# Destrukturizasiya
tuple_1 = (1, 2, 3, 4)

# a, b, c, d = tuple_1
print(a, b, c, d)
# a, _, c, d = tuple_1
print(a, _, c, d)
a, *_, d = tuple_1
print(a, _, d)
# altdan xett olanlari adeten istifade etmirler
"""
"""
lis = [1, 2, 3, 4]


def func(a, b, c, d):
    print(a, b, c, d)


func(*lis)
"""

"""
user = {
    'name': 'Orxan',
    'age': 29,
    'status': True
}


def func(name, age, status):
    print(name, str(age), status)


func(**user)
"""

###################################################
# Decorate
###################################################

"""
def decor(func):
    def inner():
        print('-'*20)
        func()
        print('-'*20)
    return inner


def greeting():
    print('hello')


decorated_func = decor(greeting)
decorated_func()

decor(greeting)()  # daha qisa variant
"""

"""
# eyni shey amma daha rahat
# dekoratorun hansi funksiyaya aid olmasini isteyirikse hemin funksiyadan evvel
# sadece @ isharesi ile dekoratorun adini qeyd edirik
# ve hemin funksiya cagrilanda dekorator onun uchun ishlemish olacaq
# decoratoru da decor etmek mumkundur yeni onna yuxarida da @ isharesi ile ...
def decor(func):
    def inner():
        print('-'*20)
        func()
        print('-'*20)
    return inner


def greeting():
    print('hello')


@decor
def sagollash():
    print('sagol')


greeting()
sagollash()
"""

"""
# dekorator vasitesi ile 'Hello_world_from_python' return eden funksiyani  
# altdan xett olan yerlerini boshluq ile evez edek
def decor(func):
    def inner(*args):
        return func(*args).replace('_', ' ')

    return inner


@decor
def salam(name):
    return f'Hello_my_name_is_{name}'


print(salam('Cahangir'))
"""

# dekorator vasitesi ile 'Hello_world_from_python' return eden funksiyani
# altdan xett olan yerlerini boshluq ile evez edek

###################################################
# Scope (Oblast vidimosti)
###################################################

# global deyishenlerimiz
# print(globals())


# local deyishenlerimiz
# def a():
#     name = 'Cahangir'
#     print(locals())
#
#
# a()

###################################################
# CLOSURE (ZAMIKANIE)
###################################################

"""
def saygac():
    say = 0

    def artir():
        nonlocal say
        say += 1
        return say

    return artir


saygac1 = saygac()
saygac2 = saygac()
print(saygac1())
print(saygac1())
print(saygac1())
print(saygac2())
print(saygac1())
print(saygac2())
"""

'''
############################## ORXAN MESELE

qarpiz = int(input('Qarpizin cekisini daxil edin : '))


def bol(gilemeyve):
    for i in range(1, gilemeyve + 1):
        dilim1 = i
        dilim2 = gilemeyve - dilim1
        if dilim2 != 0:
            print(dilim1, 'kq,', dilim2, 'kq')
            print('------------')
        if dilim1 % 2 == 0 and dilim2 % 2 == 0 and dilim2 != 0:
            return 'Qarpızı cüt hissələrə bölmək alındı'
    return 'Qarpızı cüt hissələrə bölmək alınmır'


print(bol(qarpiz))

# def bol(gilemeyve):
#     dilim1 = 0
#     while dilim1 <= gilemeyve-1:
#         dilim1 += 1
#         dilim2 = gilemeyve - dilim1
#         if dilim2 != 0:
#             print(dilim1, 'kq,', dilim2, 'kq')
#             print('------------')
#         if dilim1 % 2 == 0 and dilim2 % 2 == 0 and dilim2 != 0:
#             return 'Qarpızı cüt hissələrə bölmək alındı'
#     return 'Qarpızı cüt hissələrə bölmək alınmır'


# w = int(input('Qarpizin cekisini daxil edin : '))
# print('yes') if w % 2 == 0 and w > 2 else print('no')

'''

###################################################
# LAMBDA
###################################################


'''
def func(x, y):
    return x ** y


func_same_shit = lambda x, y: x ** y
'''

"""
users = [
    {
        'name': 'Cahangir',
        'age': 28,
        'status': True
    },
    {
        'name': 'Orxan',
        'age': 29,
        'status': True
    },
    {
        'name': 'Eldar',
        'age': 29,
        'status': False
    }
]

print(sorted(users, key=lambda x: x['age']))
"""


# ############ ############ ###########
# IMPORT YOLLARI
# ############ ############ ###########

'''
# import math
# import math as m
# from math import sqrt, cos, tan
# from math import *
# axirinci meslehet gorulmur cunki ola biler ki bizim yaratdigimiz 
# funksiyalarnan hemin libraryde olan funksiyalarin adi ust uste dushe biler
'''

###################################################
# TYPE HINTING (ANNOTACIYA TIPOV)
###################################################

'''
# bu bize misal ucun funksiya daxilinde ne ucun lazim ola biler
# parametr qebul edende name dedikde aydin meseledir ki biz ora STR tipli melumat gozleyirik
# amma python uchun bu melum deyil ve onu adi deyishen kimi gorur
# ve hemin name deyishenini funksiya daxilinde noqte ile davam etdirdikde onun tipini bilmediyi ucun
# bize lazimli funksiyalari dartmaya biler
# Bu meseleden qachmaq uchun ve hemishe lazimli metodlarin gelmesi ucun qebul etdiyimiz parametrlerin
# qarshisinda iki noqteden sonra onlarin tiplerini qeyd etmeliyik
# bundan elave funksiyalarda funksiyanin hansi tip melumat geri qaytardigini da qeyd etmek olar
# bunun ucun funksiya moterizesinden sonra ->int misal ucun qeyd etmek olar
# ashagidaki kodda tipleri annotasiya etdik  (tipizasiya etmedik), bize errora oxshar sheyler gosterse bele ishleyecek

def test(name: str)->int:
    return 'ddd'
print(test(111))
'''


'''
# tipleshdirme uchun xususi library var -> adi typingdir
from typing import List, Dict, Optional, Callable, Any

users: List[str] = [1, 2, 3, 4, 5]
user: Dict[str, Any] = {'name': 'Cahangir', 'age': 28}
print(users)
'''

'''
# python 3.9 dan etibaren typingden import etdiyimiz List ve Dict-e ehtiyac yoxdur
# onun yerine pythonun list ve dict-ini istifade ede bilerik
from typing import Optional, Callable, Any, Union

users: list[str] = [1, 2, 3, 4, 5]
user: dict[str, Any] = {'name': 'Cahangir', 'age': 28}
print(users)

# Optional -> ele funksiyalar var ki, onlar ya hansisa melumat ya da  None qaytarmali olur.
# Ve biz None de olsa qaytaririq. Bu meseleye Optional baxir.
# Ashagida bele alinir ki funksiya ya None ya da str tipli melumat qaytaracaq.

# Union -> ele bir funksiya yarada bilerem ki, funksiyaya YA bir tipli YAXUD diger tipli melumat gele biler
# Bu ishe Union baxir. Qeyd olunanlardan bashqa nese gonderilse onda warning gelecek


def test(name: Union[str, bool]) -> Optional[str]:
    return 'ddd'


print(test('111'))
'''

'''
# Python 3.10 dan etibaren ise funksiyani ashagidaki kimi qeyd elemek olar
# Yeni union ve optionali misal ucun yigishdirib | isharesi ile ya yada qeyd elemek olur.
from typing import Callable, Any

# Callable meselesine gelende ise
# Callable funksiya daxilinde funksiyaya aiddir ve Yuxari funksiyanin Funksiya qaytaracagini teleb edir
# Bundan elave Iceri funksiyanin ne qebul etdiyini ve ne qaytaracagini qeyd etmek mumkundur.


def test(name: str | bool) -> Callable[[str, int], str]:
    def inner(s: str, i: int) -> str:
        return 'Hello'
    return inner


print(test('111'))
'''
