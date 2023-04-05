
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/23/2023
# Description: LinkedList class that has recursive implementations of the add
#               and remove methods described in the Exploration
class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, newData):
        self.data = newData

    def get_next(self):
        return self.next

    def set_next(self, newNode):
        self.next = newNode

class LinkedList:
    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def rec_add(self, val, a_node):
        """recursive add method"""
        if a_node.get_next() is None:
            a_node.set_next(Node(val))
            return

        else:
            self.rec_add(val, a_node.get_next())
            return

    def add(self, val):
        """
        Adds a node containing val to the end of the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        else:
            self.rec_add(val, self._head)

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
        else:
            self.rec_remove(val, self._head)

    def rec_remove(self, val, a_node):
        """recursive remove method"""
        if a_node is None:
            return
        if a_node.get_data() == val:
            a_node.set_data(a_node.next)
            return
        else:
            self.rec_remove(val, a_node.next)
            return
        
    def contains(self, key, cursor = None):
        """ Returns True if the list contains a Node with the value key, otherwise 
returns False, recursively. """
        if self._head is None:   # if list is empty, return False
            return False
        if cursor is None:   # sets cursor to head if first iteration
            cursor = self._head
        if cursor.data == key:   # if found, returns True and breaks recursion
            return True
        if cursor.next is not None:   # calls self if not at end of list
            return self.contains(key, cursor.next)
        else:   # if reached end of list, return False
            return False
    
    def insert(self, val, pos, cursor = None, curr_pos = None):
        """ Inserts a node containing val into the linked list at position pos, 
recursively. """
        if self._head is None:   # if list is empty, adds val as head
            self.add(val)
            return
        if cursor is None and curr_pos is None:   # if first iteration, sets cursor to head and starts counter
            cursor = self._head
            curr_pos = 0
        if pos == 0:   # if pos is the head
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
            return
        if curr_pos == pos - 1:   # if previous position found, break recursion, sets next to val, and sets val's next value
            temp = cursor.next
            cursor.next = Node(val)
            cursor.next.next = temp
            return
        if cursor.next is not None: # calls self if not at end of list, while incrementing the cursor and cursor position
            self.insert(val, pos, cursor.next, curr_pos + 1)
        else:   # if last or greater pos is being replaced
            cursor.next = Node(val)
            return
        
    def reverse(self, current = None, previous = None, following = None):
        """ Reverses the linked list, recursively. """
        if self._head is None:   # if list is empty, return
            return
        if current is None and previous is None:   # if first iteration, sets cursor to head
            current = self._head
        if current is None and previous is not None:   # if reached end of list, break recursion and reconnect head
            self._head = previous
            return
        following = current.next
        current.next = previous
        previous = current
        current = following
        self.reverse(current, previous, following)   # calls self after updating values
    def to_plain_list(self, cursor = None, py_list = None):
            """ Returns a regular Python list that has the same data values, in the 
    same order, as the linked list. """
            if cursor is None and py_list is None:   # if first iteration, initializes list
                cursor = self._head
                py_list = []
            if self._head is None:   # if list is empty, returns empty list
                return py_list
            if cursor is None and py_list is not None:   # if end of list, break recursion and return list
                return
            py_list.append(cursor.data)   # append list with linked list data
            self.to_plain_list(cursor.next, py_list)
            return py_list

def main():
    list = LinkedList()
    list.add(12)
    list.add(7)
    list.add(20)
    # list.remove(20)
    # list.insert(8,2)
    list.reverse()
    print(list.get_head().next.next.data)
    print(list.display()) 
    print(list.to_plain_list())


if __name__ == '__main__':
    main()
