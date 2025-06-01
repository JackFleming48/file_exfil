import pygame
import time
import random


def rungame():
    # Initialize pygame
    pygame.init()

    # Set up screen size
    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Snake block size and speed
    block_size = 20
    snake_speed = 15

    # Fonts
    font_style = pygame.font.SysFont(None, 35)
    score_font = pygame.font.SysFont(None, 30)

    # Clock
    clock = pygame.time.Clock()

    # Score display
    def show_score(score):
        value = score_font.render(f"Score: {score}", True, white)
        screen.blit(value, [10, 10])

    # Snake drawing function
    def draw_snake(block_size, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

    # Game Over message
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width // 6, height // 3])

    # Main function
    def game_loop():
        game_over = False
        game_close = False

        # Initial position
        x1 = width // 2
        y1 = height // 2

        # Change in position
        x1_change = 0
        y1_change = 0

        # Snake body
        snake_list = []
        length_of_snake = 1

        # Food position
        foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
        foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

        while not game_over:

            while game_close:
                screen.fill(black)
                message("Game Over! Press Q-Quit or C-Play Again", red)
                show_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -block_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = block_size
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -block_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = block_size
                        x1_change = 0

            x1 += x1_change
            y1 += y1_change

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True

            screen.fill(blue)
            pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check collision with self
            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(block_size, snake_list)
            show_score(length_of_snake - 1)

            pygame.display.update()

            # Check food collision
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
                foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    game_loop()

# Run game
if __name__ == "__main__":
    rungame()