x = 'out_test.txt'
a = 'Hello out_tets.txt'
with open(x, 'w') as f:
    f.write(a)

with open(x, 'r') as f:
    for line in f:
        print(line, end="")
