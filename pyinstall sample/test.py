file = 'test.txt'
with open(file, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)