line = "To jest przykładowy wiersz"
first_chars = ''.join(word[0] for word in line.split())
last_chars = ''.join(word[-1] for word in line.split())
assert first_chars == "Tjpw"
assert last_chars == "otyz"
