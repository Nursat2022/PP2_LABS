import os

path = input()
# path = r'C:/Users/User/Desktop/PP2/pp2_lab'
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print('is not exist')    
