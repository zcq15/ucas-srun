from UCASSrunLogin.LoginManager import LoginManager

username = input("please enter your username:")
password = input("please enter your password:")

lm = LoginManager()
lm.logout(
    username = f"{username}",
    password = f"{password}"
)