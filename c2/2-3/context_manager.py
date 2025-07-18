#with can easily release the resourses, and prevent it deadlock
with open('hello.txt', 'w') as f:
    f.write('Hello, World!')

#threading.Lock
'''before
some_lock = threading.Lock()
some_lock.acquire()
try:
    #Handling shared resources
finally:
    some_lock.release() <---unlock
'''

'''after by using with
some_lock = threading.Lock()
with some_lock:
    #Handling shared resources
'''

class ManagedFile:
    def __init__(self,name):
        self.name = name
    def __enter__(self)
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            
>>> with ManagedFile('hello.txt') as f:
       f.write('Hello, World!')

#both of them are the same method

#@contextmanager - contextlib
form contextlib import closing
with closing(open('hello.txt','w') as f:
    f.write('Hello, World')

from contextlib import contextmanager

@contextmanager
def closing(resource):
    try:
        yield resource
    finally:
        resource.close()
        
with Indenter() as indent:
    indent.print('hi')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('how are you')
    indent.print('hay')
