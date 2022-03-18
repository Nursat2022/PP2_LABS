import os

WORKING_DIR = os.getcwd()

print('DIRS:')
for item in os.listdir(WORKING_DIR):
    target_path = os.path.join(WORKING_DIR, item)
    if os.path.isdir(target_path):
        print(item)

print('FILES:')
for item in os.listdir(WORKING_DIR):
    target_path = os.path.join(WORKING_DIR, item)
    if os.path.isfile(target_path):
        print(item)

print('ALL FILES AND DIRECTORIES:')
for item in os.listdir(WORKING_DIR):
    target_path = os.path.join(WORKING_DIR, item)
    if os.path.isdir(target_path):
        print(f'DIR: {item}')
    if os.path.isfile(target_path):
        print(f'FILE: {item}')    
