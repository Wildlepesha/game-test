import pygame


class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions, screen, action):
        self.screen = screen
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.action = action
        if self.action == 0:
            for i in range(4):
                img = pygame.image.load(f'img/{self.name}/idle/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
                self.animation_list.append(img)
        elif self.action == 1:
            y -= 60
            for i in range(9):
                img = pygame.image.load(f'img/{self.name}/attack/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
                self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 150
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)