from user import User


class Privileges:
    """存储权限"""
    def __init__(self, privileges=[]):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"you can privilege {privilege}")


class Admin(User):
    """用户类"""
    def __init__(self, first_name, last_name, height):
        super().__init__(first_name, last_name, height)
        self.privileges = Privileges()