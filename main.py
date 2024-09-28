import pygame
import random
import math
s_wd=800
s_ht=500
pl_x=370
pl_y=380
en_y_min=50
en_y_max=150
en_sp_x=4
en_sp_y=40
bu_sp=10
collision_distance = 30

#to initialise the game
pygame.init()

#to create the screen for the game
screen=pygame.display.set_mode((s_wd,s_ht))
bg=pygame.image.load("backgrund.jpg")
pl_img=pygame.image.load("us.png")
pl_x_change=0
en_img=[]
en_y=[]
en_x=[]
en_x_change=[]
en_y_change=[]
enemies=6
for i in range(enemies):
    en_img.append(pygame.image.load("enime.png"))
    en_x.append(random.randint(0,s_wd-64))
    en_y.append(random.randint(en_y_min,en_y_min))
    en_x_change.append(en_sp_x)
    en_y_change.append(en_sp_y)

bu_img=pygame.image.load("bulet.png")
screen=pygame.display.set_mode((s_wd,s_ht))
bu_x=0
bu_x_change=0
bu_y=pl_y
bu_y_change=bu_sp
bu_st="ready"

#score text
score=0
score_font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10

#gameover font
end_font=pygame.font.Font('freesansbold.ttf',64)


#to display the score on the screen
#screen.blit(what to display, where to display)
def show_score(x,y):
    score_text = score_font.render("Score: "+str(score),True,"white")
    screen.blit(score_text,(x,y))

#to display the gameover text in the screen
def show_gameover():
    gameover_text=end_font.render("gameover",True,"white")
    screen.blit(gameover_text,(400,400))

#display the player on the screen
def player(x,y):
    screen.blit(pl_img,(x,y))

#show the enemies on the screen   
def enimes(x,y,i):
    screen.blit(en_img[i],(x,y))

#to fire the bullet from the player's position'
def fire_bullet(x,y):
    bu_st="fire"
    screen.blit(bu_img,(x+15,y+10))

#to check the collision between the bullet and the enemy
def check_coli(en_x,en_y,bu_x,bu_y):
    distance=math.sqrt((en_x-bu_x)**2+(en_y-bu_y)**2)
    return distance<collision_distance
while True:
    screen.fill("black")
    screen.blit(bg,(0,0))
    
    #to get all the events in pygame
    for event in pygame.event.get():
        #to check if the event type is QUIT (to close the window)
        if event.type==pygame.QUIT:
            #to quit the game
            pygame.quit() 
        
        #if the event type is KEYDOWN (to press any button)
        if event.type==pygame.KEYDOWN:
            #if left arrow button is pressed, move the player to left
            if event.key==pygame.K_LEFT:
                pl_x_change-=5   
            if event.key==pygame.K_RIGHT:
                pl_x_change+=5
            if event.key==pygame.K_SPACE and bu_st=="ready":
                bu_x=pl_x+225
                for i in range(25):
                    bu_y=-2

                fire_bullet(bu_x,bu_y)
                
        #if the button is released
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            pl_x_change = 0
        
        #player movement
        pl_x = pl_x + pl_x_change
        pl_x = max(0,min(pl_x,s_wd-50))

        #enemy movement
        for i in range(enemies):
            if en_x[i]>350:
                for j in range(enemies):
                    en_y[i]=2000
                show_gameover()
                break
            
            en_x[i] = en_x[i] + en_x_change[i] 

            if en_x[i]<=0 or en_x_change[i] >= s_wd-64:

                en_x_change[i] = en_x_change[i]*-1
            
                en_y[i] = en_y[i] + en_y_change[i] 
            
            if check_coli(en_x[i],en_y[i],bu_x,bu_y):
                bu_y=pl_y
                bu_st="ready"
                score = score+1
                en_x[i] = random.randint(0,s_wd-50)
                en_y[i] = random.randint(en_y_min,en_y_max)
            enimes(en_x[i],en_y[i],i)
        
        #bullet movement
        if bu_y<=0:
            bu_y=pl_y
            bu_st="ready"
        elif bu_st=="fire":
            fire_bullet(bu_x,bu_y)
            bu_y = bu_y - bu_y_change


        player(pl_x,pl_y)     
        show_score(textx,texty)
        pygame.display.update()


        
        