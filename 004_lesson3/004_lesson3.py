#########################################
# # Class
#########################################

"""
# # JS da oldugu kimi classlari yaratmag ucun class achar sozunden istifade olunur
# # Classlarin adi CamelCase ile ilk herfi boyuk olaraq qeyd olunmalidir
# # Butun classlar object-den miraslanir(nasleduetsya). object esas classdir (balaca herifle yazildigina baxmayaraq)
# # Pythonun mueyyen versiyasindan sonra sinif yaratdiqda onun moterizesini ve moterize daxilinde (object)
# # yazmagimiz artiq vacib olmadigini bilmeliyik.
# # class User(object):         <- bele yazilirdi evvel
# # indi python ozu basha dushur ki o objectden miraslanir ona gore yazmaga ehtyac yoxdur.

class User:
    __count = 0
    # __slots__ = 'name', 'age'

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        User.__count += 1

    def get_count(self):
        return User.__count

# # classin exemplyarini yaradaq
# # JS den ferqli olaraq hec bir achar sozunden istifade etmek lazim deyil (new User() kimi)


user1 = User('Cahangir', 28)
user2 = User('Orxan', 29)
# User.count += 10
# # User sinfinin icindeki count deyisheni statik oldugu ucun , hemin deyishene birbasha noqte ile muraciet ede bilerik
# print(User.count)
# # classin exemplyari vasitesi ile de hemin counta muraciet etmek olar (amma bele etmek duzgun deyil, yeni meslehet deyil)
# print(user1.count)
# # qisa olaraq count deyisheni User sinfine mensub olan butun exemplyarlar ucun umumi deyishendir. (statikdir)
# # bes bu halda bu sinife mensub olan exemplyarlari bir birinden nece ayiraq
# # bunun ucun burada konstruktorlar movcuddur
# # konstruktorlar sinif daxilinde funksiya sheklinde qeyd olunur.
# # pythonda buna bashqa cur MAGIC METHODS deyirler.
# # sinif daxilinde yazilan butun funksiyalara metod deyilir.
# # konstruktor sistem metodlarina daxildir. (hemin bayaq dediyimiz ana sinifin yeni (object)-in metodlaridir)
# # qisa olaraq sistem(bizim halda object) metodlarina MAGIC METODLARI DEYILIR
# print(user1)
# print(user1.__dict__)
# user1.id = 1
# print(user1.__dict__)
# del user1.id
# print(user1.__dict__)

# # user1 i print etdikde yaddashdaki yerini ve obyekt oldugunu goruruk
# # normal shekilde gostermek ucun .__dict__ magic metodunu cagiririq
# # gorduyumuz kimi yuxarida biz user1-e id elave eledik ve sonra onu sildik.
# # bunun qarshisini almaq uchun sinife __slots__ deyishenini elave edek.
# # __slots__ un daxilinde exemplyarin hansi deyishenleri olacagini deqiq qeyd edirik ki sonradan ora hecne elave edib
# # silmek olmasin
# # __slots__ tuple qebul edir (moterizeleri yazmasaq da olar)
# # __slots__ u qeyd elediyimiz ucun yuxaridaki user1.id = 1 artiq ishlemeyecek
# # ona gore onlari kommente atiram

# # note : self classin exemplyarinin ssilkasidir
"""

##################################################
# # PRIVATLIQ
##################################################
"""
# # modifikatori dostupa (3 tipa est)
# # ICAZE MODIFIKATORlarinin 3 tipi var
# # (default public dir)  count = 0           count qarhisinda hecne qeyd etmedikde default olaraq public olur
# # __count = 0 (private etdik)  qarshisinda 2 altdan xett olan deyishenler private dir
# # PRIVATE deyishenlerin menasi nedir?
# # bu deyishenler yalniz sinif daxilinde istifade oluna biler
# # yeni onlara sinifden kenar muraciet ederek baxmaq olmur
# # bununla ne ede bilerik (__count) ile. misal ucun her user exemplyari yaradilanda hemin countu artira bilerik
# # bunu konstuktor daxilinde ede bilerik (cunki userin exemplyarinin yaradilmasi anı konstruktorda bash verir)
# # bes sonra Userlerin sayina nece baxa bilerik ?
# # gel sinif daxilinde bunun ucun xusasi funksiya yaradaq (bu funksiya sadece User sinfine aid olan countu qaytaracaq)
# # Bu ne ilese closure(zamikaniyeye) oxshayir. __count deyisheni User sinfinin daxilinde yashayir.
# # ve hemin deyishene exemplarin icinden yalniz xususi metod vasitesi ile muraciet ede bilerik
# print(user2.get_count())
# # Bundan elave PROTECTED tipi de var o ise _count kimi qeyd olunur.
# # PROTECTED-in PRIVATE den ferqi odur ki, PROTECTEDI varis siniflere de gondermek mumkundur
# # bir dene emma var -> bele halda print(User._count) desek bize cavab gosterecek (warning falan vermeyine baxmayaraq)

# # Umumiyyetle qeyd edilenler yeni privatliq ve s. proqramcilar arasinda sadece saazish kimi bir sheydi
# # Cunki bize lazim olsa biz yene de hemin PRIVATE deyishenleri dartib cixara bilerik
# # Ashagida bunu nece elemek mumkun oldugunu gosterirem warning falan olduguna baxmayin yene de ishleyir
# print(User._User__count)
# # Ona gore privatliq sinifler daxilinde yalniz -> sinife muraciet etdikde noqteden sonra hemin deyishenin
# # gorsenmemesi ucun istifade olunur

"""

##################################################
# # Inheritance (Nasledovanie)
##################################################
"""
class SuperUser:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class SomeTools:

    def salam(self):
        return 'Salam'

    def salam2(self):
        return 'Salam2'


# # Eger SimpleUser sinfi 2 sinifin varisidirse adeten ikinci sinif sadece elave funksionalliq uchundur
# # Misal ucun SomeTools sadece 'Salam' stringini geri qaytarir
class SimpleUser(SuperUser, SomeTools):
    def __init__(self, name: str, age: int, house: list):
        super().__init__(name, age)
        self.house = house


simple_user1 = SimpleUser('Cahangir', 27, [1, 2, 3, 4])

print(simple_user1.__dict__)
print(simple_user1.salam())
"""

#########################################
# # Incapsulation
#########################################
"""
# # nece ki bizde privatliq var, inkapsulyasiya bizde her hansisa metodlar vasitesi ile
# # melumatlari get yaxud set ede bilerik
# # Gel konstruktorda olan deyishenleri de privat edek ki onlara exemplyara muraciet etdikte bele
# # deyishenleri darta bilmeyek


# class User:
#     def __init__(self, name: str, age: int):
#         self.__age = age
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, new_name: str):
#         self.__name = new_name
#
#     def delete_name(self):
#         del self.__name
#
#
# simp1 = User('Cahangir', 28)
# print(simp1.get_name())
# simp1.set_name('Orxan')
# print(simp1.get_name())
# simp1.delete_name()
# print(simp1.__dict__)

# # bu cox gozel variant olmadigindan daha yaxshisini fikirleshibler
# # her bir metodu da private edek
# # private edenden sonra ele alinir ki indi artiq hec neyi deyishe bilmirik ve goture bilmirik
# # bu halda properti bizim komeyimize gelir (property() evvelceden qurashdirilmish funksiyadir)
# # sinifdaxilinde name deyishenini yaradaq ve ora property funksiyasini qeyd olunan parametrlerle menimsedek

# -----------------------------------------------

# class User2:
#     def __init__(self, name: str, age: int):
#         self.__age = age
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __set_name(self, new_name: str):
#         if not len(new_name) < 5:
#             self.__name = new_name
#         else:
#             print('zehmet olmasa adin uzunluguna diqqet edin minimum 5 herif olmalidir')
#
#     def __delete_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User2('Cahangir', 28)
# print(user.name)
# user.name = 'Orxan'
# print(user.name)
# del user.name
# print(user.__dict__)

# # bunlar(yeni getter ve setterler) bizim umumiyyetle neyimize gerekdir?
# # cavab : yoxlamalar etmek ucun
# # misal ucun userimizin adini set eleyende adin uzunlugu 5 simvoldan az olduqda set ede bilek
# # funksiya daxilinde bunu yazdiq, ve indi user.name = 'Orxa' qeyd etsek adi deyishmek mumkun olmayacaq

# # amma hetta bu, cox da rahat deyil
# # bunu biraz da sadeleshdiribler

# -----------------------------------------------

# # her bir funksiyamizin adini name qoyuruq (nameye aid olanlari elbetde)
# # getterin ustunde sira ile @property / setterin ustunde @deyishen.setter / deleterin ustunde @deyishen.deleter yaziriq
# class User2:
#     def __init__(self, name: str, age: int):
#         self.__age = age
#         self.__name = name
# 
#     @property
#     def name(self):
#         return self.__name
# 
#     @name.setter
#     def name(self, new_name: str):
#         if not len(new_name) < 5:
#             self.__name = new_name
#         else:
#             print('zehmet olmasa adin uzunluguna diqqet edin minimum 5 herif olmalidir')
# 
#     @name.deleter
#     def name(self):
#         del self.__name
# 
# 
# user = User2('Cahangir', 28)
# print(user.name)
# user.name = 'Orxan'
# print(user.name)
# del user.name
# print(user.__dict__)
"""

#########################################
# # Abstract classes / POLIMORFIZM  (her iki movzu burada var)
#########################################
"""
# pythonda abstrakt sinifler movcuddur
# bu ozunde hec bir melumat dashimayan siniflerdir
# sadece ne etmek lazim oldugunu gostermek ucundur
# TypeScriptdeki interfeys metodlara oxshayir
# bunun ucun bize xususi kitabxana lazimdir -> abc (abstract basic class)

# ashagidaki kimi misal uchun Shape abstrakt klassini yaradaq
# ve onun daxilinde abstrakt metodlar yaradaq (onlar bu classda hecne etmeyecek yeni pass)

# bundan sonra Shape sinifinden varis olan diger siniflerde Shape sinifinde olan metodlar olmasa warning olur
# yeni biz artiq mecburuq ki hemin metodlar orda yaradilsin

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectange(Shape):

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a*2 + self.b*2

    def area(self):
        return self.a * self.b


class Triangle(Shape):

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        triange_area = (semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (
                    semi_perimeter - self.c)) ** 0.5
        if float(triange_area.real) == 0:
            return 'Bele ucbucaq mumkun deyil, ucbucagin istenilen 2 terefinin cemi 3-cu terefden boyuk olmalidir'
        return self.a + self.b + self.c

    def area(self):
        # Herons formula
        semi_perimeter = (self.a + self.b + self.c) / 2
        triange_area = (semi_perimeter*(semi_perimeter-self.a)*(semi_perimeter-self.b)*(semi_perimeter-self.c)) ** 0.5
        if float(triange_area.real) == 0:
            return 'Bele ucbucaq mumkun deyil, ucbucagin istenilen 2 terefinin cemi 3-cu terefden boyuk olmalidir'
        return float("{:.2f}".format(triange_area.real))


shapes: list[Shape] = [Rectange(2, 4), Triangle(5, 3, 2), Rectange(4, 8), Triangle(2, 3, 2)]

for shape in shapes:
    print('Class :', shape.__class__.__name__)
    print('Area :', shape.area())
    print('Perimeter :', shape.perimeter())

                    ##### 42-ci ceqiqe video ######
                    
# # eslinde ise oz abstrakt siniflerimizden adeten istifade etmeyeceyik ( framework ve kitabxanalarda hazir olanlar var)
# # sadece abstrakt siniflerin megzini oyrendik
# # import elediyimiz abstractmethod-a baxdiq
# # baxacagimiz 2-si de var (classmethod, staticmethod)

class User:
    __count = 0

    def __init__(self, name: str):
        self.name = name
        User.__count += 1

    # # eger misal ucun ashagidaki greetin metodunda bize self lazim olmayacaqsa bele metodu statik elemek lazimdir
    @staticmethod
    def greeting():
        print('Hello')

    # # classmethod adeten classin deyishenlerine  muraciet edende istifade olunur
    # # bizim halda bu __count oldu
    # # get_count metodunun icinde gorduyunuz kimi artiq cls qebul etdik
    # # cls Hemin cari classin deyishenidir.
    @classmethod
    def get_count(cls):
        return cls.__count

# # sinife muraciet etdikde staticmethodlari, classmethodlari
# # exemplyara muraciet etdikde staticmethodlari, classmethodlari cagira bilirik
# # amma exeplyardan classmethodlari cagirmaq yaxshi praktika deyil.
"""


#########################################
# # Pereqruzka metodov
#########################################
"""
# mi mojem zrobiti yakis povedinok na yakis zovneshniy faktor yakiy bude vplivati na ekzemplyari klassu
# i ce vse robitsya z dopomohoyu magic metodiv


class User:
    __instance = None

    # # 4
    # # __new__ : konstruktordan evvel yazilir.
    # # single tone deyilen pattern movcuddur. mentiqi : classin yegane exemplarini yaradir
    # # nece eleyirsiz eleyin siz her zaman sinifin yegane exemplyarini elde edeceksiniz
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    # # __isinstance deyishenini bu merhelede yaratdim
    # eger bizim __izinstance bizim sinifimizin instancesi deyilse
    # butun exemplyarlarimizdaki __isinstance deyishenimiz Ana elementin en yeni exemplyarina beraber olacaq
    # ve sonda return edilecek

    # # 5
    # # oz exemplayrlarimizi funksiya da ede bilerik (hem funksiya hem de exemplyar olacaq)
    # # sadece misal ucun funksiya cagrilanda hemin exemplyarin adini oz adinin uzerine gelir
    def __call__(self):
        self.name = self.name + self.name

    def __init__(self, name: str):
        self.name = name

    # # 1
    def __str__(self):
        return f'Name of this user is {self.name}'
    # # yuxaridaki str magic metodunu istifade elemese idik onda onu print etdikde
    # # biz exemplyarin yaddashda tutdugu yeri gorecekdik
    # # __str__ ile ise bu meseleni istediyimiz cur hell edirik.
    # # amma bu halda bizde kicik bir problemle rastlasha bilerik
    # # misal ucun bir list yaradak ve ora hemin useri daxl edek.
    # # gorduyumuz kimi bele halda yene de kohne veziyyet qarshimiza cixir.
    # # ona gore __str__ ile birlikde adeten bunu da yazirlar ->   __repr__ ( Representation )

    # # 2
    # def __repr__(self):
    #     return f'Name of this user is {self.name}'

    # # User sinfine bunu elave edek. Adeten __str__-in tam kopyasi
    # # oldugu ucun hemin funksiyada stri cagirib return ede bilerik
    def __repr__(self):
        return self.__str__()

    # # 3
    # # bu hele son deyil, biraz da davam edek
    # # misal ucun men user1+user2 -ni print elemek isteyirem
    # # aydindir ki bunu ede bilmir
    # # __add__ metodunu elave etsek self birinci other ise ikincinin arqumenti olacaq ve istediyimizi ede bilerik.
    def __add__(self, other):
        return self.__str__() + ', ' + other.__str__()
    # # bu shekilde magic metodlar coxdur.
    # # vaciblerden birine nezer salaq
    # # yuxarida olan __new__ metoduna bax (# # 4)


user1 = User('Cahangir')
user2 = User('Orxan')
user3 = User('Eldar')
user4 = User('Baxa')
users: list[User] = [user1, user2, user3, user4]
# print(user1)  # __str__
# print(user1 + user2)  # __add__
# print(users)  # __repr__
# print(user1 is user2)  # __new__
# user4()  # __call__
# print(user4)  # __call__

# # siniflerin metodlarina sinif daxilinde ctrl+O (O herfi) basib baxa bilerik (Pycharm) 
# print(dir(User))  # bele variant da var amma hamisini gostermir
"""

'''
try:
    saadasda
except Exception as err:
    print(err)
'''

#########################################
# # TRY EXCEPT
#########################################
"""
class MyCustomException(Exception):
    pass


try:
    a = 5
    # saadasda  # NameError ucun misal
    # a = 5 + 's'  # Exception ucun misal
    # print(6 / 0)  # ZeroDivisionError ucun misal
    num = input('enter num:')  # yuxarida yaratdigim custom exception uchun
    if not num.isdigit():
        raise MyCustomException
except MyCustomException:  # hemin custom exception ishlese
    num = 0  # misal ucun num u 0 beraber ede bilerik, ve sonra lazim olsa istifade ede bilerik
    print('custom exception worked')
except ZeroDivisionError as err:
    # bura ancaq adlandirma ile elaqedar errorlar dushur
    print('ZeroDivisionError', err)
except NameError as err:
    # bura ancaq adlandirma ile elaqedar errorlar dushur
    print('NameError', err)
except Exception as err:
    # bura butun errorlar dushe bilir
    print(err)
else:
    print('ok') # error falan olmasa bu blok ishleyecek
finally:
    print('hemishe yerine yetirilir')

print('tryexcept den sonra')
"""

#########################################
# # GENERATORS
#########################################
"""
# # Generatorlar proqramimizin bizim komputerimizin RAM-inin az istifade olunmasi uchundur
# L = [i for i in range(50000000)]  # burada RAM emelli istifade olunmalidir
# gen = (i for i in range(50000000))  # eyni sheyi generator ile edek
# print(next(gen))  # lazim olduqda ise chagirag ve ekrana verek
# print(next(gen))

# for i in gen:
#     print(i)  # indi ise adi forun ishi komputer terefinden daha az RAM istifade ederekgorulecek

# ---------------------------------------------------------------------

# g = (i for i in range(3))
#
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration:
#     print('finish')

# ---------------------------------------------------------------------

# def gen():
#     yield 1
#     yield 2
#     yield 3
#
#
# generator = gen()
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# ----------------

# def gen(name: str):
#     for ch in name:
#         yield ch
#
#
# generator = gen('Cahangir')
#
# print(next(generator))
# print(next(generator))

# ---------------------------------------------------------------------
# ozum ucun


# def gen():
#     yield 'salam'
#     yield 'necesen'
#     yield 'sagol'
#
#
# generator = gen()
#
# reqem = 0
# try:
#     while True:
#         a = next(generator)
#         reqem += 1
#         print(reqem, a)
# except StopIteration as err:
#     print('dayandi')
# finally:
#     print(reqem, ' defe keche bildik')

# ---------------------------------------------------------------------
# davam

# def gen():
#     yield 'salam'
#     yield 'necesen'
#     yield 'sagol'
#     return 'finish!!!!!!!!'
#
#
# generator = gen()
#
#
# try:
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
# except StopIteration as err:
#     print(err)

# ---------------------------------------------------------------------
# istifade oluna bilecek misal
# fayl adi yarada bilen funksiya yaradaq
# uuid sadece nese esasinda yeni id falan yaratmag ucundur
# from uuid import uuid1
#
# def gen_jpg_file():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid1())
#
#
# jpg_file_generator = gen_jpg_file()
#
# file1 = next(jpg_file_generator)
#
# print(file1)
"""

###############################
# # Polimorfizm qisa misal
###############################
"""
class Shape:
    def calculate_area(self):
        # pass
        return 'Please instead of Shape Class use Square Or Triangle class'


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


def get_area(input_obj):
    print(input_obj.calculate_area())


shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()

get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)
"""

