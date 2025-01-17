import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 4

class Ball:
    def __init__(self, position_x, position_y, radius, color, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_circle_filled(self.position_x + 5,
                                          self.position_y,
                                          self.radius,
                                          self.color)
        arcade.draw_circle_filled(self.position_x + 10,
                                          self.position_y,
                                          self.radius,
                                          self.color)


    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
class Keyboard:
    def __init__(self, position_x, position_y, radius, color, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

        self.change_x = change_x
        self.change_y = change_y

        self.hit_sound = arcade.load_sound(":resources:sounds/error1.wav")

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_circle_filled(self.position_x,
                                          self.position_y + 5,
                                          self.radius,
                                          self.color)
        arcade.draw_circle_filled(self.position_x,
                                          self.position_y + 10,
                                          self.radius,
                                          self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.hit_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.hit_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.hit_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.hit_sound)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.DARK_GREEN)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN, 0, 0)
        self.keyboard = Keyboard(50, 50,15, arcade.color.WHITE, 0, 0)

        self.hit_sound = arcade.load_sound(":resources:sounds/error1.wav")

    def update(self, delta_time: float):

        self.keyboard.update()
        self.ball.update()

    def draw_window(self,x , y):
        arcade.draw_rectangle_filled(x, y, 90, 120, arcade.color.BONE)
        arcade.draw_rectangle_filled(x, y, 80, 110, arcade.color.BLUEBERRY)





    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.draw_window(130, 100)
        self.draw_window(500, 330)
        self.ball.draw()
        self.keyboard.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.hit_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.hit_sound)

    def on_key_press(self, key, modifiers):
            """ Called whenever the user presses a key. """
            if key == arcade.key.LEFT:
                self.keyboard.change_x = -MOVEMENT_SPEED
                print("up")
            elif key == arcade.key.RIGHT:
                self.keyboard.change_x = MOVEMENT_SPEED
            elif key == arcade.key.UP:
                self.keyboard.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.keyboard.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.keyboard.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.keyboard.change_y = 0

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()