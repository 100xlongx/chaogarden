#!/usr/bin/env python3
import tcod

screen_width = 80
screen_height = 50

def main() -> None:
    tileset = tcod.tileset.load_tilesheet("assets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    with tcod.context.new_terminal(screen_width, screen_height, tileset=tileset, title='hello world', vsync=True) as context:
        console = tcod.Console(screen_width, screen_height, order = 'F')

        while True:
            context.present(console)



if __name__ == "__main__":
    main()