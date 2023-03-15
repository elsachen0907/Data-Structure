# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)
class Node:
    # data = None
    # next_node = None


    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node


    def __repr__(self):
        return "<Node data: %s>" %self.data
    

class LinkedList:
    # head = None
    """
    singly linked list
    """
    # constructor
    def __init__(self):
        self.head = None
        self.__count = 0

# head is none, then no list
    def is_empty(self):
        return self.headn== None
    
    def size(self):
        """
        return the number of nodes in the list
        takes O(n) times
        """
        # current = self.head
        # count = 0

        # while current:
        #     # count = count + 1
        #     count += 1
        #     # after increment, then point to the next node
        #     current = current.next_node
        # return count    
        return self.__count
    

    def add(self, data):
        """
        Add a new node containing data at head of list
        constant time O(1) time
        """
        # new_node = data
        # set the new node to head of the node
        new_node = Node(data, next_node=self.head)
        self.head = new_node
        # increment the count by 1
        self.__count += 1


    def search(self,key):
        """
        Search for the first node containing data that matches the key
        return the node or None if not found
        worst case: linear time search for each node in the list: O(n) time
        """
        current = self.head
        while current:
            # if the current one is what we are searching for
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
        
    def insert(self, data, index):
        if index >= self.__count:
            raise IndexError('index out of range')
        
        # add a new node
        if index == 0:
            self.add(data)
            return
        if index > 0:
            # new is the data we wanna add
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            # now set the links between previous node and next node
            prev_node.next_node = new
            new.next_node = next_node

        self.__count += 1



    def remove(self, key):
        # worst case takes linear time O(n)
        # remove based on data or index
        current = self.head
        previous = None
        found = False

        while current and not found:
            # 3 situations:
            # 1. key matches the current node (is head now)
            if current.data == key and current == self.head:
                found = True
                # automatically set to next node, which is empty(不存在)
                # list is empty after removing
                self.head = current.next_node

            # 2. key matches node, but not the head now
            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            # key not found
            else:
                previous = current
                current = current.next_node

        return None

    # find the index (input is the index we had)
    def node_at_index(self, index):
        if index >= self.__count:
            raise IndexError('index out of range')
        
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current
        
    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)    