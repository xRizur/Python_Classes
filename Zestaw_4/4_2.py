
def make_ruler(n):
    top_part = "|...." * n + "|"
    bottom_part = ""

    for i in range(n + 1):
            number_str = str(i)
            if i == 0:
                bottom_part += number_str
            else:
                bottom_part += " " * (5 - len(number_str)) + number_str

    return top_part + "\n" + bottom_part

def make_grid(rows, cols):
    prostokat = ""

    linia_gorna = '+---' * cols + '+\n'
    linia_srodkowa = '|   ' * cols + '|\n'

    prostokat = linia_gorna
    for i in range(rows):
        prostokat += linia_srodkowa
        prostokat += linia_gorna
    return prostokat

print(make_ruler(21))
print(make_grid(3, 4))