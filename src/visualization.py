import pygame

pygame.init()

# RELOCATE CONSTANTS TO SEPARATE FILE
BLACK : tuple[int, int, int] = (0, 0, 0)
GREY : tuple = (128, 128, 128)
YELLOW : tuple = (255, 255, 0)
WHITE : tuple = (255, 255, 255)

WIDTH : int = 1200
HEIGHT : int = 800
TILE_SIZE : int = 20
GRID_WIDTH : int = WIDTH // TILE_SIZE
GRID_HEIGHT : int = HEIGHT // TILE_SIZE
FPS : int = 60
WIDTH_OFFSET : int = 15
WIDTH_STEP : int = 20
HEIGHT_OFFSET : int = 15
#HEIGHT_STEP : int = 20 #What is this supposed to be?

data : list[int] = [1, 2, 15, 32, 7, 9, 10, 2]

screen : pygame.Surface = pygame.display.set_mode(size =(WIDTH, HEIGHT))

clock : pygame.time.Clock = pygame.time.Clock()

def drawLines(input : list[int]) -> None:
    # top left is 0 0
    max_val : int = max(input)

    for index, value in enumerate(input):
        # To Do: longer lists not outside of width, dynamic width?
        temp : int = (HEIGHT-HEIGHT_OFFSET) * (value / max_val)
        pygame.draw.line(surface = screen,
                        color = WHITE, 
                        start_pos = (WIDTH_OFFSET + WIDTH_STEP*index, HEIGHT), 
                        end_pos = (WIDTH_OFFSET + WIDTH_STEP*index, HEIGHT-temp),
                        width = 5)

def main() -> None:
    running : bool = True
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawLines(data)
        pygame.display.update()
        # Watch it groooooooow:
        data[0] += 0.05

    pygame.quit()

main()