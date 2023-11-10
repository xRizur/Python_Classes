dlugosc = 21

top_part = "|...." * dlugosc + "|"
bottom_part = ""

for i in range(dlugosc + 1):
        number_str = str(i)
        if i == 0:
            bottom_part += number_str
        else:
            bottom_part += " " * (5 - len(number_str)) + number_str

result = top_part + "\n" + bottom_part

print(result)
