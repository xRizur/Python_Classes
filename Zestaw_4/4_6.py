def sum_seq(sequence):
    sum = 0
    for i in sequence: 
        if isinstance(i, (list, tuple)):
            sum += sum_seq(i)
        else:
            sum += i
    return sum

assert sum_seq([1, 2, 3, 4, [1,3,[1,2,[5]]]]) == 22