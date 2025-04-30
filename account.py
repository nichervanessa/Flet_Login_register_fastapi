from flet import *
from components.Reng import Reng
import httpx
import asyncio
import requests
from datetime import datetime

# ------------------------------- LOGIN PAGE -------------------------------

class LoginPage(Container):
    def __init__(self, switch_to_register, switch_to_account):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.bgcolor = Reng.BACKGROUND_COLOR

        self.username = TextField(
            label="Username",
            width=350,
            border=InputBorder.UNDERLINE,
            prefix_icon=Icons.PERSON_2_OUTLINED
        )
        self.password_field = TextField(
            label="Password",
            password=True,
            width=350,
            border=InputBorder.UNDERLINE,
            prefix_icon=Icons.PASSWORD_OUTLINED
        )
        self.status = Text("", color="red")
        self.switch_to_account = switch_to_account
        self.switch_to_register = switch_to_register

        self.login_btn = TextButton(
            "Login",
            icon=Icons.LOGIN_OUTLINED,
            on_click=self.req_login,
            width=300,
            height=45,
            style=ButtonStyle(
                color=Colors.BLACK,
                bgcolor=Colors.AMBER,
                icon_color=Colors.WHITE
            )
        )

        self.content = Container(
            padding=100,
            alignment=alignment.center,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    CircleAvatar(
                        foreground_image_src="https://example.com/avatar.jpg",
                        content=Text("Sign In"),
                        width=200,
                        height=200,
                    ),
                    self.username,
                    self.password_field,
                    self.login_btn,
                    TextButton(
                        "Don't have an account? Register",
                        on_click=lambda e: self.switch_to_register(e),
                        style=ButtonStyle(
                            text_style=TextStyle(
                                color=Colors.BLUE,
                                size=15,
                                decoration=TextDecoration.UNDERLINE
                            ),
                            bgcolor=Reng.BACKGROUND_COLOR
                        )
                    ),
                    self.status
                ]
            )
        )

    def req_login(self, e):
        data = {
            "username": self.username.value,
            "password": self.password_field.value
        }

        try:
            response = requests.post("http://127.0.0.1:8000/login", json=data)
            if response.status_code == 200:
                self.status.value = "Login Successful!"
                self.status.color = "green"
                self.switch_to_account(e)
            else:
                self.status.value = "Login failed. Please check credentials."
                self.status.color = "red"
        except Exception as ex:
            self.status.value = f"Error: {ex}"
            self.status.color = "red"
        
        self.update()


def login_Page(page):
    return LoginPage(page)


# ------------------------------- REGISTER PAGE -------------------------------

class RegisterPage(Container):
    def __init__(self, switch_to_login):
        super().__init__()
        self.expand = True
        self.switch_to_login = switch_to_login
        self.status = Text("", color="red")
        self.alignment = alignment.center
        self.bgcolor = Reng.BACKGROUND_COLOR

        self.username = TextField(label="Username", width=300, border=InputBorder.UNDERLINE)
        self.email = TextField(label="Name", width=300, border=InputBorder.UNDERLINE)
        self.password_field = TextField(label="Password", password=True, width=300, border=InputBorder.UNDERLINE)

        self.snack_bar = SnackBar(Text(""))

        self.content = Container(
            padding=100,
            alignment=alignment.center,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    CircleAvatar(
                        background_image_src="https://example.com/avatar2.jpg",
                        width=200,
                        height=200,
                    ),
                    self.username,
                    self.email,
                    self.password_field,
                    TextButton(
                        "Register",
                        on_click=self.req_register,
                        width=320,
                        height=48,
                        icon=Icons.APP_REGISTRATION,
                        style=ButtonStyle(
                            color=Colors.BLACK,
                            bgcolor=Colors.AMBER,
                            icon_color=Colors.BLACK
                        )
                    ),
                    TextButton(
                        "Already have an account? Login",
                        on_click=lambda e: self.switch_to_login(e),
                        icon=Icons.APP_REGISTRATION_OUTLINED,
                        style=ButtonStyle(
                            color=Colors.BLUE,
                            bgcolor=Reng.BACKGROUND_COLOR,
                            icon_color=Colors.BLACK,
                            text_style=TextStyle(
                                size=15,
                                color=Colors.BLUE,
                                decoration=TextDecoration.UNDERLINE
                            )
                        ),
                    ),
                    self.snack_bar
                ]
            )
        )

    def req_register(self, e):
        data = {
            "username": self.username.value,
            "name": self.email.value,
            "role": "user",  # Default role, or add a role selector
            "password": self.password_field.value
        }

        try:
            response = requests.post("http://127.0.0.1:8000/register", json=data)
            if response.status_code == 201:
                self.snack_bar.content.value = "Registration Successful!"
                self.snack_bar.bgcolor = Colors.GREEN
            elif response.status_code == 400:
                self.snack_bar.content.value = "User already exists."
                self.snack_bar.bgcolor = Colors.RED
            else:
                self.snack_bar.content.value = "Registration failed."
                self.snack_bar.bgcolor = Colors.RED
        except Exception as ex:
            self.snack_bar.content.value = f"Error: {ex}"
            self.snack_bar.bgcolor = Colors.RED

        self.snack_bar.open = True
        self.page.update()


def register_Page(page):
    return RegisterPage(page)


# ------------------------------- ACCOUNT PAGE -------------------------------

class AccountPage(Container):
    def __init__(self, logout):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.bgcolor = Reng.BACKGROUND_COLOR

        self.content = Container(
            alignment=alignment.center,
            padding=100,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=alignment.center,
                controls=[
                    Text(
                        "Business Management System",
                        size=24,
                        weight=FontWeight.BOLD,
                        color=Colors.BLUE_700,
                        text_align=TextAlign.CENTER,
                    ),
                    Text(
                        "Your All-in-One Solution for Smarter Business Management",
                        size=15,
                        color="blue",
                        weight=FontWeight.W_600,
                        text_align=TextAlign.CENTER
                    ),
                    TextButton(
                        "Next",
                        on_click=lambda e: logout(e),
                        width=320,
                        height=45,
                        icon=Icons.ARROW_FORWARD_OUTLINED,
                        style=ButtonStyle(
                            color=Colors.BLACK,
                            bgcolor=Colors.AMBER,
                            icon_color=Colors.BLACK,
                        ),
                    ),
                    TextButton(
                        "Back",
                        on_click=lambda e: logout(e),
                        width=320,
                        height=45,
                        icon=Icons.ARROW_BACK_OUTLINED,
                        style=ButtonStyle(
                            color=Colors.BLACK,
                            bgcolor=Colors.AMBER,
                            icon_color=Colors.BLACK,
                        ),
                    ),
                ]
            )
        )


def account_Page(page):
    return AccountPage(page)


class ResetPasswordPage(Container):
    def __init__(self, switch_to_login):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.bgcolor = Reng.BACKGROUND_COLOR

        self.username = TextField(label="Username", width=300)
        self.new_password = TextField(label="New Password", password=True, width=300)
        self.status = Text("", color="red")

        self.content = Container(
            padding=80,
            alignment=alignment.center,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.username,
                    self.new_password,
                    TextButton(
                        "Reset Password",
                        icon=Icons.LOCK_RESET,
                        on_click=self.reset_password,
                        style=ButtonStyle(bgcolor=Colors.AMBER)
                    ),
                    self.status,
                    TextButton(
                        "Back to Login",
                        on_click=lambda e: switch_to_login(e)
                    )
                ]
            )
        )

    def reset_password(self, e):
        data = {
            "username": self.username.value,
            "new_password": self.new_password.value
        }
        try:
            response = requests.post("http://127.0.0.1:8000/reset-password", json=data)
            if response.status_code == 200:
                self.status.value = "Password reset successful"
                self.status.color = "green"
            else:
                self.status.value = "Failed to reset password"
        except Exception as ex:
            self.status.value = f"Error: {ex}"
        self.update()

