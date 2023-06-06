def max_elaman(list):
    print(f'unsort list: {list}')
    max_index = 0
    for index in range(len(list)):
        if list[index]>list[max_index]:
            max_index = index
    array_size=list[max_index]
    arr=[]
    result = []
    for i in range(array_size+1):
        arr.append(0)
    for i in range(len(list)+1):
        result.append(0)
    return arr, result

def sort(list):
    new_array, result = max_elaman(list)
    for i in list:
        new_array[i]+=1
    print(f'new array: {new_array}')
    for index in range(1,len(new_array)):
        new_array[index]=new_array[index]+new_array[index-1]
    print(f'cumulatif: {new_array}')
    for index in range(len(list)):
        result[new_array[list[index]]]=list[index]
        new_array[list[index]]-=1
    if result[0]==0:
        result.remove(0)
    print(result)
