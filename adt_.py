# Made by Jordan Williams and Diandra Whittick

# Name: Jordan Williams
# id number: 620108502

# Name: Diandra Whittick
# id number: 620103319





# queue operations
def new_Queue():
    return 'queue',[]
def is_Queue(q):
    return type(q) == type(()) and q[0] == 'queue'
def queue_Contents(q):
    return q[1]
def empty_queue(q):
    return queue_Contents(q) == []
def queue_front(q):
    return queue_Contents(q)[0]
def enqueue(q,el):
    queue_Contents(q).append(el)
def dequeue(q):
    queue_Contents(q).pop(0) #changed to pop

# stack operations
def new_Stack():
    return 'stack',[]
def is_Stack(s):
    return type(s)== type(()) and s[0] == 'stack'
def stack_Contents(s):
    return s[1]
def empty_Stack(s):
    return stack_Contents(s) == []
def stack_Top(s):
    return stack_Contents(s)[0]
def push(s,el):
    stack_Contents(s).insert(0,el)
def pop(s):
    stack_Contents(s).pop(0)
