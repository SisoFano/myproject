def bubble_sort(items):

    """Return array of items, sorted in ascending order using bubble sort"""
    for num in range(len(items)-1,0,-1):
        for j in range(num):
            if items[j]>items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items

def merge_sort(items):

    """Return array of items, sorted in ascending order using merge sort"""
    if len(items) >1:
        mid = len(items)//2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i+=1
            else:
                items[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            items[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            items[k] = right[j]
            j+=1
            k+=1

    return items

def quick_sort(items):

    """Return array of items, sorted in ascending order quick sort"""
    if not items:
        return []

    pivots = [i for i in items if i == items[0]]
    lesser = quick_sort([i for i in items if i < items[0]])
    greater = quick_sort([i for i in items if i > items[0]])

    return lesser + pivots + greater
