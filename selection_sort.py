def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Зовнішній цикл ітерується по всьому списку від 0 до n-2
    for i in range(n - 1):
        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1  # присвоєння змінній min_index

        # Внутрішній цикл шукає найменший елемент у решті списку
        for j in range(i + 1, n):
            comparisons += 1  # операція порівняння
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1  # оновлення min_index

        # Якщо знайдено новий мінімальний — міняємо місцями
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # три присвоєння при обміні

    return arr, comparisons, assignments


# --- Приклад використання (варіант №13) ---
if __name__ == "__main__":
    my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
    sorted_list, comps, assigs = selection_sort(my_list.copy())

    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_list)
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоєнь: {assigs}")
