def merge_recursive(left, right):
    result = []
    i = j = 0
    comparisons = assignments = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        assignments += 1
    while i < len(left):
        result.append(left[i])
        i += 1
        assignments += 1
    while j < len(right):
        result.append(right[j])
        j += 1
        assignments += 1
    return result, comparisons, assignments


def merge_sort_recursive(a):
    comparisons = assignments = recursive_calls = 0
    if len(a) <= 1:
        return a, comparisons, assignments, recursive_calls
    mid = len(a) // 2
    left, c1, a1, r1 = merge_sort_recursive(a[:mid])
    right, c2, a2, r2 = merge_sort_recursive(a[mid:])
    merged, c3, a3 = merge_recursive(left, right)
    comparisons = c1 + c2 + c3
    assignments = a1 + a2 + a3
    recursive_calls = r1 + r2 + 1
    return merged, comparisons, assignments, recursive_calls


# --- Приклад ---
if __name__ == "__main__":
    data = [90, 10, 15, 80, 100, 6, 57, 5, 29]
    print("Оригінальний масив:", data)
    sorted_rec, comps_rec, assigns_rec, rec_calls = merge_sort_recursive(data)
    print("Відсортований масив:", sorted_rec)
    print(f"Порівнянь: {comps_rec}, Присвоєнь: {assigns_rec}, Рекурсивних викликів: {rec_calls}")
