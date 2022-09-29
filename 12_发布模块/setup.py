from distutils.core import setup

setup(name="yzl_message",  # 包名
      version="1.0",  # 版本
      description="yzl's 发送和接受信息模块",  # 描叙信息
      long_description="完整的发送和接收信息模块",  # 完整描述信息
      author="yzl",  # 作者
      author_email="2043399264@qq.com",  # 作者的联系邮箱
      url="www.yzl.com",  # 主页
      py_modules=["yzl_message.send_message",
                  "yzl_message.receive_message"])