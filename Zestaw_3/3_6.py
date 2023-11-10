width = 4
height = 3
prostokat = ""

linia_gorna = '+---' * width + '+\n'
linia_srodkowa = '|   ' * width + '|\n'

prostokat = linia_gorna
for i in range(height):
    prostokat += linia_srodkowa
    prostokat += linia_gorna

print(prostokat)
