class User(object):
    """保存用户信息并打招呼"""
    def __init__(self, first_name, last_name, height):
        """初始化用户"""
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        """描述用户"""
        print(f"{self.first_name}{self.last_name}的身高是{self.height}")

    def greet_user(self):
        print(f"Hello, {self.first_name}{self.last_name}")

    def increment_login_attempts(self):
        """属性值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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
    # def privileges(self):
    #     permissions = ["can add post", "can delete post", "can ban user"]
    #     print(permissions)


# 创建对象
xiaoming = User("xiao", "ming", 1.75)
xiaohua = User("xiao", "hua", 1.80)
xiaomei = Admin("xiao", "mei", 1.65)

# 调用方法
xiaoming.describe_user()
xiaoming.greet_user()
xiaohua.describe_user()
xiaohua.greet_user()
xiaomei.privileges.show_privileges()
# xiaomei.privileges()
# 确认属性值变化
for n in range(4):  # n 没有实际意义，主要是为了循环多次
    xiaohua.increment_login_attempts()
xiaohua.increment_login_attempts()
xiaohua.increment_login_attempts()
print(xiaohua.login_attempts)
xiaohua.reset_login_attempts()
print(xiaohua.login_attempts)
print(xiaohua)