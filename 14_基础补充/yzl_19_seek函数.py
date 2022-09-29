# f = open("text.txt", "r+")
f = open("text.txt", "a+")

# f.seek(0, 2)
f.seek(0, 0)
con = f.read()
print(con)


