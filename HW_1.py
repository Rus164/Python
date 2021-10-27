# 1) Создать переменную типа String
stroka = str('Devil')
# 2) Создать переменную типа Integer
int_er = int(666)
# 3) Создать переменную типа Float
fl_oat = float(6.66)
# 4) Создать переменную типа Bytes
by_tes = bytes(2)
# 5) Создать переменную типа List
li_st = list('Yterksdjfh')
# 6) Создать переменную типа Tuple
tu_ple = tuple('4334')
# 7) Создать переменную типа Set
ordinary_set = set('gffcc')
# 8. Создать переменную типа Frozen set
frozen_set = frozenset('gff')
# 9) Создать переменную типа Dict
di_ct = dict(City='Moscow', Country='Russia')
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(stroka))
print(type(int_er))
print(type(fl_oat))
print(type(by_tes))
print(type(li_st))
print(type(tu_ple))
print(type(ordinary_set))
print(type(frozen_set))
print(type(di_ct))
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'Hello '
b = 'World'
c = a + b
print(c)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
street = 'street,'
home = 23
print(street, home)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
mobile = 'Nokia '
number = 610
print(mobile + str(number))