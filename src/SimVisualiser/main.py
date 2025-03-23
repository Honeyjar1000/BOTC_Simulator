import pygame
import math
from src.SimVisualiser.RoleDict import RoleImgDict

def Display(game_players):
    # Initialize pygame
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 1200 // 1.5, 1200 // 1.5  # Adjusted window size
    RADIUS = 240  # Radius for spacing between players
    MAIN_ROOM_WIDTH = 600  # Main room width (square)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (20, 20, 20)
    FLOOR_COL = (68, 6, 102)
    OUTLINE_COLOR = (0, 0, 0)  # Black color for the outline

    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Circular Entities Simulation")

    # Load images
    #player_image = pygame.image.load('src/SimVisualiser/RoleImg/IMGWasherWoman.png')
    #player_image = pygame.transform.scale(player_image, (100, 100))  # Resize image to desired size


    def create_circular_image(image, outline_thickness=8):
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

    # Apply the circular mask to the player and central entity images
    # Central entity image (new entity in the middle)
    central_entity_image = pygame.image.load('src/SimVisualiser/RoleImg/IMGStoryTeller.png')  # Replace with your central image
    central_entity_image = create_circular_image(central_entity_image)
    central_entity_image = pygame.transform.scale(central_entity_image, (120, 120))  # Resize to fit well in the center


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


    # Create players
    players = []
    for (i, key) in enumerate(game_players):
        players.append([PlayerEntity(f"{game_players[key].player_name}"), game_players[key]])

    # Main room position (centered in the window)
    x = (WIDTH - MAIN_ROOM_WIDTH) // 2
    y = (HEIGHT - MAIN_ROOM_WIDTH) // 2
    main_room = pygame.Rect(x, y, MAIN_ROOM_WIDTH, MAIN_ROOM_WIDTH)  # Main room in the center (large)

    # Update ROOM_CENTER to be the center of the main room
    ROOM_CENTER = (main_room.x + main_room.width // 2, main_room.y + main_room.height // 2)

    # Game loop
    running = True
    clock = pygame.time.Clock()

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)  # Fill the screen with black

        # Draw the main room
        pygame.draw.rect(screen, FLOOR_COL, main_room)  # Main room

        # Draw the central entity in the center of the main room
        screen.blit(central_entity_image, (ROOM_CENTER[0] - 35, ROOM_CENTER[1] - 35))  # Center the central entity image

        # Draw the players in a circle inside the main room
        for i, player in enumerate(players):
            player[0].update_position(i, len(players), ROOM_CENTER)  # Pass the total number of players
            player_image = pygame.image.load(RoleImgDict[type(player[1].character)])
            player_image = create_circular_image(player_image)
            player_image = pygame.transform.scale(player_image, (90, 90))
            screen.blit(player_image, (player[0].x - player_image.get_width() // 2, player[0].y - player_image.get_height() // 2))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Check if the 'q' key was pressed
                    running = False  # Stop the game loop

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Frame rate

    pygame.quit()
