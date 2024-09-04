import glob

myfiles = glob.glob("**/*.txt", recursive=True)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(str(filepath).upper() + "\n" + file.read())

print(myfiles)