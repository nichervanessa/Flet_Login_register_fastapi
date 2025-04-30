from flet import *
from components.Reng import Reng
from flet_lottie import Lottie as ANIMATED
from components.get_started import ProfessionalGetStartedButton
from Pages.account import AccountPage,LoginPage,RegisterPage
class MainRootApplication(Container):
    def  __init__(self,page:Page):
        super().__init__()
        self.page=page
        self.bgcolor=Reng.BACKGROUND_COLOR
        self.page.window.width=1000
        self.page.window.height=600
        self.page.padding=0
        self.padding=0
        self.page.window.center()
        self.page.window.frameless=True
        self.page.vertical_alignment=MainAxisAlignment.CENTER
        self.page.horizontal_alignment=CrossAxisAlignment.CENTER
        self.lottie =ANIMATED(
        src='https://lottie.host/4d52d688-cb08-4677-a4b7-e5b194fad3a1/0Fj7ErDx4u.json',
        reverse=False,
        animate=True,
        background_loading=True,
        expand=True,
        repeat=True,
        tooltip="Loading",
        fit=ImageFit.COVER
        )

        self.start_btn=ProfessionalGetStartedButton(on_click=self.show_account)
        self.welcome_text =Text(
        "Welcome to My App!",
        size=30,
        weight=FontWeight.BOLD,
        opacity=0,
        offset=Offset(0, -1),
        animate_opacity=Animation(duration=800, curve=AnimationCurve.EASE_IN),
        animate_offset=Animation(duration=800, curve=AnimationCurve.EASE_OUT),

        )
        
        self.page.add(self.lottie,self.start_btn)
        self.page.update()
    def show_account(self,e):
        self.page.controls.clear()
        self.page.controls.append(AccountPage(logout=self.show_login))
        self.page.update()
    def show_login(self,e):
        self.page.controls.clear()
        self.page.controls.append(LoginPage(switch_to_register=self.show_register, switch_to_account=self.show_account))
        self.page.update()

    def show_register(self,e):
        self.page.controls.clear()
        self.page.controls.append(RegisterPage(switch_to_login=self.show_login))
        self.page.update()
app(target=MainRootApplication,assets_dir="assets",view=AppView.FLET_APP)