def flatten(seq):
    sum = []
    for i in seq: 
        if isinstance(i, (list, tuple)):
            sum.extend(flatten(i))
        else:
            sum.append(i)
    return sum

assert flatten([1, 2, 3, 4, [1,3,[1,2,[5]]]]) == [1, 2, 3, 4, 1, 3, 1, 2, 5]