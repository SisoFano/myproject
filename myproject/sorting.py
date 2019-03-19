def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for num in range(len(items)-1,0,-1):
        for j in range(num):
            if items[j]>items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items)>1:
        mid = len(nlist)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    return items

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if not items:
        return []

    pivots = [i for i in items if i == items[0]]
    lesser = quick_sort([i for i in items if i < items[0]])
    greater = quick_sort([i for i in items if i > items[0]])

    return lesser + pivots + greater
