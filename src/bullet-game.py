import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

p_pos = pygame.Vector2(400, 300)
player_speed = 5

run = True
while run:

    player = pygame.Rect(int(p_pos.x), int(p_pos.y), 50, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if pygame.key.get_pressed()[pygame.K_w]:
        p_pos.y -= player_speed
    if pygame.key.get_pressed()[pygame.K_s]:
        p_pos.y += player_speed
    if pygame.key.get_pressed()[pygame.K_d]:
        p_pos.x += player_speed
    if pygame.key.get_pressed()[pygame.K_a]:
        p_pos.x -= player_speed
    #place this movement system into a class method
        
    screen.fill('blue')
    pygame.draw.rect(screen, 'red', player)
    pygame.display.update()
    clock.tick(60)

pygame.quit()