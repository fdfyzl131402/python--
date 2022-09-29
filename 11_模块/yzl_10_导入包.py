import yzl_message

yzl_message.send_message.send("hello")
txt = yzl_message.receive_message.receive()
print(txt)