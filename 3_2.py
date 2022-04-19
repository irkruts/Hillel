def my_map(func, items):
    #new_map = [] //
    for i in items:
        #new_map.append(func(i))
        #print(new_map)
        yield func(i)
result = my_map(lambda i: i + 2, [1, 3, 4, 100])
try:
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
except StopIteration:
    print('ERROR')

