def sort(numbers, left, right):
    n = right - left + 1 #длина сортируемого массива
    pivot = numbers[left + n // 2] #опорный элемент
    print('Support element', pivot) #вывести опорный элемент
    save_left = left    #запомнить  положение левого
    save_right = right  #и правого края сортируемой части массива
    global count #использовать глобальную переменную count
    while left <= right: #цикл while, который выполняется, пока left не больше right
        while numbers[left] < pivot:    #пока левый элемент меньше опорного
            left += 1                   #сдвинуть левое ограничение на 1
        while numbers[right] > pivot:   #пока правый элемент меньше опорного
            right -= 1                  #сдвинуть правое ограничение на 1
        if left <= right: #после нахождения 2 неправильных элементов поменять их, чтобы меньший был слева, а больший справа
            if numbers[left] != numbers [right]: #если элементы не равны
                numbers[left], numbers[right] = numbers[right], numbers[left]
                count += 1
                print('Intermediate state:', numbers)  # высести промежуточное состояние массива
            left += 1
            right -= 1  #сдвинуть левое и правое ограничение на 1
    if save_left < right: #вызвать функцию для сортировки левой части массива, если в ней больше 1 элемента (есть, что сравнивать)
        sort(numbers, save_left, right)
    if save_right > left: #вызвать функцию для сортировки правой части массива, если в ней больше 1 элемента (есть, что сравнивать)
        sort(numbers, left, save_right)

count = 0 #переменная для счёта перестановок
numbers = [] #массив, который будем сортировать
print('Enter the size of the array')
n = int(input()) #считать количество элементов массива
for i in range (n): #считать элементы массива
    print(f'Enter {i+1} element')
    a = int(input())
    numbers.append(a) #добавить новый элемент в конец
print('Original array', numbers)
left = 0        #изначальные ограничения (индексы первого и последнего элемента)
right = n - 1
sort(numbers, left, right) #вызвать функцию
print('Sorted array:', numbers) #вывести отсортированный массив
print('Number of permutation', count) #вывести количество перестановок