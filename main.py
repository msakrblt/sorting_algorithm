import random
import Selection_Sort as selection
import Insertion_Sort as insertion
import Bubble_Sort as bubble

if __name__ == '__main__':
    unsort_array = [random.randint(1, 100) for x in range(10)]
    selection.sort(unsort_array)
    insertion.sort(unsort_array)
    bubble.sort(unsort_array)