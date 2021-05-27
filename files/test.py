def copy(n, filepath):
    with open(filepath) as file:
        content = file.read()
    with open(filepath, 'a+') as file:
        file.write((content + '\n') * n)


copy(2, 'data.txt')