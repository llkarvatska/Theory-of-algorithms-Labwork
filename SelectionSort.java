public class Main {

    // Алгоритм сортування вибором
    public static void selectionSort(int[] A) {
        int n = A.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < n; j++) {
                if (A[j] < A[minIndex]) {
                    minIndex = j;
                }
            }

            // Обмін елементів
            if (minIndex != i) {
                int temp = A[i];
                A[i] = A[minIndex];
                A[minIndex] = temp;
            }
        }
    }

    public static void main(String[] args) {

        // Варіант 13 — початкова послідовність
        int[] data = {90, 10, 15, 80, 100, 6, 57, 5, 29};

        // Виклик алгоритму
        selectionSort(data);

        // Виведення результату
        System.out.print("Відсортована послідовність: ");
        for (int num : data) {
            System.out.print(num + " ");
        }
    }
}
