# x = int(input('Некоторое число: '))
# n = int(input('вВЕДИТЕ КОЛИЧЕСТВО ЭЛЕМЕНТОВ В СПИСКЕ: '))
# list1 = [i for i in range (n)]
# if x in list1:
#     print(f'Оъект найден в списке {x}')
# else:
#     print('ничего')

#задача 2
# Задача 3
list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K',
               8: 'JX', 10: 'QZ'}
list_Russia = {1:'АВЕТНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5: 'ЖЗХЦЧ',
               8:'ШЭЮ', 10:'ФЩЪ'}
word = input('Введите слова на английскои или на Русском: ')
count = 0
for i in word:
    for keys, values in list_Russia.items():
        if i in values:
            count += keys
print(f'Стоимость введённого слова равняется {count}')