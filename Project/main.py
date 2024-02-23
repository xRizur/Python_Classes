import pygame
from maze import Maze, Wall
from player import Player
from menu import show_main_menu, show_pause_menu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def run_maze_game():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Game")
    font = pygame.font.Font(None, 36)

    if not show_main_menu(screen, font):
        pygame.quit()
        return

    level = 1
    total_time = 0
    running = True
    pause = False
    pause_menu_options = ["Resume", "Restart", "Exit"]
    selected_option = 0

    while running:
        maze_size = 10 + level * 2
        cell_size = min(screen_width // maze_size, screen_height // maze_size)
        maze = Maze(maze_size, maze_size)
        maze.generate()
        player = Player(0, 0)
        start_time = pygame.time.get_ticks()

        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = not pause
                        selected_option = 0
                    if not pause:
                        if event.key == pygame.K_UP:
                            player.move(Wall.TOP, maze)
                        elif event.key == pygame.K_DOWN:
                            player.move(Wall.BOTTOM, maze)
                        elif event.key == pygame.K_LEFT:
                            player.move(Wall.LEFT, maze)
                        elif event.key == pygame.K_RIGHT:
                            player.move(Wall.RIGHT, maze)
                    else:
                        if event.key == pygame.K_UP:
                            selected_option = (selected_option - 1) % len(pause_menu_options)
                        elif event.key == pygame.K_DOWN:
                            selected_option = (selected_option + 1) % len(pause_menu_options)
                        elif event.key == pygame.K_RETURN:
                            if pause_menu_options[selected_option] == "Resume":
                                pause = False
                            elif pause_menu_options[selected_option] == "Restart":
                                level = 1
                                total_time = 0
                                maze_size = 10 + level * 2
                                cell_size = min(screen_width // maze_size, screen_height // maze_size)
                                maze = Maze(maze_size, maze_size)
                                maze.generate()
                                player = Player(0, 0)
                                start_time = pygame.time.get_ticks()
                                pause = False
                                continue
                            elif pause_menu_options[selected_option] == "Exit":
                                running = False
                                game_running = False

            if not game_running or not running or pause:
                if pause:
                    show_pause_menu(screen, font, pause_menu_options, selected_option)
                continue

            current_time = (pygame.time.get_ticks() - start_time) / 1000 + total_time
            screen.fill((0, 0, 0))
            maze.draw(screen, cell_size)
            player.draw(screen, cell_size)

            goal_x, goal_y = (maze.width - 1) * cell_size, (maze.height - 1) * cell_size
            pygame.draw.rect(screen, WHITE, (goal_x, goal_y, cell_size, cell_size))

            time_text = font.render(f'Time: {current_time:.2f}s', True, WHITE)
            level_text = font.render(f'Level: {level}', True, WHITE)
            screen.blit(time_text, (10, 10))
            screen.blit(level_text, (10, 40))

            pygame.display.flip()

            if player.x == maze.width - 1 and player.y == maze.height - 1:
                level += 1
                total_time = current_time
                maze_size = 10 + level * 2
                cell_size = min(screen_width // maze_size, screen_height // maze_size)
                maze = Maze(maze_size, maze_size)
                maze.generate()
                player = Player(0, 0)
                start_time = pygame.time.get_ticks()

    pygame.quit()

run_maze_game()