filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(f"../files/ce7/{filename}", "r")
    content = file.read()
    file.close()
    print(content)