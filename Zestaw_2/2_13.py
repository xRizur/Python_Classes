line = "To jest przykładowy wiersz"
suma = sum(len(word) for word in line.split())
assert suma == 23