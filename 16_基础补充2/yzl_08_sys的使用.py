import sys
# sys.stdin
# sys.stdout
# sys.stderr

s_in = sys.stdin

# while True:
#     content = s_in.readline()
#     print(content)
#
sys.stdout = open("stdout.txt", "w")
print("hello")
sys.stderr = open("stderr.txt", "w")
print(1 / 0)