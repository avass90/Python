import os
for file in os.listdir(path='C:\\pythonstep159\\'):
    if file.endswith('.txt'):
        txtFiles = os.path.join('C:\\pythonstep159\\', file)
        print(txtFiles,os.path.getmtime(txtFiles))



