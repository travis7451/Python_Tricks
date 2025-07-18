values = [100,200,300]

''' it will be some bug when you adding some integer without comma into your list
values = [
    100,
    200,
    300   <----- invalid syntax
    400
]
'''

''' the worse situation is when you add some string without comma into your list
names = [
    'Alex',
    'Joan',
    'Bob'
    'Jenny'
]
>>> names
['Alex', 'Joan', 'BobJenny']
it won't cuz the error, so this is harder to find the bug
'''

'''sol
the way to prevent it happen we have to change our coding style
names = [
    'Alex',
    'Joan',
    'Bob',
    'Jenny',  <---- try to drop a comma on every sigle line even the last one
]
'''
