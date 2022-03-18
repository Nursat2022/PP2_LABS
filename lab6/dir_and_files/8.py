import os

WORKING_DIR = os.getcwd()

# f = open('input8', 'x')

path = os.path.join(WORKING_DIR, 'input8')
if os.access(path, os.F_OK):
    os.remove(path)
else:
    print('no such file')    