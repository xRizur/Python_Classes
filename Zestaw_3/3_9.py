L = [[],(1,2),[3,4],(5,6,7)]
result = []
for i in L:
    sum = 0
    for j in i:
        sum += j
    result.append(sum)

assert result == [0,3,7,18]