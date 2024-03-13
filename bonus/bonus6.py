contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/bonus6/{filename}", "w")
    file.write(content)
