import pygame

pygame.init()

BLACK : tuple = (0, 0, 0)
GREY : tuple = (128, 128, 128)
YELLOW : tuple = (255, 255, 0)
WHITE : tuple = (255, 255, 255)

WIDTH, HEIGHT : int = 1200, 800
TILE_SIZE : int = 20
GRID_WIDTH : int = WIDTH // TILE_SIZE
GRID_HEIGHT : int = HEIGHT // TILE_SIZE
FPS : int = 60

data : list(int) = [1, 2, 15, 32, 7, 9, 10, 2]

screen : pygame.Surface = pygame.display.set_mode(size =(WIDTH, HEIGHT))

clock : pygame.Clock = pygame.time.Clock()

def drawLines() -> None:
    # top left is 0 0
    for index, value in enumerate(data):
        # To Do: Do dynamic scaling so big values are not drawn outside of height, and longer lists not outside of width, dynamic width?
        pygame.draw.line(surface = screen, color = WHITE, start_pos = (0 + 20*index, HEIGHT), end_pos = (0 + 20*index, HEIGHT - value*20), width = 5)

def main() -> None:
    running : bool = True
    
    while running:
        clock.tick(framerate = FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawLines()
        pygame.display.update()

    pygame.quit()

main()