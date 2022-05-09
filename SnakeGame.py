
import pygame
pygame.init()
import random

#game window
gamescreen = pygame.display.set_mode((800,600))
gamescreen_width = 600
gamescreen_height = 800


#colors
green = (0,255,0)
red=(255,0,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#gametitle
pygame.display.set_caption("The Snake Game")
font = pygame.font.SysFont(None, 55)

def text_gamescreen(text,color,x,y):
    gamescreentext=font.render(text,True,color)
    gamescreen.blit(gamescreentext,[x,y])



def plots(gamescreen,color,slist,ssize):
   for x,y in slist: 
     pygame.draw.rect(gamescreen,color,[x,y,ssize,ssize]) 

#creating game loop
def gameloop():
        
    #game specific variables
    exitgamescreen = False
    gameover = False
    sx=30
    sy=30
    ssize=20
    fps=60
    vel_x=0
    vel_y=0
    food_x = random.randint(20,gamescreen_width/2)
    food_y = random.randint(20,gamescreen_height/2)
    score = 0
    clock = pygame.time.Clock()
    font=pygame.font.SysFont(None,55)
    slist=[]
    slength=1
   
    while not exitgamescreen:
        if gameover:
            gamescreen.fill(black)
            text_gamescreen("Game Over!!! Press Enter To Continue",white,gamescreen_width/9,gamescreen_height/3)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgamescreen = True  

                if event.type==pygame.KEYDOWN:
                        if event.key ==pygame.K_RETURN:
                            gameloop()
       
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgamescreen = True  

                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_RIGHT:
                        vel_x=5
                        vel_y=0
                    
                
                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_LEFT:
                        vel_x=-5
                        vel_y=0

                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_DOWN:
                        vel_y=5
                        vel_x=0 
        
                
                if event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_UP:
                        vel_y=-5
                        vel_x=0 
            
            sx = sx + vel_x
            sy = sy + vel_y
            
            if abs(sx - food_x)<6 and abs(sy - food_y)<6:
                score += 1
                food_x = random.randint(20,gamescreen_width/2)
                food_y = random.randint(20,gamescreen_height/2)
                slength+=5

            gamescreen.fill(green)    
            text_gamescreen("score:"+str(score*10),black,15,15)
            
            head = []
            head.append(sx)
            head.append(sy)
            slist.append(head) 
            
            if len(slist)>slength:
                del slist[0]


            pygame.draw.rect(gamescreen,red,[food_x,food_y,ssize,ssize]) 

            if sx<0 or sx>gamescreen_width or sy<0 or sy>gamescreen_height:
                gameover= True 
                

            pygame.draw.rect(gamescreen,blue,[sx,sy,ssize,ssize]) 
            plots(gamescreen,blue,slist,ssize)
            
        pygame.display.update() 
        clock.tick(fps)



    pygame.QUIT
    quit()
gameloop()