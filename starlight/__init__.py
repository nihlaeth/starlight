"""Start the Starlight application."""
import pygame
import anime
from pkg_resources import resource_filename, Requirement

class Starlight(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.images = []
        self.register_image("starlight/images/Sterrennacht.jpg", 400, 300, 100)
        self.register_image("starlight/images/Ster1.png", 100, 100, 99)

    def register_image(self, image, x, y, layer):
        """Create an image to keep track of."""
        resource = {"layer": layer}
        resource["image"] = pygame.image.load(resource_filename(
            Requirement.parse('starlight'), image))
        resource["anime"] = anime.Anime(resource["image"], x, y)
        self.images.append(resource)
        return resource["anime"]

    async def update(self):
        """Update objects on the screen and process events."""
        self.starry_sky.render(self.screen)
        self.star.render(self.screen)
        pygame.display.flip()
        pygame.time.wait(1000)

def start():
    """Start the application."""
    book = Starlight()
