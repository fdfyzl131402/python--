filename = "learning_python"

with open(filename) as file_object:
    txt = file_object.read()
    print(txt)
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
with open(filename) as file_object:
    lines = file_object.readlines()


for line in lines:
    print(line.replace("python", "C").rstrip())

