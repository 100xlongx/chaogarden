from __future__ import annotations

import tcod

class Scene:
    def render(self, console: tcod.Console) -> None:
        console.print(x=0, y=0, string="Hello World!")

class MainGame(Scene):
    def render(self, console: tcod.Console) -> None:
        console.print(x=0, y=0, string="Hello World!")