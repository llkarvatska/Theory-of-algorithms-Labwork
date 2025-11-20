public class Main {
    // Алгоритм сортування вставками
    public static void insertionSort(int[] values) {
        int n = values.length;

        for (int j = 1; j < n; j++) {
            int key = values[j];
            int i = j - 1;

            // Зсув елементів, що більші за key
            while (i >= 0 && values[i] > key) {
                values[i + 1] = values[i];
                i--;
            }

            // Вставка key на правильне місце
            values[i + 1] = key;
        }
    }

    public static void main(String[] args) {
        // Початковий масив (Варіант 13)
        int[] values = {90, 10, 15, 80, 100, 6, 57, 5, 29};

        // Виклик алгоритму сортування вставками
        insertionSort(values);

        // Виведення результату
        System.out.print("Відсортована послідовність: ");
        for (int num : values) {
            System.out.print(num + " ");
        }
    }
}
