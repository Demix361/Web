from .models import Color


class ColorBuilder():
    name = None

    def with_name(self, name: str):
        self.name = name
    
    def build(self):
        return Color(name = self.name)
