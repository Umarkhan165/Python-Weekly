import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()

# Correct loading
wood_bg = pygame.image.load(r'D:\PyGame\wood_bg.png')  
land_bg = pygame.image.load(r'D:\PyGame\land_bg.png')   
waves_bg = pygame.image.load(r'\PyGame\waves_bg.png')
cloud_bg = pygame.image.load(r'\PyGame\cloud_bg.png')
cloud2_bg = pygame.image.load(r'\PyGame\cloud2_bg.png')


wood_bg = pygame.transform.scale(wood_bg, (1280, 720))   
land_bg = pygame.transform.scale(land_bg, (1300, 160))  
cloud_bg = pygame.transform.scale(cloud_bg, (300, 300))
cloud2_bg = pygame.transform.scale(cloud2_bg, (300, 300))
cloud3_bg = pygame.transform.scale(cloud_bg, (300, 300))

land_position_y = 520
land_speed = 1

water_position_y = -70
water_speed = 1.5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            sys.exit()

    screen.blit(wood_bg, (0,0))
    land_position_y -= land_speed  

    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1

    screen.blit(land_bg, (0,land_position_y))    

    water_position_y += water_speed

    if water_position_y<=620 or water_position_y >= 680:
        water_speed *= -1
    screen.blit(waves_bg, (-100,water_position_y))
    screen.blit(cloud_bg, (10,70))
    screen.blit(cloud2_bg, (370,170))
    screen.blit(cloud3_bg, (800,100))
    pygame.display.update()
    clock.tick(120) 

