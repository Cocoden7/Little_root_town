import time

import pygame
import random

# TODO: tout ce qui est load et scale, je peux utiliser des fonctions en fait


def get_text_surf(font, text):
    return font.render(text, False, (0, 0, 0))


class ProcessImage:
    def __init__(self, grow_factor, init_size=(26.25, 37.5)):
        self.grow_factor = grow_factor
        self.init_size = init_size

    def load_image(self, path, filename):
        return pygame.image.load(path + filename + ".png")

    def scale_image(self, image):
        return pygame.transform.scale(image, (self.init_size[0] * self.grow_factor, self.init_size[1] * self.grow_factor))

    def load_and_scale_image(self, path, filename):
        return self.scale_image(self.load_image(path, filename))

    def load_images(self, path, filenames):
        return [self.load_image(path, f) for f in filenames]

    def scale_images(self, images):
        return [self.scale_image(img) for img in images]

    def load_and_scale_images(self, path, filenames):
        return self.scale_images(self.load_images(path, filenames))


def get_filenames_anim_tiles(tilename, n_images_animation):
    return [tilename + str(i) for i in range(1, 1 + n_images_animation)]


class AnimatedCharacter:
    def __init__(self, imgs, n_left):

        self.anim_imgs_dic = {"down": imgs[0:2],
                              "up": imgs[2:4],
                              "left": imgs[4:4+n_left],
                              "idle": {"down": imgs[-3], "up": imgs[-2], "left": imgs[-1]}}
        self.anim_imgs_dic["right"] = [pygame.transform.flip(e, True, False) for e in self.anim_imgs_dic["left"]]  # Flipping left tiles for right animation

        self.anim_imgs_dic["idle"]["right"] = pygame.transform.flip(imgs[-1], True, False)  # Left idle



class Animated:
    def __init__(self, anim_images, pos=(0, 0)):
        self.anim_images = anim_images
        self.img = anim_images[0]
        self.rect = self.img.get_rect()
        self.rect.topleft = pos
        self.anim_counter = 0
        self.anim_speed = 0.04

    def update(self):
        self.anim_counter += self.anim_speed
        self.img = self.anim_images[int(self.anim_counter) % len(self.anim_images)]

    def draw(self, screen):
        screen.blit(self.img, self.rect.topleft)

