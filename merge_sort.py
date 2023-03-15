def merge_sort(list):
    """
    sort the given list in a ascending order
    return a new sorted list
    divide: find the midpoint of the list and divide into sublists
    conquer: recursively sort the sublists created in previous step
    combine: merge the sorted sublists crested in pre step

    Takes O(n log n) time:
    """

    # natively sorting--- only 1 element in the list, already sorted
    if len(list) <=1:
        return list
    
    # divide
    left_half, right_half = split(list)
   
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # merge
    return merge(left, right)



def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Return 2 sublists --left and right

    Takes overall O(log n) time
    """
    # floor division 
    mid = len(list) // 2
    # left of midpoint (not include mid)
    left = list[:mid]
    # right of midpoint (include midpoint)
    right = list[mid:]

    return right, left


def merge(left, right):
    """
    Merges 2 lists (arrays) sorting them in the process
    Returns a new merged list

    Takes overall O(n) time
    """

    l = []
    i = 0
    j = 0

    # and condition
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # append to the end of empty list
            l.append(left[i])
            i += 1
        else:
            # left[i] > right[j]
            l.append(right[j])
            j += 1

    # odd number of arrays
    # right is shorter than left
    while i < len(left):
        l.append(left[i])
        i+=1

    # left is shorter than right
    while j < len(right):
        l.append(right[j])
        j+=1

    return l



def verify_sorted(list):
    n = len(list)
    if n == 0 or n ==1:
        return True
    
    # and operator here (both to be true)
    # recursion function here to anything after the 2nd element (index 1:)
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 62, 92, 23, 44, 12]
print(verify_sorted(alist))
l = merge_sort(alist)
print(verify_sorted(l))
# print(l)