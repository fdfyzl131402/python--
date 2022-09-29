current_users_0 = ["Admin", "Jaden", "Join", "Bob", "Alice"]
new_users = ["admin", "eric", "bob", "jordan", "mike"]
current_users_1 = []
for current_users in current_users_0:
    current_users_1.append(current_users.lower())
print(current_users_1)
for new_user in new_users:
    if new_user.lower() in current_users_1:
        print(f"你输入的{new_user}被占用，请在输入一个")

    else:
        print(f"你输入的{new_user}是新的")

