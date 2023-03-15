# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)
from linked_list import LinkedList
# l = LinkedList()

# l.add(1)
# print(l)

# compared to regular merge  sort, we need to deal with the references in linked list now
def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """
    # first, we check if the len is 1 or 0, then no sorting applied
    if linked_list.size == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list
    else:
        left_half, right_half = split(linked_list)
    
        left = merge_sort(left_half)
        right = merge_sort(right_half)

        return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublinked_lists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    
    else:
        size = linked_list.size()
        mid = size //2

        # mid -1 (use size, it will return a value greater than the max index)
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        # first assign the next node to be the first/ head of right half sublist
        right_half.head = mid_node.next_node
        # then separate the 2 sub linked list (remove the link in between) 
        mid_node.next_node = None

    return left_half, right_half



def merge(left, right):
    """
    Merges 2 linked lists, sorting by data in nodes
    Returns a new merged list
    """

# create a new linked list that contains nodes
# from merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail point of either
    while left_head or right_head:
        # if the head of left is none, we will past the tail
        # add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to False
            right_head = right_head.next_node
            
        
        # if the head node of right is none, we will past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition to False
            left_head = left_head.next_node


        else:
            # not at either tail node
            # obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node

            # if data on left is greater than right, set current to right one
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node
        
        # move current to next node
        current = current.next_node


    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged




l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
# l.add(23)


print(l)

node1 = l.node_at_index(0)
print(node1)
# Result:
# [Head: 200]-> [15]-> [44]-> [2]-> [Tail: 10]
# <Node data: 200>

# sorted_linked_list = merge_sort(l)
# print(merge_sort(l))

left_half, right_half = split(l)
print("The left half is:", left_half)
print("The right half is:", right_half)
# The left half is: [Head: 200]-> [Tail: 15]
# The right half is: [Head: 44]-> [2]-> [Tail: 10]
