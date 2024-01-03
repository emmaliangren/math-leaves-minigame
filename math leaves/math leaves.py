import random
import pygame
import leaf as l
pygame.init()

# game variables
spawnRate = 3000
lastSpawn = 0
operation = ["+","x","÷","-"]
lim = 15
score = 0
userIn = "0"
lastReset = 0
resetRate = 500

# game objects & visual elements
background = pygame.image.load("images/math leaves bg.png")
background_rect = background.get_rect()

startButton = pygame.image.load("images/start!.png")
startButton_rect = startButton.get_rect()

infoButton = pygame.image.load("images/info button graphic.png")
infoButton_rect = infoButton.get_rect()
infoButton = pygame.transform.scale(infoButton,((infoButton_rect.width)//2.3,(infoButton_rect.height)//2.3))
infoButton_rect = infoButton.get_rect()

instruct = pygame.image.load("images/instructions page.png")
instruct_rect = instruct.get_rect()

exitButton = pygame.image.load("images/exit button.png")
exitButton_rect = exitButton.get_rect()
exitButton = pygame.transform.scale(exitButton,((exitButton_rect.width)//3.5,(exitButton_rect.height)//3.5))
exitButton_rect = exitButton.get_rect()

cloud1 = pygame.image.load("images/cloud1.png")
cloud1_rect = cloud1.get_rect()
cloud1 = pygame.transform.scale(cloud1, ((cloud1_rect.width)//5, (cloud1_rect.height)//5))
cloud1_rect = cloud1.get_rect()

cloud2 = pygame.image.load("images/cloud2.png")
cloud2_rect = cloud2.get_rect()
cloud2 = pygame.transform.scale(cloud2, ((cloud2_rect.width)//4, (cloud2_rect.height)//4))
cloud2_rect=cloud2.get_rect()

font = pygame.freetype.Font("fonts/Poppins-Medium.ttf")
title, title_rect = font.render("Math Leaves", "papayawhip", size=80)
scoreLabel, scoreLabel_rect = font.render("Score: "+str(score), "seashell", size=50)
gameover, gameover_rect = font.render("Game Over", (212, 24, 24), size=75)

leaves = pygame.image.load("images/leaf pile.png")
leaves_rect = leaves.get_rect()
leaves = pygame.transform.scale(leaves, ((leaves_rect.width)//1.5, (leaves_rect.height)//1.5))
leaves_rect = leaves.get_rect()

endBKG = pygame.image.load("images/end screen.png")
endBKG_rect = endBKG.get_rect()

restart = pygame.image.load("images/restart button.png")
restart_rect = restart.get_rect()

# audio objects
pygame.mixer.music.load("audio/start screen music.mp3")
pygame.mixer.music.set_volume(0.65) # lower volume of music
pygame.mixer.music.play(-1)

# surface initialization
surf_width, surf_height = 600,750
surface = pygame.display.set_mode((surf_width,surf_height))
pygame.display.set_caption("math leaves game")

# clock for determining spawning of leaves
FPS = 64
clock = pygame.time.Clock()

leaf_group = pygame.sprite.Group()

# display loop
running = True
startScreen = True
alive = False
endScreen = False
infoScreen = False

# display variables
scroll = 0
startW = (surf_width-startButton_rect.width)//2
startH = (surf_height-startButton_rect.height+title_rect.height)//2 + 50
infoW = surf_width-infoButton_rect.width-25
infoH = 25
exitW = surf_width-exitButton_rect.width-5
exitH = 5
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                userIn+="0"
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                userIn+="1"
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                userIn+="2"
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                userIn+="3"
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                userIn+="4"
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                userIn+="5"
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                userIn+="6"
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                userIn+="7"
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                userIn+="8"
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                userIn+="9"
            if event.key == pygame.K_DELETE:
                userIn=userIn.rstrip(userIn[-1])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if startButton_rect.collidepoint(pos): 
                    # if the start button is clicked, start game, stop start screen
                    alive = True
                    startScreen = False
                    # unload start screen music, start game music
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("audio/bg music.mp3")
                    pygame.mixer.music.play(-1)
                if infoButton_rect.collidepoint(pos):
                    # stop start screen, start info screen
                    infoScreen = True
                    startScreen = False
                if exitButton_rect.collidepoint(pos):
                    # stop info screen, restart start screen
                    startScreen = True
                    infoScreen = False
                if restart_rect.collidepoint(pos):
                    # stop end screen, restart game
                    alive = True
                    endScreen = False
                    score = 0
                    scoreLabel, scoreLabel_rect = font.render("Score: "+str(score), "seashell", size=50)
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("audio/bg music.mp3")
                    pygame.mixer.music.play(-1)
                    

    if startScreen: # start screen display
        # scrolling screen
        surface.blit(background,(0,scroll))
        surface.blit(background,(0,scroll-surf_height))
        # display text
        pygame.draw.rect(surface,"darkorange",((surf_width-title_rect.width-25)//2,(surf_height-title_rect.height-175)//2,title_rect.width+25,title_rect.height+25))
        surface.blit(title,((surf_width-title_rect.width)//2,(surf_height-title_rect.height-150)//2))
        # start button blit
        surface.blit(startButton,(startW,startH))
        # update start button rect
        startButton_rect.x = startW
        startButton_rect.y = startH
        # info button blit
        surface.blit(infoButton,(infoW,infoH))
        # update info button rect
        infoButton_rect.x = infoW
        infoButton_rect.y = infoH
        scroll+=0.5
    
        if scroll>surf_height: # if the bottom background image is out of view, reset to scroll to 0
            scroll=0
    
    if infoScreen:
        surface.blit(instruct,(0,0))
        # exit button blit
        surface.blit(exitButton,(exitW,exitH))
        # update exit button rect
        exitButton_rect.x = exitW
        exitButton_rect.y = exitH

    if alive:
        #deciding the numbers and operation for each leaf 
        opNum = random.randint(0,3)
        if opNum==0: # addition case
            num1 = random.randint(1,lim)
            num2 = random.randint(1,lim)
            ans = num1+num2
        elif opNum==1: # multiplication case
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            ans = num1*num2
        elif opNum==2: # division case
            num2 = random.randint(1,10) #divisor
            ans = random.randint(1,10)
            num1 = num2 * ans # will always be the bigger num, this is the dividend
        else: # subtraction case
            num1 = random.randint(1,20)
            num2 = random.randint(1,20)
            ans = num1-num2
        text, text_rect = font.render(str(num1)+f" {operation[opNum]} "+str(num2), "white", size=23)

        # spawn leaves
        time = pygame.time.get_ticks()
        if time - lastSpawn > spawnRate:
            lastSpawn = time
            leaf = l.Leaf(0,0,num1,num2,ans,0.5)
            leaf.rect.y = 0
            leaf.rect.x = random.randint(0,surf_width-leaf.rect.width)
            leaf_group.add(leaf)
            
            # blitting equation onto center of leaf
            if leaf.image==leaf.images[0]:
                (leaf.image).blit(text,((leaf.rect.width)//2-22,(leaf.rect.height)//2-10))
            elif leaf.image==leaf.images[1]:
                (leaf.image).blit(text,((leaf.rect.width)//2-28,(leaf.rect.height)//2-10))
            else:
                (leaf.image).blit(text,((leaf.rect.width)//2-22,(leaf.rect.height)//2))
        
        # if user correctly inputs answer of leaf, remove leaf
        for leaf in leaf_group:
            if int(userIn)==leaf.ans:
                leaf_group.remove(leaf)
                score+=1
                userIn="0"
                scoreLabel, scoreLabel_rect = font.render("Score: "+str(score), "seashell", size=50)

        # slightly delay resetting of user input to allow for double digit input
        timeReset = pygame.time.get_ticks()
        if timeReset - lastReset > resetRate:
            lastReset=timeReset
            userIn="0"

        # background and bottom of display
        surface.fill("aliceblue")
        surface.blit(cloud2,(surf_width-cloud2_rect.width-25,50))
        surface.blit(cloud2,(10,150))
        surface.blit(cloud1,(60,-5))
        surface.blit(leaves,(0,surf_height-leaves_rect.height+30))

        # score blit
        pygame.draw.rect(surface,"tomato",(5,surf_height-scoreLabel_rect.height-18,scoreLabel_rect.width+15,scoreLabel_rect.height+15))
        surface.blit(scoreLabel,(10,surf_height-scoreLabel_rect.height-10))

        #if leaf falls into leaf pile, game over 
        for leaf in leaf_group:
            if leaf.rect.y > surf_height - (leaves_rect.height)//2:
                leaf.sound.play()
                leaf_group.remove(leaf)

                for leaf in leaf_group:
                    leaf_group.remove(leaf)
                
                endScreen = True
                alive = False

        #update game display
        leaf_group.draw(surface)
        leaf_group.update()
    
    if endScreen:
            # end screen display, game over text and restart button blit
            surface.blit(endBKG,(0,0))
            pygame.draw.rect(surface,"orange",((surf_width-gameover_rect.width-25)//2,(surf_height-gameover_rect.height-220)//2-22,gameover_rect.width+25,gameover_rect.height+scoreLabel_rect.height+35))
            surface.blit(gameover,(((surf_width)-gameover_rect.width)//2,(surf_height-gameover_rect.height-220)//2-10))
            surface.blit(scoreLabel,(((surf_width)-scoreLabel_rect.width)//2,(surf_height-gameover_rect.height-220)//2+gameover_rect.height))
            surface.blit(restart,((surf_width-restart_rect.width)//2,450))
            # update restart button coordinates
            restart_rect.x = (surf_width-restart_rect.width)//2
            restart_rect.y = 450
            pygame.mixer.music.stop()

    pygame.display.update()

pygame.quit()