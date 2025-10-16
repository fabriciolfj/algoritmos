def calc(value):
    if value == 1:
        return 1
    else:
        return value * calc(value - 1)



def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

result = sum([2,4,6])

print(result)