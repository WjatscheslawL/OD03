import sort_class as sc

sort = sc.SortClass()


print("Start Быстрая сортировка")
print(sort.quick_sort([5, 2, 9, 0, 1, 5, 3]))

print("Start Пузырьковая сортировка")
mas = [5, 7, 4, 3, 8, 2]
sort.sort_bubble(mas, 6)

print("Start Сортировка слиянием")
a = [-3, 5, 0, -8, 1, 10]
print("for sort: ", a)
sort.insert_sort(a)
print("for after: ",a)

print("Start Сортировка выбором")
a = [-3, 5, 0, -8, 1, 10]
print("for sort: ", a)
sort.selection_sort(a)
print("for after: ", a)
