######################################
########## Stacks and Queues #########
######################################
#
# In this homework, we will be giving you the methods to implement, and the classes
# that you will need to define. You are responsible for deciding how to implement the
# stack and queue.
#
# A node class definition is provided. Feel free to look
# at it for help.
#####################################
class Node:
    def __init__(self, data=None, n=None):
        self.data = data
        self.next = n

    # Feel free to add methods that you wrote from your previous homework to add to this
    # class definition, if you find it helpful, or want to use it.

class Stack:
    '''
    This method will be where you define the object. You may or may not use top and bottom
    '''
    def __init__(self, top=None, bottom=None):
        self.top = top

    '''
    This method is called upon to add an element to your object
    '''
    def push(self, data):
        if self.top == None:
            self.top = Node(data)
            return
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    '''
    This method is called upon to remove an element from the list, and return the
    removed object

    Return None if the list is empty
    '''
    def pop(self):
        if self.top == None:
            return None
        temp = self.top
        self.top = temp.next
        return temp.data

    '''
    This method returns the top element, but does NOT remove it from the stack
    '''
    def peek(self):
        if self.top == None:
            return None
        return self.top.data

    '''
    This method is used to determine whether the object is empty, return a boolean
    '''
    def is_empty(self):
        if self.top == None:
            return True
        return False

    '''
    This method returns the size of your object, or in other words, the number of
    elements that it contains.
    '''
    def size(self):
        if self.top == None:
            return 1
        return self.top



class Queue:
    '''
    This method will be where you define the object.
    You may or may not need to use the front and back parameters.
    '''
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    '''
    This method is called upon to add an element to your object
    '''
    def push(self, data):
        if self.front == None:
            self.front = Node(data)
            self.back = self.front
            return
        temp = Node(data)
        self.back.next = temp
        self.back = temp

    '''
    This method is called upon to remove an element from the list.
    It should return the removed object.

    Return None if the list is empty
    '''
    def pop(self):
        if self.front == None:
            return None
        temp = self.front
        self.front = temp.next
        return temp.data

    '''
    This method returns the front element, but does NOT remove it from the queue
    '''
    def peek(self):
        if self.top == None:
            return None
        return self.top.data

    '''
    This method is used to determine whether the object is empty, return a boolean
    '''
    def is_empty(self):
        if self.front == None:
            return True
        return False

    '''
    This method returns the size of your object, or in other words, the number of
    elements that it contains.
    '''
    def size(self):
        pass

