line = "To jest przykładow wiersz"
longest_word = max(line.split(), key=len)
longest_word_number = len(longest_word)
assert longest_word == "przykładow"
assert longest_word_number == 10

