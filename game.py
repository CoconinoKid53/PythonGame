import pygame
pygame.init()

Width , Height = 600, 500
Win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pong")

FPS = 60

RED = (255, 255, 255)
BLACK = (0, 0, 0)

def draw(win):
    PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
    BALL_RADIUS = 7
    win.fill(BLACK)
class Paddle:
    COLOR = RED
    vel = 4


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, WIN):
        pygame.draw.rect()
        pygame.draw.rectangle(win, self.COLOR, (self.x, self.y, self.width. self.height))

    pygame.display.update()
    if up:
        self.y -= self.VeL
    else:
        def move(self, up=TRUE):
            self.y +=self.VEL

class Ball:
    MAX_VEL = 5
    COLOR = GREEN

    def_init_(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.x_vel = MAX_VEL
    self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR,(self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel



def draw(win,paddles, ball):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)
    for  i in range(10, Height, Height//20):
         if i % 2==1:
            continue
        pygame.draw.rect(win, RED, (WIDTH//2 - 5, i, 10, Height//20 ))
    ball.draw(win)
    pygame.display.update()


def handle_collison(ball, left_paddle, right_Paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1


    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_principle = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_principle
                ball.y_vel = y_vel
    else:
        if ball.y >= right_paddle.y and ball.x <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                
                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_principle = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_principle
                ball.y_vel = y_vel


def handle_paddle_movement(keys, left_Paddle, right_paddle):
    if keys[pygame.K_w] and  left_Paddle.y - left_Paddle.VEL >= 0:
        left_Paddle.move(up=True)
    if keys[pygame.K_s] and left_Paddle.y + left_Paddle.VEL + left_Paddle.height <= HEIGHT:
        left_Paddle.move(up=False)

     if keys[pygame.K_UP]: and right_Paddle.y - right_Paddle.VEL >= 0:
        right_Paddle.move(up=True)
    if keys[pygame.K_DOWN]:and right_Paddle.y + right_Paddle.VEL + right_Paddle.height <= HEIGHT:
        right_Paddle.move(up=False)

    




def main():
    run = True
    clock = pygame.time.Clock()

    
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
    
    While run:
        clock.tick(FPS)
        draw(WIN [left_Paddle, right_paddle], ball)

        for event in pygame.event.get():
            left_Paddle = paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2)
            right_paddle = paddle(width - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH)
            if event.type == pygame.Quit:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collison(ball, left_Paddle, right_paddle)
    pygame.quit()

if __name__ == '_main_':
    main()