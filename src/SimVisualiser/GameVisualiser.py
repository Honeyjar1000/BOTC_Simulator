from src.Player.Player import Player
from src.StoryTeller.StoryTeller import StoryTeller
import pygame
import math
from src.SimVisualiser.RoleDict import RoleImgDict

# Constants
WIDTH, HEIGHT = 1200 // 1.5, 1200 // 1.5  # Adjusted window size
RADIUS = 240  # Radius for spacing between players
MAIN_ROOM_WIDTH = 600  # Main room width (square)

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
FLOOR_COL = (68, 6, 102)
OUTLINE_COLOR = (0, 0, 0)  # Black color for the outline


# Player class
class PlayerEntity:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def update_position(self, index, num_players, room_center):
        """ Update player's position based on the number of players and room center """
        angle = 2 * math.pi * index / num_players  # Correct angle calculation
        self.x = room_center[0] + RADIUS * math.cos(angle)
        self.y = room_center[1] + RADIUS * math.sin(angle)


class GameVisualiser:
    def __init__(self, players: dict, story_teller: StoryTeller):
        self.players = players
        self.story_teller = story_teller

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Circular Entities Simulation")

        self.story_teller_image = pygame.image.load('src/SimVisualiser/RoleImg/IMGStoryTeller.png')
        self.story_teller_image = self.create_circular_image(self.story_teller_image)
        self.story_teller_image = pygame.transform.scale(self.story_teller_image, (120, 120))

        self.player_vis_entity = []
        for i, key in enumerate(self.players):
            player_character_image = pygame.image.load(RoleImgDict[type(self.players[key].character)])
            player_character_image = self.create_circular_image(player_character_image)
            player_character_image = pygame.transform.scale(player_character_image, (90, 90))
            
            self.player_vis_entity.append([PlayerEntity(self.players[key].player_name), self.players[key], player_character_image])


    def create_circular_image(self, image, outline_thickness=8):
        # Create a surface with the same size as the image
        mask_surface = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA)
        # Draw the outline (black circle) with specified thickness
        pygame.draw.circle(mask_surface, OUTLINE_COLOR, 
                        (image.get_width() // 2, image.get_height() // 2), 
                        image.get_width() // 2, outline_thickness)  # Thicker outline
        # Draw the filled white circle for masking the player image (inside the outline)
        pygame.draw.circle(mask_surface, WHITE, 
                        (image.get_width() // 2, image.get_height() // 2), 
                        image.get_width() // 2)
        # Copy the image to the mask surface, applying the circular mask
        mask_surface.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
        return mask_surface

    def initialize_display(self):
        self.screen.fill(BLACK)
        self.main_room = pygame.Rect((WIDTH - MAIN_ROOM_WIDTH) // 2, (HEIGHT - MAIN_ROOM_WIDTH) // 2, MAIN_ROOM_WIDTH, MAIN_ROOM_WIDTH)
        self.ROOM_CENTER = (self.main_room.x + self.main_room.width // 2, self.main_room.y + self.main_room.height // 2)
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)


    def update_display(self):
        pygame.draw.rect(self.screen, FLOOR_COL, self.main_room)
        self.screen.blit(self.story_teller_image, (self.ROOM_CENTER[0] - 35, self.ROOM_CENTER[1] - 35))
        
        for i in range(len(self.player_vis_entity)):
            self.player_vis_entity[i][0].update_position(i, len(self.player_vis_entity), self.ROOM_CENTER)
            player_x, player_y = self.player_vis_entity[i][0].x, self.player_vis_entity[i][0].y
            player_img = self.player_vis_entity[i][2]
            img_width, img_height = player_img.get_width(), player_img.get_height()
            
            pygame.draw.circle(self.screen, BLACK, (player_x, player_y), img_width // 2 + 3, 3)
            self.screen.blit(player_img, (player_x - img_width // 2, player_y - img_height // 2))
            
            player_name_text = self.font.render(self.player_vis_entity[i][1].player_name, True, BLACK)
            text_x, text_y = player_x - player_name_text.get_width() // 2, player_y - player_name_text.get_height() // 2
            self.screen.blit(player_name_text, (text_x, text_y))

        pygame.display.flip()
