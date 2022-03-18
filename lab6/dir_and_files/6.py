import os

for i in range(65, 91):
    letter = chr(i)
    f = open(f'{letter}.txt', 'w')
    f.close()

# os.remove(letter + '.txt')