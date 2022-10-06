import pygame, time, array
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("meowCakeTest1")
hamster = pygame.image.load("hamster.png")
pygame.display.set_icon(hamster)
bg=pygame.image.load("bg.png")
bg=pygame.transform.scale(bg, (800, 600))
player = pygame.image.load("hamster.png")
player=pygame.transform.scale(player, (50, 50))
posX=375
posY=310
font=pygame.font.Font("freesansbold.ttf",32)

hitSound = pygame.mixer.Sound("hitSound.mp3")
missSound = pygame.mixer.Sound("missSound.mp3")
array.array("i")                
a = array.array("i",(0 for i in range(0,33)))


def showScore():
        score=font.render(str(scoreValue),True,(0,0,0))
        screen.blit(score, (640,100))

def testText():
        text=font.render(str(presentTicks),True,(0,0,0))
        screen.blit(text, (400,300))

scoreValue = 0

def dogBeat(n,t):
        scoreValue=0
        if presentTicks>=t and presentTicks<=t+0.5 and a[n]==0 :
                if keys[pygame.K_LEFT]:
                        scoreValue+=50
                        hitSound.play()
                        a[n]=1
                elif keys[pygame.K_RIGHT] :
                        missSound.play()
                        a[n]=1
        elif presentTicks>t+0.5 and a[n]==0:
                missSound.play()
                a[n]=1
        elif a[n]==0 and presentTicks<=t-0.5 and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                missSound.play()
        return scoreValue

def catBeat(n,t):
        scoreValue=0
        if presentTicks>=t and presentTicks<=t+0.5 and a[n]==0 :
                if keys[pygame.K_RIGHT]:
                        scoreValue+=50
                        hitSound.play()
                        a[n]=1
                elif keys[pygame.K_LEFT] :
                        missSound.play()
                        a[n]=1
        elif presentTicks>t+0.5 and a[n]==0:
                missSound.play()
                a[n]=1
        elif a[n]==0 and a[n-1]==1 and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                missSound.play()
        return scoreValue





pygame.mixer.music.load("jgbEdit.mp3")
pygame.mixer.music.play(1,0.0)
startTicks=pygame.time.get_ticks()





while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
        keys = pygame.key.get_pressed()
        presentTicks=(pygame.time.get_ticks()-startTicks)/1000
        if keys[pygame.K_LEFT]:
                posX=296
                posY=310
                
               
        if keys[pygame.K_RIGHT]:
                posX=450
                posY=310
               
                
        if keys[pygame.K_UP]:
               posX=375
               posY=224
               
               
        if keys[pygame.K_DOWN]:
                posX=375
                posY=375

                
        #For checking time

        if a[0]==0:
                scoreValue+=dogBeat(0,4.05)
        elif a[0]==1 and a[1]==0:
                scoreValue+=catBeat(1,9.00)
        elif a[1]==1 and a[2]==0:
                scoreValue+=dogBeat(2,11.00)
        elif a[2]==1 and a[3]==0:
                scoreValue+=dogBeat(3,13.50)
        elif a[3]==1 and a[4]==0:
                scoreValue+=catBeat(4,15.00)
        elif a[4]==1 and a[5]==0:
                scoreValue+=dogBeat(5,17.50)
                
                
        
                
                
                 
        
                
                        
        screen.blit(bg,(0,0))
        screen.blit(player,(posX,posY))
        showScore()
        testText()
       
        posX=375
        posY=310
        pygame.display.update()
