# open('test.txt', 'r')  # read # fayli oxumaq uchun acmaga calishiriqsa ve o esline yoxdursa -> err
# open('test.txt', 'w')  # write # fayl yoxdursa yaradacaq amma her yazida silib tezden yazacaq
# open('test.txt', 'a')  # append # fayl yoxdursa yaradir ve melumati elave edir
# open('test.txt', 'x')  # create # sadece yeni fayl yaradir

# open('test.txt', 'rt')  # text rejiminde oxumaq (t defaultdur. yazmasaq da olar)
# open('test.txt', 'rb')  # binary rejiminde oxumaq (shekil, video misal ucun binar fayl olur adeten)

file1 = open('test.txt', 'r')
# print(file1.read())  # bele variant az istifade olunur.
# print(file1.readline())  # bir setir oxuyur sonda enter varsa onu da oxuyacaq enteri bogur elemek ucun end='' qeyd edek
# print(file1.readline(), end='')
# windowslarda oxuma ile elaqedar problem yarana biler. encoding='utf-8' yazmaq olar
# print(file1.read(5))  # birinci 5 simvolu oxumaq. kiril elifbasi olanda yazilan reqemde az gostere biler. (bele bug olur)

# for line in file1:
#     print(line, end='')
# ikinci defe for elesek alinmayacaq onu elemek ucun fayl daxilinde kursoru yeniden evvele getirmek lazimdir.
# fayli oxuyanda son oxudugu hardadirsa kurson orada olur. file.seek(0) elesek kursor 0-ci simvola gelecek
# file1.seek(12)
#
# for line in file1:
#     print(line, end='')

# bir variant da var. butun setirleri list sheklinde almaq.
# amma bununla biraz ehtiyatli davranmaq lazimdir.
# cunki fayl cox boyuk olsa list yaradilanda kompun RAMI catmaya biler
# print(file1.readlines())
# oxumaqla bu qeder


# yazmaq (w) # opende w duranda
# file1.write('hello')  # bunu elesek butun fayl temizlenecek ve yerine hello yazilacaq.
# file1.writelines(['salam\n', 'necesen\n', 'yaxshiyam\n'])  # bir neche setiri birlikde yazmaq.

# yazmaq(a) # opende a duranda
# file1.write('finish')  # bunu elesek fayla yazilan elave olunacaq (\n) meselesine ozumuz diqqet elemeliyik.

# fayli achmishiqsa lazim olmayanda onu baglamaliyiq. RAMIN bitmesine getirib cixara biler.
file1.close()

# fayllarla ishleyende potensial olaraq sizin kodunuz tehlukeli olur ve onu try excepte salmaginiz meslehetdir.
# en meshur errorlardan biri FileNotFoundError -dur (r olanda)
# amma biz butun errorlarimizi evvelceden bile bilmerik.
# yaddash catishmamazligi, sert diskin zedeli olmasi, fayli oxumaq ucun huquq catmir ve s.
# elave bir dene de Except versek (en boyuk Exceptimiz) -> Exception

# try:
#     file = open('olmayan_fayl.txt')
#     file.write('misalucun')
#     file.close()
# except FileNotFoundError:
#     print('...')
# except Exception as err:
#     print('EXCEPTION EROROROROROROROROOROR', err)

# nezere alaq ki bu kod yerine yetirilende error fayli acmaq istediyimiz merhelede dusherse
# ondan sonraki file.close() metodu ishlemeyecek.
# her ehtimala qarshi onu baglamaq lazimdir.

# yeni gozel yol var bunun ucun. context manager (with ... as ...)

# try:
#     # burada fayl 100% baglanacaq(context manager bunu qarantiya edir).
#     # qisa olaraq bizim yerimize close edir.
#     with open("olmayan_fayl.txt") as file:
#         file.write('misalucun')
# except FileNotFoundError:
#     print('...')
# except Exception as err:
#     print('EXCEPTION EROROROROROROROROOROR', err)

#####################################################
# # Praktiki misal olsun
#####################################################
import json  # json melumatlarin yazilmasi ucun
import pickle  # binar melumatlarin yazilmasi ucun

users = [{'name': 'Cahangir', 'age': 28}]

# # jsonu yazaq
# try:
#     # burada fayl 100% baglanacaq(context manager bunu qarantiya edir).
#     # qisa olaraq bizim yerimize close edir.
#     with open("users.json", 'a', encoding='utf-8') as file:
#         # file.write('misalucun')
#         json.dump(users, file)  # jsonu fayla yazma ucun .dump (gonderilen melumat, faylin ozu) (import json lazimdir)
# except FileNotFoundError:
#     print('...')
# except Exception as err:
#     print('EXCEPTION EROROROROROROROROOROR', err)

# # binari yazaq
# try:
#     with open("binary_users.json", 'wb') as file:
#         # file.write('misalucun')
#         pickle.dump(users, file)  # binari fayla yazma ucun .dump (gonderilen melumat, faylin ozu) (import pickle lazimdir)
# except FileNotFoundError:
#     print('...')
# except Exception as err:
#     print('EXCEPTION EROROROROROROROROOROR', err)

# # binari oxuyaq
# try:
#     with open("binary_users.json", 'rb') as file:
#         users = pickle.load(file)
#         print(users)
# except FileNotFoundError:
#     print('...')
# except Exception as err:
#     print('EXCEPTION EROROROROROROROROOROR', err)

# # jsonu da oxumaq ucun .load lazim olacaq.


##############################################################################
# # Pattern matching
##############################################################################

# # Python 3.10 dan etibaren JS switchine oxshar match emele gelib. (evvel yox idi)

# a = input('Enter num: ')
# match a:
#     case '5':
#         print('besh')
#     case '4':
#         print('dord')
#     case _:
#         print('error')


# s = 'left 200'.split()

# videoda 31-32 deqiqe yazmaq cetin olacaq, gormek lazimdir.
# match s:
#     case action, value:  # action ve value s in destrukturizasiya olunmush deyishenleridir
#         print(action, value)
#     case 'top' | 'left' as action, value:
#         print(action, value)
#     case 'hit' as action, value:
#         print(action, value)
#     case _:
#         print('error')


# eyni shey dictionary ile de ishleyir 33:44

# user = {'name': 'Max', 'age': 15, 'status': True}
#
# match user:
#     case {'name': str(name), 'age': int(age), 'status': bool(status)}:
#         print('All Right', name, age, status)
#     case _:
#         print('Error')
