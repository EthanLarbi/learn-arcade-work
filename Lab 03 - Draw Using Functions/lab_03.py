import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_ground():
    arcade.draw_lrtb_rectangle_filled(0, 800, 165, 0, arcade.color.GRAY)

def draw_window(x,y):
    arcade.draw_rectangle_filled(x, y, 90, 120, arcade.color.BONE)
    arcade.draw_rectangle_filled(x, y, 80, 110, arcade.color.BLUEBERRY)

def draw_birds(x,y):
    arcade.draw_arc_outline(x - 15, y, 35, 30, arcade.color.BLACK, 0, 180, 3)
    arcade.draw_arc_outline(x + 17, y, 39, 30, arcade.color.BLACK, 0, 180, 3)
    arcade.draw_circle_filled(x, y, 4, arcade.color.BLACK)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3")
    arcade.set_background_color(arcade.color.DARK_GREEN)
    arcade.start_render()



    draw_window(400, 380)
    draw_window(100, 500)
    draw_window(100, 230)
    draw_window(700, 500)
    draw_window(700, 230)


    draw_birds(100,490)
    draw_birds(100, 220)
    draw_birds(400, 380)
    draw_birds(696, 500)
    draw_birds(699, 220)

    arcade.finish_render()
    arcade.run()

main()


