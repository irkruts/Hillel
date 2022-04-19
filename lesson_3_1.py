def my_range(start, stop, step):
    if start is not None and stop is not None:
        new_generator = (start + step for start in range(start, stop))
        start += step
        if start < stop:
            for i in new_generator:
                yield i
        yield 'Stop generator. Start point is bigger than stop point'
    else:
        yield 'Start point or stop point is None'


new_range = my_range(1, 5, 1)
print(next(new_range))
print(next(new_range))
print(next(new_range))
print(next(new_range))
print(next(new_range))
