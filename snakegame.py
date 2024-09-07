import pygame
import random

pygame.init()  # initialize pygame

#screen dimentions
width, height =600,600
game_screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Nandakishore's Snake game")

snake_x,snake_y=width/2,height/2
change_x,change_y=0,0

food_x,food_y=random.randrange(0,width)//10*10, random.randrange(0,height)//10*10
food_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

clock = pygame.time.Clock() # frame rate controller

snake_body = [(snake_x,snake_y)]

def display_snake():  # function to display and move the snake
    global snake_x,snake_y, food_x,food_y,food_color
    snake_x=(snake_x+change_x)%width  #wrap  around the screen horozontally
    snake_y=(snake_y+change_y)%height #wrap around the screen vertically

    if((snake_x,snake_y) in snake_body[1:]):
        print("Game Over!")
        quit()

    snake_body.append((snake_x,snake_y))  #snake body increasing

    #for snake length increasing after eating 
    if(food_x==snake_x and food_y==snake_y):
        food_x,food_y=random.randrange(0,width)//10*10, random.randrange(0,height)//10*10
        food_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    else: 
        del snake_body[0]
    
    game_screen.fill([0,0,0])  # clear the screen and draw the snake
    for (x,y) in snake_body:
        pygame.draw.rect(game_screen,(255,0,0),[x, y, 10, 10])
    pygame.draw.rect(game_screen,food_color,[food_x, food_y, 10, 10])
    pygame.display.update()

while True: 
    events= pygame.event.get()
    for event in events:
        if(event.type==pygame.QUIT):
            pygame.QUIT
            quit()
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                change_x=-10
                change_y=0
            elif(event.key==pygame.K_RIGHT):
                change_x=10
                change_y=0
            elif(event.key==pygame.K_UP):
                change_x=0
                change_y=-10
            elif(event.key==pygame.K_DOWN):
                change_x=0
                change_y=10
    display_snake()
    clock.tick(10)
