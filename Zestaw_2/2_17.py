line = "abcd def ghiddd  jssssssskl"
assert sorted(line.split()) == ['abcd', 'def', 'ghiddd', 'jssssssskl']
assert sorted(line.split(), key=len) == ['def', 'abcd', 'ghiddd', 'jssssssskl']