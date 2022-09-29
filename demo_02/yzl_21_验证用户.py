import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_username():
    """提示用户输入用户名"""
    username = input("请输入用户名:")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def get_user():
    """问候用户，打印招呼"""
    username = get_stored_username()
    # 查看用户是否记得他自己的用户名
    if username:
        your_user = input("请输入你的用户名:")
        if your_user == username:
            print(f"欢迎回来,{your_user}")
        else:
            username = get_username()
            print(f"We'll remember you when you come back ,{username}")


get_user()

