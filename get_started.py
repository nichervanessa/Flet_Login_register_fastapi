import asyncio
from flet import *

class ProfessionalGetStartedButton(Container):
    def __init__(self, on_click=None):
        super().__init__()
        self.width=320
        self.height=45
        self.padding=0
        self.on_click_callback = on_click

        self.scale = transform.Scale(1)
        self.icon_opacity = 0.0
        self.shadow = BoxShadow(
            spread_radius=0,
            blur_radius=0,
            color=Colors.BLUE_900,
            offset=Offset(0, 0)
        )

        self.button = TextButton(
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    Text(
                        "GET STARTED",
                        style=TextStyle(
                            color=Colors.BLACK,
                            weight=FontWeight.W_600,
                            size=16
                        )
                    ),
                    Icon(
                        name=Icons.ARROW_FORWARD,
                        color=Colors.BLACK,
                        size=18,
                        opacity=self.icon_opacity
                    )
                ]
            ),
            icon=Icons.ARROW_FORWARD_OUTLINED,
            style=ButtonStyle(
                icon_color=Colors.BLACK,
                icon_size=45,
                padding=padding.symmetric(horizontal=30, vertical=18),
                shape=RoundedRectangleBorder(radius=15),
                bgcolor=Colors.AMBER,
                overlay_color=Colors.TRANSPARENT,
                animation_duration=300,
            ),
            on_click=self._handle_click,
        )

        self.content = self.button
        self.bgcolor = Colors.AMBER
        self.border_radius = 15
        self.shadow = self.shadow
        self.animate_scale = animation.Animation(300, AnimationCurve.BOUNCE_OUT)
        self.animate_opacity = animation.Animation(200, AnimationCurve.BOUNCE_IN)
        self.scale = self.scale
        self.on_hover = self._handle_hover

    def _handle_hover(self, e):
        hover = e.data == "true"
        self.scale = transform.Scale(1.05 if hover else 1)
        self.shadow = BoxShadow(
            spread_radius=2 if hover else 0,
            blur_radius=15 if hover else 0,
            color=Colors.BLUE_900,
            offset=Offset(0, 5) if hover else Offset(0, 0),
        )
        self.button.content.controls[1].opacity = 1.0 if hover else 0.0  # Arrow icon fade
        self.update()

    async def _handle_click(self, e):
        self.scale = transform.Scale(0.95)
        self.update()
        await asyncio.sleep(0.1)
        self.scale = transform.Scale(1.05)
        self.update()
        if self.on_click_callback:
            self.on_click_callback(e)
