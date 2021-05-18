import pygame
from models import Fighter

pygame.init()

clock = pygame.time.Clock()
fps = 60

font = pygame.font.SysFont('Times New Roman', 26)
red = (255, 0, 0)
green = (0, 255, 0)

# game window
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle RPG')

# images

# background
back_img = pygame.image.load('img/back_m.png').convert_alpha()
back_img = pygame.transform.scale(back_img, (screen_width, screen_height))


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def draw_bg():
    # show background
    screen.blit(back_img, (0, 0))
    # show player stats
    draw_text(f'{player.name} HP: {player.hp}', font, red, 30, 10)
    for i, count in enumerate(bandits):
        draw_text(f'{count.name} HP: {count.hp}', font, red, screen_width - 200, 10 + i * 30)


player = Fighter(200, 300, 'player2', 30, 10, 3, screen, 0)
player2 = Fighter(550, 300, 'player2', 30, 10, 3, screen, 0)
player3 = Fighter(600, 300, 'player2', 30, 10, 3, screen, 0)
bandits = []
bandits.append(player2)
bandits.append(player3)

run = True
while run:

    clock.tick(fps)

    # draw background
    draw_bg()

    # draw players
    player.update()
    player.draw()
    for bandit in bandits:
        bandit.update()
        bandit.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
