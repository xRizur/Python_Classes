L = [5, 23, 100, 7, 56, 890]
blocks = [str(x).zfill(3) for x in L]
line = ''.join(blocks)
assert line == "005023100007056890"