def sort(list):
    for i in range(1,len(list)):
        sorted = True
        for index in range(0,len(list)-i):
            if(list[index+1]<list[index]):
                list[index], list[index+1] = list[index+1], list[index]
                sorted = False
        if sorted:
            break
        print(f'Bubble Sort - {i}.adım: {list}')
