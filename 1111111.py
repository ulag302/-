#pip install pygame
import pygame
import time
import random

def food():
    global foodx, foody
    while True:
        foodx = random.randrange(10, DISPLAY_SIZE[0] - SNAKE_SIZE, SNAKE_SIZE)
        foody = random.randrange(10, DISPLAY_SIZE[1] - SNAKE_SIZE, SNAKE_SIZE)
        food_pos = [foodx, foody]
        if food_pos in [snake_pos_x, snake_pos_y]:
            continue
        else :
            break
        
def message(fonts, msg, color, posx, posy):
    mesg = fonts.render(msg, True, color)
    mesg_Rect = mesg.get_rect()
    mesg_Rect.centerx = posx
    mesg_Rect.centery = posy
    screen.blit(mesg, mesg_Rect)

#food
foodx = None
foody = None

DISPLAY_SIZE = (800,600)

#snake
snake_tail = 1
SNAKE_SIZE = 20
snake_pos_x = DISPLAY_SIZE[0]/2 - SNAKE_SIZE/2
snake_pos_y = DISPLAY_SIZE[1]/2 - SNAKE_SIZE/2
snake_pos_x_change = 0
snake_pos_y_change = 0
snake_list = []
snake_speed = 5
score = 0

def snake(SNAKE_SIZE, snake_list):
    for pos in snake_list:
        print(pos)
        pygame.draw.rect(screen, RED, \
                         [pos[0], pos[1],
                          SNAKE_SIZE,
                          SNAKE_SIZE])

#color
RED = (255,0,0); GREEN = (0,255,0)
BLUE = (0,0,255); WHITE = (255,255,255) 
GRAY = (127,127,127)


pygame.init()
#fonts
font_gameOver = pygame.font.SysFont(None, 50)
font_madeBy = pygame.font.SysFont(None, 20)
font_score = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("SNAKE GAME ver 0.1")
food()
print(foodx, foody)

running = True

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_pos_x_change = 0
                snake_pos_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_pos_x_change = 0
                snake_pos_y_change = 20
            elif event.key == pygame.K_LEFT:
                snake_pos_x_change = -20
                snake_pos_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_pos_x_change = 20
                snake_pos_y_change = 0
            
    snake_pos_x += snake_pos_x_change
    snake_pos_y += snake_pos_y_change
    snake_head = []
    snake_head.append(snake_pos_x)
    snake_head.append(snake_pos_y)
    snake_list.append(snake_head)
    print(snake_list)
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, [0,0, DISPLAY_SIZE[0], DISPLAY_SIZE[1]],10)
    if len(snake_list) > snake_tail :
        del snake_list[0]
    snake(SNAKE_SIZE, snake_list)
    
    pygame.draw.rect(screen, BLUE, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])
    message(font_score, "Score : " + str(score), GREEN, DISPLAY_SIZE[0]/2, 30)
    
    if snake_pos_x >= (DISPLAY_SIZE[0] - SNAKE_SIZE) or \
       snake_pos_x - (SNAKE_SIZE/2) < 0 or \
       snake_pos_y >= (DISPLAY_SIZE[1] - SNAKE_SIZE) or \
       snake_pos_y - (SNAKE_SIZE/2 ) < 0 :
        running = False
    if snake_pos_x == foodx and snake_pos_y == foody :
        #print("Yummy!")
        snake_speed = snake_speed + 1
        score = score + 10
        print(score)
        snake_tail += 1
        food()
        
        
        
    pygame.display.update()
    clock.tick(snake_speed)

message(font_gameOver, 'Game Over', RED, int(DISPLAY_SIZE[0]/2), int(DISPLAY_SIZE[1]/2))
message(font_madeBy, 'user', GRAY, int(DISPLAY_SIZE[0]/2), int(DISPLAY_SIZE[1]/2)+30)
pygame.display.update()
time.sleep(3)
pygame.quit()
