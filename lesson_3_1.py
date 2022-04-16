def my_range(start, stop, step):
    while start <= stop:
        yield start
        start += step


new_range = my_range(1, 5, 1)
print(next(new_range))
print(next(new_range))
print(next(new_range))
print(next(new_range))
print(next(new_range))