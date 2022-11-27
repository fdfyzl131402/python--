from io import StringIO, BytesIO

s_io = StringIO()
s_io.write("yzl")
s_io.write("sss")

# file 需要的是一个文件流对象
# print("hello", file="text.csv")
print("hello", file=s_io)
print("world", file=s_io)
print(s_io.getvalue())
s_io.close()
b_io = BytesIO()
b_io.write("HHH".encode("utf8"))
print(b_io.getvalue().decode("utf8"))
b_io.close()
