def sort_lil_bit(items,begin,end):
    left_index = begin
    pivot_index = end
    pivot_value = items[pivot_index]


    while(left_index!=pivot_index):
        item = items[left_index]
        if item <= pivot_value:
            left_index+=1
            continue
        items[left_index] = items[pivot_index - 1]
        items[pivot_index-1] = pivot_value
        items[pivot_index] = item
        pivot_index-=1

    return pivot_index

def sort_all(items,begin,end):
    if end <= begin:
        return
    pivot_index = sort_lil_bit(items,begin,end)
    sort_all(items,begin,pivot_index-1)
    sort_all(items,pivot_index+1,end)

def quicksort(items):
    sort_all(items,0,len(items)-1)

items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)
