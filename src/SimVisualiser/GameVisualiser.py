from src.Player.Player import Player
from src.StoryTeller.StoryTeller import StoryTeller
import pygame
import math
from src.SimVisualiser.RoleDict import RoleImgDict, RED_HERRING, IS_POISONED, BUTLER_PICKED, WASHER_WOMAN_CORRECT, WASHER_WOMAN_WRONG, LIBRARIAN_CORRECT, LIBRARIAN_WRONG, INVESTIGATOR_CORRECT, INVESTIGATOR_WRONG, MONK_PROTECTS


# Constants
WIDTH, HEIGHT = 1200 // 1.5, 1200 // 1.5
RADIUS = 240
MAIN_ROOM_WIDTH = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
FLOOR_COL = (68, 6, 102)
OUTLINE_COLOR = (0, 0, 0)



class PlayerEntity:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def update_position(self, index, num_players, room_center):
        angle = 2 * math.pi * index / num_players
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
        self.story_teller_image = pygame.transform.scale(self.story_teller_image, (120, 120))
        self.story_teller_image = self.create_circular_image(self.story_teller_image)

        self.red_herring_image = pygame.image.load(RED_HERRING)
        self.red_herring_image = self.create_circular_image(self.red_herring_image)
        self.red_herring_image = pygame.transform.scale(self.red_herring_image, (50, 50))

        self.is_poisoned_image = pygame.image.load(IS_POISONED)
        self.is_poisoned_image = self.create_circular_image(self.is_poisoned_image)
        self.is_poisoned_image = pygame.transform.scale(self.is_poisoned_image, (50, 50))

        self.butler_picked_image = pygame.image.load(BUTLER_PICKED)
        self.butler_picked_image = self.create_circular_image(self.butler_picked_image)
        self.butler_picked_image = pygame.transform.scale(self.butler_picked_image, (50, 50))

        self.washer_woman_info_correct = pygame.image.load(WASHER_WOMAN_CORRECT)
        self.washer_woman_info_correct = self.create_circular_image(self.washer_woman_info_correct)
        self.washer_woman_info_correct = pygame.transform.scale(self.washer_woman_info_correct, (50, 50))

        self.washer_woman_info_wrong = pygame.image.load(WASHER_WOMAN_WRONG)
        self.washer_woman_info_wrong = self.create_circular_image(self.washer_woman_info_wrong)
        self.washer_woman_info_wrong = pygame.transform.scale(self.washer_woman_info_wrong, (50, 50))

        self.librarian_info_correct = pygame.image.load(LIBRARIAN_CORRECT)
        self.librarian_info_correct = self.create_circular_image(self.librarian_info_correct)
        self.librarian_info_correct = pygame.transform.scale(self.librarian_info_correct, (50, 50))

        self.librarian_info_wrong = pygame.image.load(LIBRARIAN_WRONG)
        self.librarian_info_wrong = self.create_circular_image(self.librarian_info_wrong)
        self.librarian_info_wrong = pygame.transform.scale(self.librarian_info_wrong, (50, 50))

        self.investigator_info_correct = pygame.image.load(INVESTIGATOR_CORRECT)
        self.investigator_info_correct = self.create_circular_image(self.investigator_info_correct)
        self.investigator_info_correct = pygame.transform.scale(self.investigator_info_correct, (50, 50))

        self.investigator_info_wrong = pygame.image.load(INVESTIGATOR_WRONG)
        self.investigator_info_wrong = self.create_circular_image(self.investigator_info_wrong)
        self.investigator_info_wrong = pygame.transform.scale(self.investigator_info_wrong, (50, 50))

        self.monk_protects = pygame.image.load(MONK_PROTECTS)
        self.monk_protects = self.create_circular_image(self.monk_protects)
        self.monk_protects = pygame.transform.scale(self.monk_protects, (50, 50))



        self.player_vis_entity = []
        for i, key in enumerate(self.players):
            player_character_image = pygame.image.load(RoleImgDict[type(self.players[key].character)])
            player_character_image = self.create_circular_image(player_character_image)
            player_character_image = pygame.transform.scale(player_character_image, (90, 90))
            self.player_vis_entity.append([PlayerEntity(self.players[key].player_name), self.players[key], player_character_image])

    def darken_image(self, image, amount=100):
        """Darkens only the circular part of an image with proper alpha blending."""
        darkened = image.copy()
        radius = image.get_width() // 2
        center = (radius, radius)

        # Create a transparent overlay with a circular semi-transparent black region
        overlay = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA)
        pygame.draw.circle(overlay, (0, 0, 0, amount), center, radius)

        # Standard alpha blending
        darkened.blit(overlay, (0, 0))  # ← no special_flags here
        return darkened


    def create_circular_image(self, image, outline_thickness=20):
        mask_surface = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA)
        pygame.draw.circle(mask_surface, OUTLINE_COLOR,
                           (image.get_width() // 2, image.get_height() // 2),
                           image.get_width() // 2, outline_thickness)
        pygame.draw.circle(mask_surface, WHITE,
                           (image.get_width() // 2, image.get_height() // 2),
                           image.get_width() // 2)
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
        img_w, img_h = self.story_teller_image.get_size()
        
        # Correction offset to visually center the storyteller image
        offset_x, offset_y = -4, 0

        # Adjusted center for drawing outline
        adjusted_center = (self.ROOM_CENTER[0] + offset_x, self.ROOM_CENTER[1] + offset_y)

        # Draw circular black outline at the adjusted center
        pygame.draw.circle(self.screen, BLACK, adjusted_center, img_w // 2 + 3)

        # Blit the storyteller image with the same offset
        self.screen.blit(self.story_teller_image,
            (self.ROOM_CENTER[0] - img_w // 2 + offset_x,
            self.ROOM_CENTER[1] - img_h // 2 + offset_y))
        
        for i in range(len(self.player_vis_entity)):
            self.player_vis_entity[i][0].update_position(i, len(self.player_vis_entity), self.ROOM_CENTER)
            player_x, player_y = self.player_vis_entity[i][0].x, self.player_vis_entity[i][0].y
            original_img = self.player_vis_entity[i][2]
            player_obj = self.player_vis_entity[i][1]
            player_img = self.darken_image(original_img) if not player_obj.alive else original_img

            img_width, img_height = player_img.get_width(), player_img.get_height()

            pygame.draw.circle(self.screen, BLACK, (player_x, player_y), img_width // 2 + 3, 3)
            self.screen.blit(player_img, (player_x - img_width // 2, player_y - img_height // 2))

            player_name_text = self.font.render(self.player_vis_entity[i][1].player_name, True, BLACK)
            text_x, text_y = player_x - player_name_text.get_width() // 2, player_y - player_name_text.get_height() // 2
            self.screen.blit(player_name_text, (text_x, text_y))

        def place_token(image, player_entity, stack_index, spacing=50):
            dx = self.ROOM_CENTER[0] - player_entity.x
            dy = self.ROOM_CENTER[1] - player_entity.y
            distance = math.hypot(dx, dy)

            direction = (0, 0) if distance == 0 else (dx / distance, dy / distance)
            token_distance = 65 + stack_index * spacing

            token_x = player_entity.x + direction[0] * token_distance
            token_y = player_entity.y + direction[1] * token_distance

            # Draw black outline behind the token (radius = 25 + 4 for outline)
            pygame.draw.circle(self.screen, BLACK, (int(token_x), int(token_y)), 29)
            self.screen.blit(image, (token_x - 25, token_y - 25))


        red_herring_player = self.story_teller.black_board.grimoir.data.data.get("red_herring")
        poisoned_player = self.story_teller.black_board.grimoir.data.data.get("poisoner_hits")
        butler_picked_player = self.story_teller.black_board.grimoir.data.data.get("butler_picks")
        washer_woman_correct_player = self.story_teller.black_board.grimoir.data.data.get("washer_woman_info_correct")
        washer_woman_wrong_player = self.story_teller.black_board.grimoir.data.data.get("washer_woman_info_wrong")
        librarian_correct_player = self.story_teller.black_board.grimoir.data.data.get("librarian_info_correct")
        librarian_wrong_player = self.story_teller.black_board.grimoir.data.data.get("librarian_info_wrong")
        investigator_correct_player = self.story_teller.black_board.grimoir.data.data.get("investigator_info_correct")
        investigator_wrong_player = self.story_teller.black_board.grimoir.data.data.get("investigator_info_wrong")
        monk_protects_player = self.story_teller.black_board.grimoir.data.data.get("monk_protects")



        red_herring_entity = next((p[0] for p in self.player_vis_entity if p[1] == red_herring_player), None)
        poisoned_entity = next((p[0] for p in self.player_vis_entity if p[1] == poisoned_player), None)
        butler_picked_entity = next((p[0] for p in self.player_vis_entity if p[1] == butler_picked_player), None)
        washer_woman_correct_entity = next((p[0] for p in self.player_vis_entity if p[1] == washer_woman_correct_player), None)
        washer_woman_wrong_entity = next((p[0] for p in self.player_vis_entity if p[1] == washer_woman_wrong_player), None)
        librarian_correct_entity = next((p[0] for p in self.player_vis_entity if p[1] == librarian_correct_player), None)
        librarian_wrong_entity = next((p[0] for p in self.player_vis_entity if p[1] == librarian_wrong_player), None)
        investigator_correct_entity = next((p[0] for p in self.player_vis_entity if p[1] == investigator_correct_player), None)
        investigator_wrong_entity = next((p[0] for p in self.player_vis_entity if p[1] == investigator_wrong_player), None)
        monk_protects_entity = next((p[0] for p in self.player_vis_entity if p[1] == monk_protects_player), None)


        token_map = [
            (red_herring_entity, self.red_herring_image),
            (poisoned_entity, self.is_poisoned_image),
            (butler_picked_entity, self.butler_picked_image),
            (washer_woman_correct_entity, self.washer_woman_info_correct),
            (washer_woman_wrong_entity, self.washer_woman_info_wrong),
            (librarian_correct_entity, self.librarian_info_correct),
            (librarian_wrong_entity, self.librarian_info_wrong),
            (investigator_correct_entity, self.investigator_info_correct),
            (investigator_wrong_entity, self.investigator_info_wrong),
            (monk_protects_entity, self.monk_protects)
        ]


        entity_to_tokens = {}
        for entity, token_img in token_map:
            if entity:
                entity_to_tokens.setdefault(entity, []).append(token_img)

        for entity, tokens in entity_to_tokens.items():
            for i, token_img in enumerate(tokens):
                place_token(token_img, entity, stack_index=i)

        pygame.display.flip()
