L = ['a','b','c','d','e','f','g','h']
M = ['y','z','a','b','c','d','e','f']

assert set(L + M) == {'a','b','c','d','e','f','g','h','y','z'}
assert set(L) & set(M) == {'a','b','c','d','e','f'}