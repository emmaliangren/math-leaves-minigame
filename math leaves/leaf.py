import pygame
import random 

class Leaf(pygame.sprite.Sprite):
    # a falling leaf with an arithemetic equation written on it
    def __init__(self, x=0, y=0, num1=0, num2=0, ans=0, speed=1):
        super().__init__()

        # 3 different leaves, randomly select one to display
        self.images = [pygame.image.load("math leaves/images/leaf1.png"),pygame.image.load("math leaves/images/leaf2.png"),pygame.image.load("math leaves/images/leaf3.png")]
        self.image = self.images[random.randint(0,2)]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed
        self.sound = pygame.mixer.Sound("math leaves/audio/leaf crunch.mp3")
        self.ans = ans

    def update(self):
        self.rect.y += self.speed 