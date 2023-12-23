import pygame
import random
import time

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gra Snake")

red_fruit_img = pygame.image.load('apple.png')
blue_fruit_img = pygame.image.load('blue_fruit.png') 
fruit_size = 20
red_fruit_img = pygame.transform.scale(red_fruit_img, (fruit_size, fruit_size))
blue_fruit_img = pygame.transform.scale(blue_fruit_img, (fruit_size, fruit_size))

snake_size = 20
snake = [{'x': screen_width / 2, 'y': screen_height / 2}]
snake_dx = 0
snake_dy = 0

# sekundy do aktualizacji pozycji owoców
fruit_update_interval = 8
fruits = [{
    'x': random.randrange(0, screen_width - fruit_size, fruit_size),
    'y': random.randrange(0, screen_height - fruit_size, fruit_size),
    'type': 'nutritious',
    'last_eaten_time': time.time()
}, {
    'x': random.randrange(0, screen_width - fruit_size, fruit_size),
    'y': random.randrange(0, screen_height - fruit_size, fruit_size),
    'type': random.choice(['nutritious', 'poisonous']),
    'last_eaten_time': time.time()
}]

score = 0
game_over = False
clock = pygame.time.Clock()
speed = 10
last_speed_increase_score = 0

while not game_over:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = snake_size
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy == 0:
                snake_dy = -snake_size
                snake_dx = 0
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dy = snake_size
                snake_dx = 0

    snake_head = {'x': snake[0]['x'] + snake_dx, 'y': snake[0]['y'] + snake_dy}

    # Sprawdzanie kolizji węża z własnym ciałem - zakonczenie gry
    if any(segment['x'] == snake_head['x'] and segment['y'] == snake_head['y'] for segment in snake[1:]):
        game_over = True
        break

    snake.insert(0, snake_head)

    # Warunki brzegowe weza
    if snake[0]['x'] >= screen_width:
        snake[0]['x'] = 0
    elif snake[0]['x'] < 0:
        snake[0]['x'] = screen_width - snake_size
    if snake[0]['y'] >= screen_height:
        snake[0]['y'] = 0
    elif snake[0]['y'] < 0:
        snake[0]['y'] = screen_height - snake_size

    # Sprawdzanie kolizji z owocami i aktualizacja dlguośći węża
    for fruit in fruits:
        if snake[0]['x'] == fruit['x'] and snake[0]['y'] == fruit['y']:
            if fruit['type'] == 'nutritious':
                score += 1
                # Powiększanie węża
                snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y']})
            else:
                score -= 1
                # Skracanie węża, jeśli jest dłuższy niż 1 segment
                if len(snake) > 1:
                    snake.pop()

            # Regeneracja owocu
            fruit['x'] = random.randrange(0, screen_width - fruit_size, fruit_size)
            fruit['y'] = random.randrange(0, screen_height - fruit_size, fruit_size)
            fruit['type'] = random.choice(['nutritious', 'poisonous'])
            fruit['last_eaten_time'] = current_time

            # Przynajmniej jeden owoc czerwony
            if all(f['type'] == 'poisonous' for f in fruits):
                fruit['type'] = 'nutritious'
            # Zwiększanie prędkości węża co 10 punktów
            if score // 10 > last_speed_increase_score:
                speed += 1
                last_speed_increase_score = score // 10
        elif current_time - fruit['last_eaten_time'] > fruit_update_interval:
            fruit['x'] = random.randrange(0, screen_width - fruit_size, fruit_size)
            fruit['y'] = random.randrange(0, screen_height - fruit_size, fruit_size)
            fruit['last_eaten_time'] = current_time

    if not (snake[0]['x'] == fruit['x'] and snake[0]['y'] == fruit['y'] and fruit['type'] == 'nutritious'):
        snake.pop()

    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), [segment['x'], segment['y'], snake_size, snake_size])
    for fruit in fruits:
        img = red_fruit_img if fruit['type'] == 'nutritious' else blue_fruit_img
        screen.blit(img, (fruit['x'], fruit['y']))

    # Wyświetlanie wyniku
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Wynik: {score}", True, (255, 255, 255))
    screen.blit(score_text, [0, 0])

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
