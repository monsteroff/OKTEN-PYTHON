# asdasd

"""
asdasd
"""

'''
asdasd
'''

# print('salam')
# print(1, 2, 3, 4, 5, 6, sep='-')
# print(1, 2, 3, 4, 5, 6, sep='-', end='___')
# print('salam2')
#
# i = 5
# f = 1.3
# b = True  # False
# s = 'salam'  # "salam"
# n = None

# names used to be snake case
# some_variable = 'some variable'
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# from_int_to_string = str(i)
# print(type(from_int_to_string))
# print(from_int_to_string)

# int() float() bool() str()

# a = 8
# print(a)
# a = 'sss'
# print(a)

# a = 5
# b = 4
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)  # bolme zamani tam reqem alinarsa bele hemishe float aliriq misal uchun 5/5 = 1.0
# print(a // b)  # birbasha tam reqem almaq uchun bele yazmaq olar (noqteden sonraki sadece silinir) 5/4 = 1.25 1.25 => 1
# print(round(4.5))  # round bank sistemi ile yuvarlaqlashdirmadi (x.5 alinarsa en yaxin cut reqeme teref yuvarlaqlashdirir)
# print(round(5.5))
# print(a ** b)
# print(a % b)


'''
# gozel sual 1: print(5 / 5)  Ekrana ne cixacaq (yazili shekilde qeyd edin)
# gozel sual 2: print(type(a / b))  a=4 b=4 Ekrana ne cixacaq
# gozel sual 3: print(round(4.5))  Ekrana ne cixacaq
'''

# s = input('Enter num: ')
# print(type(s))

'''
inputdan reqem yoxlanishi

s = input('Bura bir reqem yazin: ')


def reqem(yazilan):
    try:
        print(int(yazilan))
    except ValueError:
        print('reqem deyil')


reqem(s)
'''

# a = 5
# b = 4
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)
# print(a == b)  # deyerlerin beraber oldugunu yoxlayir
# print(a is b)  # eyni obyekte ssilka olub olmadigini yoxlayir (yaddashda olan unvani yoxlayir)
# print(a != b)
# print(a is not b)

'''
misal uchun bele:
x = [1]
c = x
d = [1]  # bura da x yazsaq her iki cavab True olacaq 
print(c == d)
print(c is d)
'''

# print(isinstance('5', int))

'''
a = 4
b = 5
if a == 4:
    pass
elif a < b:
    print('A kickidir B')
elif a == b:
    print('A beraberdir B')
else:
    print('A boyukdur B')
'''

'''
a = 5
b = 4

# if (b > a and a > 1) or b == 6:
if (b > a > 1) or b == 6:
    print('shertler odendi')
'''

# ternar operator | inline  if
'''
num = int(input('num: '))
result = 'yes' if num > 5 else 'no'
print(result)
'''

###########################################################
# list
###########################################################
"""
L = [1, 2, 3, 'sss', True]
print(L[0])
print(L[-1])
print(L[9])  # bu ikisi movcud deyil / error olacaq (JS-de undefined verecekdi)
print(L[-6])
L[-1] = 'last'
del L[2]
print(L)
"""

'''
A = [1, 2, 3, 4, 5]
B = [a for a in A]
C = A
D = A.copy()

B[0] = 55
C[-1] = 88

print(A)
print(B)
print(C)
print(D)
'''

"""
A = [1, 2, 3, 4, 5]
print(A)

A.append(6)
print(A)

A.insert(-8, 111)  # index, value   olan indeksden boyukdurse errorsuz  en axira dushecek, menfi terefe eyni shey
print(A)

# indeksle silme
popped = A.pop()  # moterizeye hecne qeyd etmeyende axirincini silir
print(A)
print(popped)
# value ile silme
A.remove(3)
print(A)

B = [12, 13, 14]
A.extend(B)  # A = A + B de elemek olar, ishleyecek lap qisa A += B
print(A)

# index axtarishi
print(A.index(111))
# hecne tapmasa  xeta gosterecek
# mueyyen yerden start yaxud stop vermek olur
# pycharmnan komek lazim olanda metodun moterizesinin icinde ctrl + P basib mumkun variantlara baxmaq olar
# bu shekilde => A.index(value, start) yaxud A.index(value, start, stop)
print(A.index(4, 2, -1))

# massivi dondermek
A.reverse()

# siralama
A.sort()

# tersine siralama
A.sort(reverse=True)

# mueyyen deyerin sayini gostermek
print(A.count(5))
"""

'''
# listin 0-cidan (0 daxil) 3-cu indekse qeder olan deyerlerin yeni liste yazilmasi
L = [1, 2, 3, 4, 5]
L_2 = L[0: 3]
# 0-i yazmaya bilerik L_2 = L[: 3] bele
# 2 den sona qeder isteyirikse L_2 = L[2:] bele
# evvelden sona qeder isteyirikse L_2 = L[:] bele
# evvelden sona qeder isteyirikse amma addim iki iki olsun L_2 = L[::2] bele
print(L_2)
# tersine 3 deneden 1
print([1, 2, 3, 4, 5][::-3])
print(len(l_2))
# listi bele de yaratmaq mumkundur
list()
'''
###########################################################
# Tuple (Kortej)
###########################################################
'''
# deyishilmesi icaze verilmeyen listdir
# yaradilanda moterize qoymaq vacib deyil
# count ve index metodlari var
# elave hecne yazmaq yaxud silmek mumkun deyil
# tuple liste nisbeten daha az yer tutur
# yaddashin ekonomiyasi ucun backendde qebul elediyimiz melumatlar tuple sheklinde olur
# yaratmaq uchun hemchinin tuple() funksiyasi movcuddur
t = (2,)
print(type(t))
print(t)
t2 = 2,
print(type(t2))
print(t2)
t3 = 1, 2, 3, 4, 5, 4
print(type(t3))
print(t3)
print(t3.count(4))
print(t3.index(4))
l3 = [1, 2, 3, 4, 5, 4]
print(t3.__sizeof__())
print(l3.__sizeof__())
'''
###########################################################
# Dictionary
###########################################################
'''
# ACHAR olaraq dictionary ve listden bashqa her shey ola biler misal uchun int yaxud string
# esasen string olur
# DEYER ise her shey ola biler
d = {
    'name': 'Cahangir',
    'age': 28,
    'status': True
}
print(d['name'])
# olmayan bir key chagirsag error dushur
# erroru kechmek uchun alternativ yol var. Bu halda achar olmasa None qayidacaq
print(d.get('name'))
# print(d.get('name1'))
# olmadigi halda -> yeni None qayitdigi halda yerine diger shey qebul ede bilerik misal ucun:
print(d.get('name1', 'Orxan'))

# Metodlari
d.clear()  # tam temizleme
d.copy()  # kopyalama
d.pop('name')  # achar vasitesi ile
d.pop('name1', None)  # eger yoxdursa error atmasin
d.setdefault('name', 'Eldar')  # Eger misal ucun name yoxdursa yerine Eldar qeyd edecek
# ve eger qeyd olunan xana movcud deyilse : misalucun name1 yazsaydiq
# onda yeni xana yaradilacaqdir
d.popitem()  # sondan silme (return var) Tuple kimi qayidir ('status', True)  misalcun bele
d.keys()  # acharlarini goster dict_keys([........]) bu shekilde gelecek
# lazim olarsa list(d.keys()) kimi yazib rahat liste kechire bilerik
d.items()  # deyerleri gostermek list(d.items()) eyni sohbet
d.update(house=34)  # yenisini elave etmek yaxud kohnesini deyishmek
d.update([('house', 34)]) # yenisini elave etmek yaxud kohnesini deyishmek 2-ci variant
d.update([('name', 'Baxa'), ('house', 34)])  # bir neche dene de elemek olar
dict()  # cast etmek uchun funksiya deyilir
'''
###########################################################
# Set
###########################################################
'''
# Setde ardicilliq yoxdur (sort yoxdur) (sira olmadigi ucun indeks de yoxdur)
# eger eyni deyerler salsaq ichine dublikatlar silinecek
# bosh olaraq yazsaq set yaratmaq alinmayacaq ele bilecek ki dictionarydir => set1 = {} <= dictionary
# amma yene de bosh yaratmaq istesek bu shekilde yazmaq lazimdi set1 = set()
# bu shekilde ichini de doldurmaq olar amma MENASIZDIR set1 = set([1, 2, 3, 4, 5])
set1 = {1, 2, 3, 4, 5, 2, 2}  # bu ise artiq setdir (2-ler tekrar oldugu ucun ancaq biri qalacaq)
set2 = {1, 2, 3, 4, 6}

# METODLAR
set1.update(set2)  # iki seti birleshrimek uchun
set1.add(55)  # nese elave etmek (tekrar olarsa aydin meseledir elave olmayacaq)
set1.remove(2)  # silmek (olmasa error VERIR)
set1.discard(123123)  # silmek (olmasa error VERMIR)
set1.pop()  # en bash elementi silir ve sildiyini geri qaytara bilir ??? en bash elementin ne oldugunu basha dushmedim
print(set1.issuperset(set2))  # True False qaytarir set2 elementlerin set1-in ichinde tam olaraq oldugunu yoxlamaq uchundur
print(set1.issubset(set2))  # True False qaytarir amma tersine mentiqle
print(set1.isdisjoint(set2))  # True False qaytarir mentiq : tam ferqli olarsa True
print(set1.intersection(set2))  # eyni olan elementleri qaytarir
print(set1.difference(set2))  # ferqli olan elemetleri (1-cide olub 2-cide olmayan)
print(set1)  # setlerden az istifade olunur, adeten eyni elementleri aradan qaldirmaq lazim olanda istifade olunur
'''

###########################################################
# String
###########################################################

# string1 = "Orxan \"lordbaku\" Heyderli - '29' yashi var '"  # ( \" ) => " isharesinin ekranizasiyasi demekdir
# string2 = r"asd\\\\asd"  # r'' raw string demekdir

# name = 'Max'
# age = 66
# weight = 70.5

# string = name + str(age) + str(weight)
# string = 'Hello my name is %s, I"m %d, and my weight is %f' % (name, age, weight)
# string = 'Hello my name is {}, I"m {}, and my weight is {}'.format(name, age, weight)
# string = 'Hello my name is {0}, I"m {1}, and my weight is {2}'.format(name, age, weight)
# string = 'Hello my name is {name}, I"m {age}, and my weight is {weight}'.format(name=name, age=age, weight=weight)
# string = f'Hello my name is {name}, I"m {age}, and my weight is {weight}'
# print(string)

# string = 'Hello World'
# print('from 0 till 4 string: ', string[:4])
# print('index of l: ', string.index('l'))
# print('index of llo: ', string.index('llo'))  # yoxdursa error verecek
# print('find ez: ', string.find('ez'))  # yoxdursa -1 qaytaracaq
# print('count of l in str: ', string.count('l'))
# print(string.capitalize())
# print(string.upper())
# print(string.isupper())
# print(string.lower())
# print(string.islower())
# print(string.title())  # Her sozun birinci herifini boyuk eleyir
# print(string.swapcase())  # Balaca boyuk yerlerini deyish

# print(''.isspace())  # probel olub olmadigini yoxlamaq
# print('asdasd'.isalpha())  # herif olub olmadigi yoxla
# print('1111'.isdigit())  # reqem olub olmadigi
# print('11555asd'.isalnum())  # simvol olarsa false (ancaq reqem ve herf)
# print('123123'.startswith('23'))  # qeyd olunan deyerle bashladigini yoxlayir
# print('123123'.endswith('23'))  # qeyd olunan deyerle bitdiyini yoxlayir

# print('    salam  ---  '.strip())  # problelleri sagdan soldan yigishdirmaq
# print('    salam  ---  '.strip(' -'))  # problelleri ve defisleri sagdan soldan yigishdirmaq
# print('    salam  ---  '.rstrip(' -'))  # eyni shey sag terefden
# print('    salam  ---  '.lstrip(' -'))  # eyni shey sol terefden

# print('intelMx'.removesuffix('Mx'))  # Python 3.9 dan etibaren var
# print('intelMx'.removeprefix('intel'))

# print('Hello World'.split())
# print('Hello-World'.split('-'))
# print('Hello is World'.partition('is'))

# print('-'.join(['hello', 'world']))  # birleshdirmek

# print('Hello World'.replace('l', 'b'))

###########################################################
# Elaveler
###########################################################

# print(min([2, 4, 12, -1]))
# print(max([2, 4, 12, -1]))
# print(sorted([2, 4, 12, -1], reverse=True))
# print(pow(2, 25))  # 2 ustu 25

'''
i = 5
while i > 0:
    print(i)
    i -= 1
else:  # while bitdikde ishe dushecek (ishlemese bele)
    print('finish')
'''
'''
# for i in [1, 3, 4]:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(3, 10, 2):  # (start, stop, addim)
#     print(i)

# for i in range(10, 0, -2):  # (start, stop, addim)
#     print(i)
# else:
#     print('finish', i)

# print(3 in [1, 2, 3, 4, 5])  # ichinde hansisa deyerin olub olmamasini yoxlamaq
'''


'''
# dictionary for
d = {
    'name': 'Orxan',
    'age': 29,
    'city': 'Baku'
}

for k, v in d.items():
    print(k, ':', v)
'''

###########################################################
# Funksiyalar
###########################################################

'''
# *args ashagidaki halda 3-cu den sonra olan butun diger deyerler (tuple sheklinde dushecek funksiyaya)
# **kwargs ashagidaki halda argsdan sonra olan butun adli deyishenler (dictionary sheklinde)
def some_func(a, b, c=5, *args, **kwargs):
    print('Hello World')
    print(a, b, c, args, kwargs)
    return 5


some_func(1, 2)  # js dan ferqli olaraq funksiyani ancaq yaratdiqdan sonra cagira bilersen
func = some_func(1, 2, 8, 3, 5, 2, 2, 16, name='Orxan', age=29)

print(func)
'''

###########################################################
# List Comprehension
###########################################################
# a = [i for i in range(1, 11)]
# print(a)

# base_list = [1, 2, 3, 4, 5, 6, 7, 8]
# filtered = [i for i in base_list if i % 2 == 0]  # JS filter
# print(filtered)
# mapped = [i**2 for i in base_list]  # JS map
# print(mapped)
# mapped2 = ['cut' if i % 2 == 0 else 'tek' for i in base_list]  # JS map
# print(mapped2)


'''
# lists_in_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# res = [j for i in lists_in_list for j in i]
# print(res)
'''

'''
# Daha uzun
# lists_in_list = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
# res = [j for i in lists_in_list for j in i]
# res2 = [j for i in res for j in i]
# print(res2)
'''


'''
# Normal for
lists_in_list = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
res = []
for x in lists_in_list:
    for y in x:
        for z in y:
            res.append(z)
print(res)
'''

'''
# Bir defeye daha uzun olan
lists_in_list = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
a = [z for x in lists_in_list for y in x for z in y]
print(a)
# basha dushmesen yuxaridaki  normala bax ve yanbayan qoymaga calish
'''
