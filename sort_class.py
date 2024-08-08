class SortClass:
    def __init__(self):
        pass

    def sort_bubble(self, sorfroop, n):
        mas = sorfroop
        print("for sort: ", mas)
        for run in range(n - 1):
            for i in range(n - 1 - run):

                if mas[i] > mas[i + 1]:
                    mas[i], mas[i + 1] = mas[i + 1], mas[i]
        print("after sort", mas)

    def quick_sort(self, s):
        if len(s) <= 1:
            return s
        element = s[0]
        left = list(filter(lambda i: i < element, s))
        center = [i for i in s if i == element]
        right = list(filter(lambda i: i > element, s))

        return self.quick_sort(left) + center + self.quick_sort(right)

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    def insert_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
