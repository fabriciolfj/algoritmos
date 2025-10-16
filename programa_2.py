def sort_test(values):
    if len(values) < 2:
        return values

    pivot = values[0]

    less = [i for i in values[1:] if i <= pivot]

    greater = [i for i in values[1:] if i > pivot]

    return sort_test(less) + [pivot] + sort_test(greater)


result = sort_test([8, 5, 6,7, 9, 4, 2, 3, 1])

print(result)