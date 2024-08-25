files = ['a.txt', 'b.txt', 'c.txt']

for file in files:
    f = open(file, 'r')
    print(f.read())
    f.close()