""""
drawing ting
"""
import arcade

arcade.open_window(600, 600, "Drawing")

arcade.set_background_color((arcade.color.CHARCOAL))
arcade.start_render()

arcade.draw_ellipse_filled( 300, 300, 250, 300, arcade.color.DARK_BROWN)
arcade.draw_ellipse_filled( 235, 305, 100, 70, arcade.color.WHITE)
arcade.draw_ellipse_filled( 360, 305, 120, 20, arcade.color.WHITE)
arcade.draw_ellipse_filled( 300, 255, 35, 40, arcade.color. DARK_CHESTNUT)
arcade.draw_ellipse_filled( 240, 299, 35, 40, arcade.color. BLACK)
arcade.draw_ellipse_filled( 359, 304, 35, 27, arcade.color. BLACK)
arcade.draw_ellipse_filled( 305, 200, 115, 40, arcade.color.WHITE)
arcade.draw_ellipse_filled( 304.9, 190, 85, 30, arcade.color.BROWN)
arcade.draw_ellipse_filled( 295.5, 450, 320, 200, arcade.color.BLACK)
arcade.draw_ellipse_filled( 300, 439, 35, 40, arcade.color.GRAY)


arcade.draw_circle_filled(500, 550, 40, arcade.color.WHITE)

arcade.draw_rectangle_filled(300, 122, 60, 60, arcade.color.BLACK)

arcade.draw_ellipse_filled( 295.5, 5, 320, 200, arcade.color.BLACK)



arcade.finish_render()

arcade.run()

