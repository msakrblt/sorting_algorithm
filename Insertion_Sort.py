def sort(list):
    for ayrac in range(1,len(list)):
        if(list[ayrac]<list[ayrac-1]):
            for eleman in range(ayrac,0,-1):
                if list[eleman]<list[eleman-1]:
                    list[eleman], list[eleman - 1] = list[eleman - 1], list[eleman]
                else:
                    break
        print(f'Insertion Sort - {ayrac}. iterasyon: {list}')