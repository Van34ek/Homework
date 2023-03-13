n = int(input('Введите количество элементов 1 множества: '))
m = int(input('Введите количество элементов 2 множества: '))
my_set1 = set()
my_set2 = set()
for i in range(n):
    my_set1.add(input())
for j in range(m):
    my_set2.add(input())
my_set3 = my_set1 & my_set2 
print(sorted(my_set3))


