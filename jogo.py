import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações da tela
screen_width = 800  
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CodeQuest: O Labirinto dos Códigos')

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)  # Cor para as paredes do labirinto

# Configurações do personagem
player_image = pygame.image.load('mario.png')  # Substitua por sua imagem
player_size = (60, 60)  # Ajuste conforme o tamanho da imagem
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Configurações do objetivo
goal_size = 80
goal_color = GREEN
goal_x = 500
goal_y = 530

# Configurações do labirinto
walls = [
    # Borda externa
    pygame.Rect(50, 50, 700, 20),
    pygame.Rect(50, 50, 20, 500),
    pygame.Rect(50, 530, 450, 20),
    pygame.Rect(580, 530, 170, 20),
    pygame.Rect(730, 50, 20, 500),
    
    # Corredores internos
    pygame.Rect(300, 360, 250, 20), #x, y, largura, altura
    pygame.Rect(200, 280, 400, 20),
    pygame.Rect(600, 280, 20, 100),
    pygame.Rect(200, 280, 20, 180),
    pygame.Rect(200, 450, 400, 20),
    pygame.Rect(700, 280, 20, 100),
]
# Fonte
font = pygame.font.SysFont(None, 36)

def draw_player(x, y):
    # Desenha o personagem usando a imagem
    screen.blit(pygame.transform.scale(player_image, player_size), (x, y))

def draw_goal(x, y):
    pygame.draw.rect(screen, goal_color, (x, y, goal_size, goal_size))

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, GREY, wall)

def display_message(message, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

def main():
    global player_x, player_y
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        
        # Movimento do personagem
        new_x = player_x
        new_y = player_y
        
        if keys[pygame.K_LEFT]:
            new_x -= player_speed
        if keys[pygame.K_RIGHT]:
            new_x += player_speed
        if keys[pygame.K_UP]:
            new_y -= player_speed
        if keys[pygame.K_DOWN]:
            new_y += player_speed
        
        # Verificação de colisão com as paredes
        new_rect = pygame.Rect(new_x, new_y, *player_size)
        if not any(wall.colliderect(new_rect) for wall in walls):
            player_x = new_x
            player_y = new_y

        screen.fill(WHITE)
        draw_walls(walls)
        draw_player(player_x, player_y)
        draw_goal(goal_x, goal_y)
        
        if (goal_x <= player_x <= goal_x + goal_size and
            goal_y <= player_y <= goal_y + goal_size):
            display_message('Você completou o desafio!', BLUE, 20, 20)
        else:
            display_message('Use as setas do teclado para mover o personagem!', BLACK, 20, 20)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
