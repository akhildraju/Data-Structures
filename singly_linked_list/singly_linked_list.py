class Node:
    def __init__(self, value, next=None):
	    self.value = value
	    self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    # def add_to_tail(self, value):
    #     new_node = Node(value)
    #     if self.head is None and self.tail is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.set_next(new_node)
    #         self.tail = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else:
            # store the last Node's value in a nother variable so we can return it 
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning 
            
            # starting from the head, we'll traverse down to the second-to-last Node 
            # init another reference to keep track of where we are in the linked 
            # list as we're iterating 
            current = self.head 

            # keep iterating until the node after `current` is the tail
            while current.get_next() != self.tail:
                # keep iterating 
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None) 
            return val

    def print(self):
        current = self.head

        while current is not None:
            print("Print value =", current.value)
            current = current.next


    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    # def remove_head(self):
    #     val = self.head.value

    #     if self.head.next is not None:
    #         self.head = self.head.next
    #     else:
	#         self.head = None

    #     return val

    def get_max(self):
        this = self.head
        if this is None:
            return None

        val = self.head.value
        while this is not None:
            if this.value > val:
                val = this.value
            this = this.next
        return val

    def remove_head(self):
        # check if the linked list empty 
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node 
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return 
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value 
            return val


