#1.создать переменную String
name = 'Fera'
#2.создать переменную Integer
integer_type = 27
#3.создать переменную Float
fl_digit = 3.14
#4. создать переменную Bytes
b_type = bytes(26)
#5.создать переменную List
list_type = ['123', '456', '789']
#6.создать переменную Tuple
tuple_type = (12, '23')
#7.создать переменную Dict
dict_type = {'name':'Fera','age':27}
#8.создать переменную Set
set_type = {'harry', 'potter', 'griffyndor', '1', '26'}
#8* для себя создала переменную mixed_set
mixed_set = {1, True, 3,14, 21,'potter'}
#9.создать переменную Frozen set
#creating a dictionary
Testing = {'Postman':'to test API', 'SQL':'to work with Database', 'Python':'to code', 'Jmeter':'for load testing'}
#making keys of dictionary as frozenset
key = frozenset(Testing)


#10.вывести в консоль все выше перечисленные переменные с добавлением  типа данных
print(type(name), name)
print(type(integer_type), integer_type)
print(type(fl_digit), fl_digit)
print(type(b_type), b_type)
print(type(list_type), list_type)
print(type(tuple_type), tuple_type)
print(type(dict_type), dict_type)
print(type(set_type), set_type)
print(type(mixed_set), mixed_set)
print('the frozen set is:', key)

#11.создать 2 пересенные String, создать переменную которой сканкатенируете эти переменныею вывести в консоль.
print("lala"+'land')
#12.вывести в одну строку переменные типа String и Integer используя ","Запятую
print('Hello ', 'World')
#13.вывести в одну строку переменные типа String и Integer используя "+"Плюс
print('Hello '+'World')