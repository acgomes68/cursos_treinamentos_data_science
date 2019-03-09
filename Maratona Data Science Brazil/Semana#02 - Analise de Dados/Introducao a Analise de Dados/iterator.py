'''
fdfdsf
'''
def my_for_loop(some_iterable):
    oIter = some_iterable.__iter__()
    while True:
        try:
            print(oIter.next())
        except StopIteration:
            break

my_for_loop([1,2,3])
