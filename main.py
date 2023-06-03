import random
import Selection_Sort as selection

if __name__ == '__main__':
    unsort_array = [random.randint(1, 100) for x in range(10)]
    selection.sort(unsort_array)