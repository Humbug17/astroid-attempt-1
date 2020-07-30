import pygame

class Ship(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('ship.png')
    self.image = pygame.transform.smoothscale(self.image, (80, 80))
    self.rect = self.image.get_rect()
    self.rect.center = (0, 300)
    self.image = pygame.transform.rotate(self.image, 270)
    self.speed = pygame.math.Vector2(10, 0)

  def update(self):
    self.rect.move_ip(self.speed)