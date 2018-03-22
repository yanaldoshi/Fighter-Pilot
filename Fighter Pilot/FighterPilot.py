import pygame
#from pygame.locals import *
from sys import exit
from Sprites import *
pygame.init()
def game():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    background=pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    plane=Plane()
    island=Island(screen)
    ocean=Ocean()
    clouds=[]
    for i in range(0,5):
        clouds.append(Cloud(screen))
    score=ScoreBoard()
    scoreboard=pygame.sprite.Group(score)
    friendlygroup=pygame.sprite.OrderedUpdates(ocean,island,plane)
    enemygroup=pygame.sprite.Group(clouds)
    #island.rect.centery=400
    #island.rect.centerx=300
    clock=pygame.time.Clock()
    pygame.mouse.set_visible(False)
    Loop=True
    while Loop:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.mouse.set_visible(True)
                pygame.quit
                exit()
        hitclouds=pygame.sprite.spritecollide(plane,enemygroup,False)
        if hitclouds:
            print "Bro u ded"
            for i in hitclouds:
                i.reset()
            score.lives-=1
            if score.lives<=0:
                print "Game Over"
                Loop=False
        if plane.rect.colliderect(island.rect):
            print "Bro u just mailed it huehuehue get it mailed it as in nailed it"
            island.reset()
            score.score+=100
        #spritegroup.clear(screen,background)
        friendlygroup.update()
        enemygroup.update()
        scoreboard.update()
        friendlygroup.draw(screen)
        enemygroup.draw(screen)
        scoreboard.draw(screen)
        pygame.display.update()
    pygame.mouse.set_visible(True)
    return score.score

def intro(score):
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    background=pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    plane=Plane()
    ocean=Ocean()
    intro_text=['Previous Score: %d'%score,
                'Welcome to Mail Pilot',
                'Use your mouse to control the plane,',
                'avoid the clouds as they can damage your plane',
                'with thunder, try to deliver as many mails as',
                'possible on the islands',
                'Click to begin or Esc to quit']
    intro_font=pygame.font.SysFont(None,30)
    spritegroup=pygame.sprite.OrderedUpdates(ocean,plane)
    intro_lines=[]
    for text in intro_text:
        intro_lines.append(intro_font.render(text,1,(255,255,255)))
    Loop=True
    clock=pygame.time.Clock()
    while Loop:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    done=True
                    Loop=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                done=False
                Loop=False
        spritegroup.clear(screen,background)
        spritegroup.update()
        spritegroup.draw(screen)
        for i in range(len(intro_lines)):
            screen.blit(intro_lines[i],(50,30*i))
        pygame.display.update()
    return done
                
def main():
    done=False
    score=0
    while not done:
        done=intro(score)
        if not done:
            score=game()

if __name__=='__main__':
    main()
