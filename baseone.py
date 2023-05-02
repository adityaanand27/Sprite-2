import pygame
import time
import math
def scale_image(img,factor):
    size = round(img.get_width() *factor),round(img.get_height()*factor)
    return pygame.transform.scale(img,size)
road=pygame.image.load("road.png")
grass= scale_image(pygame.image.load("grass.png"),0.45)
bike= pygame.image.load("bike.png")
car= pygame.image.load("car.png")
str= pygame.image.load("newstr.png")
ca= pygame.image.load("car.png")


width,height = 1000,580
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Traffic Simulation")
fps = 60
class Abscar:
    def __init__(self,x,y):
        # self.max_vel=max_vel
        # self.val=2
    #     self.rotation_vel=rotation_vel
    #     self.angle=0
    # def rotate(self,left=False,right=False):
    #     if left:
    #         self.angle += self.rotation_vel
    #     elif right:
    #         self.angle-=self.rotation_vel
   
        self.image = pygame.image.load('car.png')
        self.rect = self.image.get_rect()

        self.rect.x=0
        self.rect.y=300
   

run=True
clock = pygame.time.Clock()
while run:
    clock.tick(fps)
    pygame.display.flip()
    screen.blit(road,(0,70))
    screen.blit(road,(200,70))
    screen.blit(road,(400,70))
    screen.blit(road,(600,70))
    screen.blit(grass,(0,0))
    screen.blit(grass,(150,0))
    screen.blit(grass,(300,0))
    screen.blit(grass,(400,0))
    screen.blit(grass,(500,0))
    screen.blit(grass,(600,0))
    screen.blit(grass,(700,0))
    screen.blit(grass,(830,0))
    screen.blit(grass,(830,0))
    screen.blit(grass,(830,400))
    screen.blit(grass,(700,400))
    screen.blit(grass,(600,400))
    screen.blit(grass,(500,400))
    screen.blit(grass,(400,400))
    screen.blit(grass,(300,400))
    screen.blit(grass,(150,400))
    screen.blit(grass,(0,400))
    screen.blit(str,(20,80))
    screen.blit(str,(270,80))
    screen.blit(str,(520,80))
    screen.blit(str,(770,80))
    screen.blit(car,(0,300))
    car_position = [0, 300]  # starting position of the car
# cn=0
while run:
   
    car_position[0] += 5
    
    screen.blit(car, car_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.QUIT()