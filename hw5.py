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
        pass

    '''
    This method is called upon to add an element to your object
    '''
    def push(self, data):
        pass

    '''
    This method is called upon to remove an element from the list, and return the
    removed object

    Return None if the list is empty
    '''
    def pop(self):
        pass

    '''
    This method returns the top element, but does NOT remove it from the stack
    '''
    def peek(self):
        pass

    '''
    This method is used to determine whether the object is empty, return a boolean
    '''
    def is_empty(self):
        pass

    '''
    This method returns the size of your object, or in other words, the number of
    elements that it contains.
    '''
    def size(self):
        pass


class Queue:
    '''
    This method will be where you define the object. You may or may not use front and back
    '''
    def __init__(self, front=None, back=None):
        pass

    '''
    This method is called upon to add an element to your object
    '''
    def push(self):
        pass

    '''
    This method is called upon to remove an element from the list, and return the
    removed object

    Return None if the list is empty
    '''
    def pop(self):
        pass

    '''
    This method returns the front element, but does NOT remove it from the queue
    '''
    def peek(self):
        pass

    '''
    This method is used to determine whether the object is empty, return a boolean
    '''
    def is_empty(self):
        pass

    '''
    his method returns the size of your object, or in other words, the number of
    elements that it contains.
    '''
    def size(self):
        pass

