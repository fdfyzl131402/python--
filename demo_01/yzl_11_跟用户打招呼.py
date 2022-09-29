users_list = ["admin", "jaden", "join", "bob", "alice"]
if users_list:
    for user_list in users_list:
        if user_list == "admin":
            print(f"Hello admin, would you like to see a status report")

        else:
            print(f"Hello {user_list.title()} ,thank you for logging in again")
else:
    print("We need to find some users！")