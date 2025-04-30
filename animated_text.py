from flet import *
from components.Reng import Reng

class Animated_Text(Text):
    def __init__(self, content: str, animation_duration: int = 800, size: int = 30, color: Colors = Reng.TEXT_COLOR):
        super().__init__(content)  # Initialize with the given text content
        self.size = size  # Set font size
        self.weight = FontWeight.BOLD  # Set the font weight to bold
        self.color = color  # Set the color from Reng or a passed value
        
        # Animation settings
        self.opacity = 0  # Start with opacity 0 (invisible)
        self.offset = Offset(0, -20)  # Start slightly above the normal position
        
        # Animation: fade in and move into place
        self.animate_opacity = Animation(duration=animation_duration, curve=AnimationCurve.EASE_IN_OUT)
        self.animate_offset = Animation(duration=animation_duration, curve=AnimationCurve.EASE_IN_OUT)
        
       
        
        # Additional options can be added, like size transitions, if needed
        
    def set_text(self, content: str):
        """Function to update text dynamically"""
        self.content = content
        self.update()  
        