filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"../files/ce6/{filename}", "w")
    file.write("Hello")
    file.close()