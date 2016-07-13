"""
Lesson 6
7/11/2016
implementations of classes

    DATA STRUCTURES (structs)

    STACKS
    QUEUES
    LINKED LISTS

lists, sets, tuples, dicts, hashmaps, trees,
    doubly linkedlits

    STACKS
    - stack of items
    - can be anything, ints, strings, coords,
        language syntax
    - lifo: last in first out

    **look at picture
    4 operations
    every operation has the constraints having O(1)
    OR CONSTANT TIME, no matter how many items you have
    it's still takes the same amount of time to perform
        1.push
        2.pop
        3.peek
        4.size

why does it matter
-order might matter
-user only needs last element
-user friendly
-large amounts of data can easily be seen
-git fetching: only grabing most recent data
-there are actual practical applications to stacks
-used for certain algorithms
    -algorithms: BST (binary-search tree)
                DFS (dEPTH-fIRST Search)

Why not want a stack
-better ways to org data
-access only top element
-only use few functions:can't do much
-time efficiency: not scalable
    -list of 10k items
    -needed to look at item of first item
    -O(n) operations to look at first item
-instantly loose data when popping
    -fixed by popping  and pushing into other stack
        -reversing stack
"""
class Stack(object):
    #whenever you make an instance of the class it comes from here
        #global variables, attributes, characteristics
    def __init__(self):
        self.stack = []



    # adds/puts elements at the top of the stack
    def push(self, add): #function definition
        self.stack.append(add) #add to end

    #retrieve last element out of the top of the stack
    #and return it, give it back to user
    def pop(self):
        return self.stack.pop()
        #return self.stack.remove(self.stack[-1])

    #looks at the last item in the stack
    #looks at item at the top of stack
    def peek(self):
        return self.stack[-1]

    #returns how many items in stack
    def size(self):
        return len(self.stack)

aStack = Stack()
print(aStack)
aStack.push(1) #we will be manipulating self.stack
print(aStack)
aStack = Stack()

"""
    Queues
    -a line that you wait in
    -4 operations
        -enque
        -dequeue
        -size
        -isEmpty

    -first person to enter queue is first person to leave

"""
class Queue(object):
    def __index__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    #add item to queue
    def enqueue(self, item):
        self.queue.append(item)

    #removes item from the front of the queue
    #and returns the item to user
    def dequeue(self):
        return self.queue.pop(0)

    #return number of items in queue
    def size(self):
        return len(self.queue)

    # return if queue is empty or not
    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        else:
            return False

        #return not bool(self.size())
        #return not bool(len(self.queue))
        #return not bool(self.queue)
        #return not self.queue
        """
        truthy or falsy
        0 false     1 true
        "" = false  "a" = true
        [] = false  [1] = true

        ***can use
            return self.size() == 0
        turns int 0 == 0
        then into True

        return True
        """
aQueue = Queue()
print("le queue:", aQueue)
aQueue.enqueue(1)
print("le queue;", aQueue)
aQueue.enqueue(2)
print("le queue:", aQueue)
print("popped", aQueue.dequeue())
print("le queue", aQueue)