import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 700, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
FONT = pygame.font.SysFont("Arial", 20)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎹 Virtual Piano")

# Define piano keys and their sounds
keys = [
    {'note': 'C', 'key': pygame.K_a},
    {'note': 'D', 'key': pygame.K_s},
    {'note': 'E', 'key': pygame.K_d},
    {'note': 'F', 'key': pygame.K_f},
    {'note': 'G', 'key': pygame.K_g},
    {'note': 'A', 'key': pygame.K_h},
    {'note': 'B', 'key': pygame.K_j},
]

# Load sounds
for key in keys:
    key['sound'] = pygame.mixer.Sound(f"sounds/{key['note']}.wav")

# Draw white keys
def draw_keys(pressed_key=None):
    key_width = WIDTH // len(keys)
    for i, key in enumerate(keys):
        x = i * key_width
        color = GREY if pressed_key == key['key'] else WHITE
        pygame.draw.rect(screen, color, (x, 0, key_width, HEIGHT))
        pygame.draw.rect(screen, BLACK, (x, 0, key_width, HEIGHT), 2)
        label = FONT.render(key['note'], True, BLACK)
        screen.blit(label, (x + key_width // 2 - 5, HEIGHT - 40))

# Main loop
def main():
    running = True
    while running:
        screen.fill(BLACK)
        draw_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Play note on key press
            if event.type == pygame.KEYDOWN:
                for key in keys:
                    if event.key == key['key']:
                        key['sound'].play()
                        draw_keys(pressed_key=key['key'])

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

