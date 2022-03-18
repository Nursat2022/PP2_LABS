with open('input.txt', 'r') as f:
    x = f.readlines()

cnt = sum(1 for line in x if line != '\n')
print(f'number of lines: {cnt}')