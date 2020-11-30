import random
import time

def heapify(arr, n, i):

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    count = 0
    if l < n and arr[i] < arr[l]:
        largest = l
        count += 1
    if r < n and arr[largest] < arr[r]:
        largest = r
        count += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        count += 1
        heapify(arr, n, largest)
    return count

def heapSort():
    arrayHeapSort = []
    for _ in range(5000):
    	arrayHeapSort.append(random.randint(1, 5000))
    n = len(arrayHeapSort)
    count = 0
    for i in range(n, -1, -1):
        count += 1
        count += heapify(arrayHeapSort, n, i)
    for i in range(n - 1, 0, -1):
        count += 1
        arrayHeapSort[i], arrayHeapSort[0] = arrayHeapSort[0], arrayHeapSort[i]
        count += heapify(arrayHeapSort, i, 0)

def merge():
    arrayMergeSort = []
    for _ in range(5000):
        arrayMergeSort.append(random.randint(1, 5000))

    def mergeSort(arrayMergeSort):
        if len(arrayMergeSort) > 1:
            mid = len(arrayMergeSort) // 2
            L = arrayMergeSort[:mid]
            R = arrayMergeSort[mid:]
            mergeSort(L)
            mergeSort(R)

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

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSortHelper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSortHelper(arr, low, pi - 1)
        quickSortHelper(arr, pi + 1, high)

def quickSort():
    arrayQuickSort = []
    for _ in range(5000):
    	arrayQuickSort.append(random.randint(1, 5000))
    quickSortHelper(arrayQuickSort, 0, len(arrayQuickSort)-1)

def selectionSort():
    arraySelectionSort = []
    for _ in range(5000):
    	arraySelectionSort.append(random.randint(1, 500))
    count = 0
    for i in range(len(arraySelectionSort)):
        count += 1
        min_index = i
        for j in range(i + 1, len(arraySelectionSort)):
            count += 1
            if arraySelectionSort[min_index] > arraySelectionSort[j]:
                min_index = j
        arraySelectionSort[i], arraySelectionSort[min_index] = arraySelectionSort[min_index], arraySelectionSort[i]

def insertionSort():
    arrayInsertionSort = []
    for _ in range(5000):
    	arrayInsertionSort.append(random.randint(1, 500))
    count = 0
    for i in range(1, len(arrayInsertionSort)):
        key = arrayInsertionSort[i]
        j = i - 1
        while j >= 0 and key < arrayInsertionSort[j]:
            count += 1
            arrayInsertionSort[j + 1] = arrayInsertionSort[j]
            j -= 1
        arrayInsertionSort[j + 1] = key
        count += 1

def bubbleSort():
    arrayBubbleSort = []
    for _ in range(5000):
    	arrayBubbleSort.append(random.randint(1, 500))
    n = len(arrayBubbleSort)
    count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1
            if arrayBubbleSort[j] > arrayBubbleSort[j + 1]:
                arrayBubbleSort[j], arrayBubbleSort[j + 1] = arrayBubbleSort[j + 1], arrayBubbleSort[j]
        count += 1
