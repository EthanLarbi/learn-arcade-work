""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.2
BALL_COUNT = 50
GHOST_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ball(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 50,
                                         SCREEN_HEIGHT + 100)

        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 0.5

        if self.top < 0:
            self.reset_pos()


class Ghost(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.ball_list = None
        self.ghost_list = None


        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        self.ball_sound = arcade.load_sound("goodsound.wav")
        self.ghost_sound = arcade.load_sound("impact.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        self.ghost_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("pacman.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(BALL_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            ball = Ball("red ball.gif", SPRITE_SCALING_COIN)

            # Position the coin
            ball.center_x = random.randrange(SCREEN_WIDTH)
            ball.center_y = random.randrange(SCREEN_HEIGHT)
            ball.change_x = random.randrange(-3, 4)
            ball.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.ball_list.append(ball)

        for i in range(GHOST_COUNT):

            ghost = Ghost("ghost.png", SPRITE_SCALING_COIN)

            # Position the coin
            ghost.center_x = random.randrange(SCREEN_WIDTH)
            ghost.center_y = random.randrange(SCREEN_HEIGHT)
            ghost.change_x = random.randrange(-3, 4)
            ghost.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.ghost_list.append(ghost)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ball_list.draw()
        self.player_list.draw()

        self.ghost_list.draw()

        if len(self.ball_list) == 0:
            arcade.draw_text("GAME OVER", 50, 50, arcade.color.WHITE, 80)


        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if len(self.ball_list) > 0:



            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.ball_list) > 0:
            self.ball_list.update()
            self.ghost_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.ball_list)
        for ball in hit_list:
            ball.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.ball_sound)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.ghost_list)


        for ghost in hit_list:
            ghost.remove_from_sprite_lists()
            self.score += -1
            arcade.play_sound(self.ghost_sound)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
