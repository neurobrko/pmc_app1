data = input("Datum: ")
mood = input("1 to 10: ")
thoughts = input("Napis cosi:\n")

with open(f"../files/bonus8/journal/{data}.txt", "w") as file:
    file.write(mood + "\n\n")
    file.write(thoughts)