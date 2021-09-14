import random
import time

import arcade

class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'img/pear.jpg'
        self.pear = arcade.Sprite(self.img , 0.09)
        self.pear.center_x = random.randint(0, w)
        self.pear.center_y = random.randint(0, h)

    def draw(self):
        self.pear.draw()

class Chocolate(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'img/choco.jpg'
        self.choco = arcade.Sprite(self.img , 0.09)
        self.choco.center_x = random.randint(0, w)
        self.choco.center_y = random.randint(0, h)

    def draw(self):
        self.choco.draw()        

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'img/apple.jpg'
        self.apple = arcade.Sprite(self.img , 0.09)
        self.apple.center_x = random.randint(0, w)
        self.apple.center_y = random.randint(0, h)

    def draw(self):
        self.apple.draw()
        
class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.SEA_GREEN
        self.speed = 3
        self.width = 16
        self.height = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []
        self.body.append([self.center_x, self.center_y])

    def draw(self):        
        for i in range(len(self.body)):
            if i % 3 == 0:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, self.color)
            elif i % 3 == 1:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, arcade.color.RED)
            else:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, arcade.color.YELLOW_ROSE)
       
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y


    def eat(self , n):
        if n == 'apple':
            self.score += 1
        elif n == 'pear':
            self.score += 2
        elif n == 'chocolate':
            self.score -= 1   

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 600, 500, 'Super Snake')
        arcade.set_background_color(arcade.color.PURPLE_TAUPE)
        self.snake = Snake(600, 500)
        self.apple = Apple(600, 500)
        self.pear = Pear(600, 500)
        self.chocolate = Chocolate(600, 500)

    def on_draw(self):
        #نمایش اشیاء داخل بازی 
        arcade.start_render()
        if self.snake.center_x <= 0 or self.snake.center_x >= 600 \
            or self.snake.center_y <= 0 or self.snake.center_y >= 500 \
                or self.snake.score < 0 :
            
            arcade.draw_text('Game Over', start_x= 120, start_y= 250,   
                color= arcade.color.OLD_GOLD, font_size = 50)
            arcade.exit()
        else:
            self.snake.draw()
            self.apple.draw()
            self.pear.draw()
            self.chocolate.draw()

            arcade.draw_text('Score: %i'%self.snake.score, start_x= 10, start_y= 10,
            color= arcade.color.PINK, font_size = 20)

    def on_update(self, delta_time: float):
        #تمام منطق و اتفاقات بازی این تابع رخ میده
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.eat('apple')
            self.snake.body.append([self.snake.body[len(self.snake.body)-1][0],
             self.snake.body[len(self.snake.body)-1][1]])
            self.apple = Apple(600, 500)

        elif arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.eat('pear')
            self.snake.body.append([self.snake.body[len(self.snake.body)-1][0],
             self.snake.body[len(self.snake.body)-1][1]])
            self.pear = Pear(600, 500)

        elif arcade.check_for_collision(self.snake, self.chocolate.choco):
            self.snake.eat('chocolate')
            self.chocolate = Chocolate(600, 500)

    def on_key_release(self, key, modifiers):
        #هرتابعی روی کیبورد فشرده شود و سپس رها بشه این تابع اجرا میشه
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif key == arcade.key.RIGHT:
            self.snake.change_x = +1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = +1
        
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

game = Game()
arcade.run()