import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge Arcade")

clock = pygame.time.Clock()

spaceship = pygame.image.load("spaceship.png")  
spaceship = pygame.transform.scale(spaceship, (50, 50))
spaceship_rect = spaceship.get_rect()

asteroid_img = pygame.image.load("asteroid.png")  
asteroid_img = pygame.transform.scale(asteroid_img, (40, 40))

star_img = pygame.image.load("star.png") 
star_img = pygame.transform.scale(star_img, (30, 30))

spaceship_rect.center = (WIDTH // 2, HEIGHT - 60)
speed = 5
score = 0
game_over = False

asteroids = [{"rect": pygame.Rect(random.randint(0, WIDTH - 40), random.randint(-600, -40), 40, 40)} for _ in range(5)]
stars = [{"rect": pygame.Rect(random.randint(0, WIDTH - 30), random.randint(-600, -30), 30, 30)} for _ in range(3)]


def reset_game():
    """Reset the game state."""
    global spaceship_rect, score, game_over, asteroids, stars
    spaceship_rect.center = (WIDTH // 2, HEIGHT - 60)
    score = 0
    game_over = False
    asteroids = [{"rect": pygame.Rect(random.randint(0, WIDTH - 40), random.randint(-600, -40), 40, 40)} for _ in range(5)]
    stars = [{"rect": pygame.Rect(random.randint(0, WIDTH - 30), random.randint(-600, -30), 30, 30)} for _ in range(3)]


def draw_text(text, size, color, x, y):
    """Draw text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spaceship_rect.left > 0:
            spaceship_rect.x -= speed
        if keys[pygame.K_RIGHT] and spaceship_rect.right < WIDTH:
            spaceship_rect.x += speed

        for asteroid_data in asteroids:
            asteroid_data["rect"].y += speed
            if asteroid_data["rect"].top > HEIGHT:
                asteroid_data["rect"].y = random.randint(-600, -40)
                asteroid_data["rect"].x = random.randint(0, WIDTH - 40)
            if spaceship_rect.colliderect(asteroid_data["rect"]):
                game_over = True

        for star_data in stars:
            star_data["rect"].y += speed
            if star_data["rect"].top > HEIGHT:
                star_data["rect"].y = random.randint(-600, -30)
                star_data["rect"].x = random.randint(0, WIDTH - 30)
            if spaceship_rect.colliderect(star_data["rect"]):
                score += 1
                star_data["rect"].y = random.randint(-600, -30)
                star_data["rect"].x = random.randint(0, WIDTH - 30)

    
    screen.fill(BLACK)
    screen.blit(spaceship, spaceship_rect)

    for asteroid_data in asteroids:
        screen.blit(asteroid_img, asteroid_data["rect"])
    for star_data in stars:
        screen.blit(star_img, star_data["rect"])

    draw_text(f"Score: {score}", 36, WHITE, WIDTH // 2, 30)

    if game_over:
        draw_text("GAME OVER! Press R to Restart", 48, WHITE, WIDTH // 2, HEIGHT // 2)

    pygame.display.flip()
    clock.tick(60)
