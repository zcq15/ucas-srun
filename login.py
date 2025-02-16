from UCASSrunLogin.LoginManager import LoginManager

username = input("please enter your username: ")
password = input("please enter your password: ")

lm = LoginManager()
lm.login(
    username = f"{username}",
    password = f"{password}"
)

print('在公用服务器上登录校园网账户后，为避免流量误用，请在网络使用完毕后，及时下线账户！')
