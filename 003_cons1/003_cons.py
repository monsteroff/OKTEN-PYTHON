"""
def notepad():
    todo_list: list[str] = []

    def save(new_todo: str) -> None:
        nonlocal todo_list
        todo_list.append(new_todo)

    def get_all() -> list[str]:
        return todo_list

    # return {'save': save, 'get_all': get_all}
    return save, get_all


save, get_all = notepad()

save('eve get')
save('yemek ye')
save('yat')
save('dur')
save('yuyun')
save('yemek ye')
save('ishe get')
print(get_all())

save2, get_all2 = notepad()
save2('salam')
save2('nev var ne yox')
save2('sagol salamatciliqdi')
save2('sen necesen')
print(get_all2())
"""

# from functools import reduce
#
#
# arr = [1, 2, 3, 4, 5, 6]
# cem = reduce(lambda x, y: x + y, arr)
# print(cem)

# for i in enumerate(arr):
#     print(i[0], '-', i[1])

# for i, v in enumerate(arr):
#     print(i, '-', v)

'''
reqem = 4321


def reqem_ayiran(r):
    netice = []
    defe = 1
    axirinci = r % 10
    while r != axirinci:
        netice.insert(0, axirinci * defe)
        defe = defe * 10
        r = r // 10
        axirinci = r % 10
    netice.insert(0, axirinci * defe)
    return netice


print(reqem_ayiran(reqem))
print(sum(reqem_ayiran(reqem)))
'''

# Balaca console menu yaradilmasi

while True:
    print('1) Salamlash')
    print('2) Sagollash')
    print('3) Exit')

    sechim = input('Seciminizi edin : ')

    if sechim == '1':
        print('-----------')
        print('salam')
        print('-----------')
    elif sechim == '2':
        print('-----------')
        print('sagol')
        print('-----------')
    elif sechim == '3':
        break
