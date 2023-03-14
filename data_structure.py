def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
            # print("The index of the element is:", index)
    return None
            # print("Element not in the list")
    
# iterative solution of binary search
def binary_search(list, target):
    first = 0
    last = len(list) - 1

# update the first and last
    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None

def verify(index):
    if index is not None:
        print("The index of the element is:", index)
    else:
        print("Element not in the list")


# keep calling the function with smaller list (recursive)
def recursive_binary_search(list, target):
    # empty list is the stopping condition
    if len(list)==0:
        return False
    else:
        midpoint =(len(list))// 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                # new list in recursive function
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                #  list[midpoint] > target:
                return recursive_binary_search(list[:midpoint], target)


def verify_recursive(result):
    print("The target is found. ", result)



if __name__ == "__main__":
    result = linear_search([1,23,4,56,799],799)
    verify(result)
    result2 = binary_search([1,23,4,56,799],1222)
    verify(result2)

    result3 =  recursive_binary_search([1,23,4,56,799],1)
    verify(result3)
    result4 =  recursive_binary_search([1,23,4,56,799],1222)
    verify(result4)