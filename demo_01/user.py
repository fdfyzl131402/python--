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