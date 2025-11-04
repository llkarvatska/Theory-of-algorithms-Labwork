def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Цикл ітерується від другого елемента до кінця
    for i in range(1, n):
        # Зберігаємо поточний елемент для вставки
        key = arr[i]
        assignments += 1

        # Індекс попереднього елемента
        j = i - 1
        assignments += 1

        # Пересуваємо елементи, більші за key, вправо
        while j >= 0 and arr[j] > key:
            comparisons += 1  # порівняння в умові while
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        # Додаткове порівняння, коли цикл завершується
        if j >= 0:
            comparisons += 1

        # Вставляємо key на його правильне місце
        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments


# --- Приклад використання (варіант №13) ---
if __name__ == "__main__":
    my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
    sorted_list, comps, assigs = insertion_sort(my_list.copy())

    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоєнь: {assigs}")
