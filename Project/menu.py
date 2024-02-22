import pygame
# Definicje kolorów
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

def show_main_menu(screen, font):
    running = True
    while running:
        screen.fill(BLACK)
        title_text = font.render('Maze Game', True, WHITE)
        start_text = font.render('Start', True, WHITE)
        quit_text = font.render('Quit', True, WHITE)

        title_rect = title_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 60))
        start_rect = start_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        quit_rect = quit_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 60))

        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    return True
                elif quit_rect.collidepoint(pygame.mouse.get_pos()):
                    return False

def show_pause_menu(screen, font, options, selected_index):
    screen.fill(BLACK)
    for i, option in enumerate(options):
        color = YELLOW if i == selected_index else WHITE
        text_surface = font.render(option, True, color)
        text_rect = text_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 30 + i * 40))
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
