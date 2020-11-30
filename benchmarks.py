import random
import Astar
import RemoveDuplicates
import SortingAlgos
import Huffman
import queensproblem
import time
import statistics


functions = Astar.Astar, RemoveDuplicates.remove_duplicates,SortingAlgos.bubbleSort, SortingAlgos.insertionSort, SortingAlgos.selectionSort, SortingAlgos.quickSort, SortingAlgos.merge, SortingAlgos.heapSort, Huffman.huff, queensproblem.queen
times = {f.__name__: [] for f in functions}

for i in range(10):
    for j in range(len(functions)):
        func = functions[j]
        t0 = time.time()
        func()
        t1 = time.time()
        times[func.__name__].append((t1 - t0)*1000) #execution time in ms


dict = {}
for name, numbers in times.items():
    dict[name] = statistics.median(numbers)
    print('FUNCTION:', name, 'Used', len(numbers), 'times')
    print('\tMEDIAN', statistics.median(numbers))
    print('\tMEAN  ', statistics.mean(numbers))
    print('\tSTDEV ', statistics.stdev(numbers))
