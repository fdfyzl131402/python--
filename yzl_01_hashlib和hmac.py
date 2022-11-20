import  hashlib

h1 = hashlib.md5('abc'.encode("utf8"))
print(h1.hexdigest())
h2 = hashlib.sha1('123456'.encode())
print(h2.hexdigest())