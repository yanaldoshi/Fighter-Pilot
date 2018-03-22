import random
import pygame
import serial


class Plane(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
	self.ser=serial.Serial('/dev/ttyACM0',baudrate=9600)
        self.image=pygame.image.load('Plane.png')
        self.image.convert_alpha()
        self.rect=self.image.get_rect()

    def readJoystick(self):
	try:
		temp=self.ser.readline()
		temp=temp.strip('\n')
		temp=temp.strip('\r')
		pos=map(int,temp.split())
		return pos
	except ValueError:
		return (self.rect.centerx,self.rect.centery)
			

    def update(self):
        self.rect.centerx=self.readJoystick()[0]
	#print self.rect.centerx
        self.rect.centery=self.readJoystick()[1]

class Island(pygame.sprite.Sprite):

    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Island.png')
        self.image.convert_alpha()
        self.rect=self.image.get_rect()
        self.dy=3
        self.screen=screen
        self.rect.top=0
        self.rect.centerx=random.randrange(48,self.screen.get_width()-48)

    def update(self):
        self.rect.centery+=self.dy
        if self.rect.centery>=self.screen.get_height():
            self.reset()

    def reset(self):
        self.rect.top=0
        self.rect.centerx=random.randrange(48,self.screen.get_width()-48)

class Cloud(pygame.sprite.Sprite):

    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.image=pygame.image.load('Cloud.png')
        self.image.convert_alpha()
        self.rect=self.image.get_rect()
        self.dx=random.randrange(-1,2)
        self.dy=random.randrange(2,5)
        self.rect.bottom=0
        self.rect.centerx=random.randrange(self.image.get_width(),640-self.image.get_width())

    def update(self):
        self.rect.centerx+=self.dx
        self.rect.centery+=self.dy
        if self.rect.centery>=self.screen.get_height():
            self.reset()

    def reset(self):
        self.rect.bottom=0
        self.rect.centerx=random.randrange(self.image.get_width(),640-self.image.get_width())
        self.dx=random.randrange(-1,2)
        self.dy=random.randrange(2,5)
        
class Ocean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('ocean1.png')
        self.image.convert()
        self.rect=self.image.get_rect()
        self.dy=4
        self.reset()

    def update(self):
        self.rect.bottom+=self.dy
        if self.rect.top>=0:
            self.reset()
    def reset(self):
        self.rect.bottom=480
        
        
"""class Waves(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('waves.png')
        self.image.convert_alpha()
        self.rect=self.image.get_rect()
        self.dy=5
        self.rect.centerx=random.randrange(0,640)
        

    def update(self):
        self.rect.centery+=self.dy
        if self.rect.top>=480:
            self.reset()

    def reset(self):
        self.rect.bottom=0
        self.rect.centery=random.randrange(0,100)
        self.rect.centerx=random.randrange(0,640)
        
"""

class ScoreBoard(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font=pygame.font.SysFont(None,50)
        self.score=0
        self.lives=5

    def update(self):
        self.text="Score: %d     Planes Left: %d"%(self.score,self.lives)
        self.image=self.font.render(self.text,1,(255,255,255))
        self.rect=self.image.get_rect()
        
