import glob

myfiles = glob.glob("../files/**/*.txt", recursive=True)

print("Reading files...")
for filepath in myfiles:
    print(f"\n{filepath}")
    with open(filepath, "r") as file:
        print(file.read())

print("Finished!")
