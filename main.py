import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import time


# Алгоритмы сортировки
def bubble_sort(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    return arr, end_time - start_time


def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return arr, end_time - start_time


def merge_sort(arr):
    start_time = time.time()
    arr, _ = merge_sort_recursive(arr)
    end_time = time.time()
    return arr, end_time - start_time


def merge_sort_recursive(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort_recursive(L)
        merge_sort_recursive(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr, 0


def quick_sort(arr):
    start_time = time.time()
    arr = quick_sort_recursive(arr)
    end_time = time.time()
    return arr, end_time - start_time


def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)


# Функция для выполнения сортировки и отображения результатов
def perform_sorting():
    try:
        array_size = int(entry_size.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")
        return

    array = [random.randint(0, 1000) for _ in range(array_size)]

    results = []
    for sort_func in [bubble_sort, insertion_sort, merge_sort, quick_sort]:
        sort_name = sort_func.__name__.replace("_", " ").capitalize()
        _, duration = sort_func(array.copy())
        results.append((sort_name, duration))

    results.sort(key=lambda x: x[1])

    output_text = "Результаты сортировки:\n"
    for name, duration in results:
        output_text += f"{name}: {duration:.6f} секунд\n"

    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, output_text)


# Создание GUI
root = tk.Tk()
root.title("Сравнение алгоритмов сортировки")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_size = ttk.Label(frame, text="Размер массива:")
label_size.grid(row=0, column=0, sticky=tk.W)

entry_size = ttk.Entry(frame)
entry_size.grid(row=0, column=1, sticky=(tk.W, tk.E))
entry_size.insert(0, "100")

button_sort = ttk.Button(frame, text="Выполнить сортировку", command=perform_sorting)
button_sort.grid(row=0, column=2, sticky=tk.W)

text_result = tk.Text(frame, width=50, height=20)
text_result.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E))

root.mainloop()
