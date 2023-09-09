import pygame

# game setup
pygame.init()
game = pygame.display.set_mode((800, 400))
font = pygame.font.Font(None, 32)
winner_text = ''

# game assets

blue_ship = pygame.image.load('blue.png')
red_ship = pygame.image.load('Red.png')
bg = pygame.image.load('bg.png')
bg_x = 0
red_x = 100
red_y = 154
red_hp = 100
blue_x = 604
blue_y = 154
blue_hp = 100
vel = 4


# OOP


class Ship:
    def __init__(self, x, y, health, ship):
        self.x = x
        self.y = y
        self.health = health
        self.ship = ship

    def redrawing(self):
        game.blit(self.ship, (self.x, self.y))


class Projectile:
    def __init__(self, x, y, color, vel):
        self.x = x
        self.y = y
        self.color = color
        self.vel = vel

    def draw(self):
        game.blit(self.color, (self.x, self.y))

def redraw():
    red.redrawing()
    blue.redrawing()
    for redbullet in redbullets:
        redbullet.draw()
    for bluebullet in bluebullets:
        bluebullet.draw()
    game.blit(font.render(winner_text, True, (255, 255, 255)), (330, 190))
    game.blit(font.render(redhp, True, (255, 255, 255)), (0, 0))
    game.blit(font.render(bluehp, True, (255, 255, 255)), (640, 0))
    pygame.display.update()

# objects


red = Ship(red_x, red_y, red_hp, red_ship)
blue = Ship(blue_x, blue_y, blue_hp, blue_ship)

# game code

redbullets = []
bluebullets = []
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    for redbullet in redbullets:
        if redbullet.x < 800:
            redbullet.x += redbullet.vel
        else:
            redbullets.pop(redbullets.index(redbullet))

    for bluebullet in bluebullets:
        if bluebullet.x > 0:
            bluebullet.x -= bluebullet.vel
        else:
            bluebullets.pop(bluebullets.index(bluebullet))

    for redbullet in redbullets:
        if redbullet.x >= blue.x and redbullet.x <= blue.x +96 and redbullet.y >= blue.y and redbullet.y <= blue.y + 96:
            blue.health -= 3
            redbullets.pop(redbullets.index(redbullet))
    for bluebullet in bluebullets:
        if bluebullet.x >= red.x and bluebullet.x <= red.x +96 and bluebullet.y >= red.y and bluebullet.y <= red.y + 96:
            red.health -= 3
            bluebullets.pop(bluebullets.index(bluebullet))


    if blue.health <= 1:
        winner_text = 'WINNER : RED'
    if red.health <= 1:
        winner_text = 'WINNER : BLUE'

    key = pygame.key.get_pressed()

    if key[pygame.K_w] and red.y > 0:
        red.y -= vel
    if key[pygame.K_s] and red.y < 304:
        red.y += vel
    if key[pygame.K_a] and red.x > 0:
        red.x -= vel
    if key[pygame.K_d] and red.x < 304:
        red.x += vel
    if key[pygame.K_LEFT] and blue.x > 400:
        blue.x -= vel
    if key[pygame.K_RIGHT] and blue.x < 704:
        blue.x += vel
    if key[pygame.K_UP] and blue.y > 0:
        blue.y -= vel
    if key[pygame.K_DOWN] and blue.y < 304:
        blue.y += vel
    if key[pygame.K_x] and len(redbullets) < 1:
        redbullets.append(Projectile(red.x + 96, red.y + 38, pygame.image.load('redbullet.png'), 20))
    if key[pygame.K_SPACE] and len(bluebullets) < 1:
        bluebullets.append(Projectile(blue.x - 15, blue.y + 38, pygame.image.load('bluebullet.png'), 20))

    bg_x -= 1
    bg1_x = bg_x + 1200
    if bg_x <= -1200:
        bg_x = 0

    game.blit(bg, (bg_x, 0))
    game.blit(bg, (bg1_x, 0))

    redhp = 'RED HP : ' + str(red.health)
    bluehp = 'BLUE HP : ' + str(blue.health)

    redraw()

pygame.quit()