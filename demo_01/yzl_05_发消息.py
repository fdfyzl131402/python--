# 打印列表中的每条文本信息


def show_messages(unprinted_message, completed_message):
    while unprinted_message:
        current_messages = unprinted_message.pop()
        print(f"{current_messages}")
        completed_message.append(current_messages)

        # 显示打印好的信息


def send_messages(completed_message):
    print("\n打印好的信息是:")
    for sent_messages in completed_message:
        print(sent_messages)


unprinted_messages = ["c", "c++", "python"]
completed_messages = []

show_messages(unprinted_messages, completed_messages)
send_messages(completed_messages)

