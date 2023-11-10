def odwracanie(L,left,right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie(L, left + 1, right - 1)
    return L

assert odwracanie([1,2,3,4,5,6,7,8,9], 0, 4) == [5,4,3,2,1,6,7,8,9]