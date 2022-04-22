import pygame

from constants import (
    TILE_HEIGHT,
    BLACK,
    HORIZONTAL_GAP_HEIGHT,
    SCREEN_WIDTH,
    THICK_HORIZONTAL_GAP_HEIGHT,
    TILE_WIDTH,
    VERTICAL_GAP_WIDTH,
    THICK_VERTICAL_GAP_WIDTH,
    SCREEN_HEIGHT,
    SUDOKU_HEIGHT,
    WHITE,
    GRAY,
    GREEN,
    RED,
    FONT
)
from utils import vertical_gap, horizontal_gap


class Tile:
    def __init__(self, val=0, changeable=True):
        self.val = val
        self.changeable = changeable
        
        self.backval = 0
        self.is_marked = False
        self.is_collision = False
    
    def toggle_marked(self, x, y, window):
        self.is_marked = not self.is_marked
        self.draw(x, y, window)

    def set_collision(self, collision, x, y, window):
        self.is_collision = collision
        self.draw(x, y, window)

    def on_click(self, x, y, window):
        self.toggle_marked(x, y, window)

    def delete(self, x, y, window):
        if not self.changeable:
            return
        
        self.backval = 0
        self.val = 0
        self.draw(x, y, window)

    def update_backval(self, new_val, x, y, window):
        if not self.changeable:
            return
        
        self.backval = new_val
        self.draw(x, y, window)

    def update(self, x, y, window):
        if not self.changeable:
            return False

        self.val = self.backval
        self.backval = 0
        self.draw(x, y, window)

        return True

    def draw(self, x, y, window):        
        if self.is_marked:
            # thick black lines
            pygame.draw.rect(window, BLACK, (0, 3*TILE_HEIGHT + 2*HORIZONTAL_GAP_HEIGHT, SCREEN_WIDTH, THICK_HORIZONTAL_GAP_HEIGHT))
            pygame.draw.rect(window, BLACK, (0, 6*TILE_HEIGHT + 5*HORIZONTAL_GAP_HEIGHT, SCREEN_WIDTH, THICK_HORIZONTAL_GAP_HEIGHT))
            pygame.draw.rect(window, BLACK, (3*TILE_WIDTH + 2*VERTICAL_GAP_WIDTH, 0, THICK_VERTICAL_GAP_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(window, BLACK, (6*TILE_WIDTH + 5*VERTICAL_GAP_WIDTH, 0, THICK_VERTICAL_GAP_WIDTH, SCREEN_HEIGHT))

            # green marker
            pygame.draw.rect(window, GREEN, vertical_gap(x - VERTICAL_GAP_WIDTH - SUDOKU_HEIGHT/500, VERTICAL_GAP_WIDTH + SUDOKU_HEIGHT/250))
            pygame.draw.rect(window, GREEN, vertical_gap(x + TILE_WIDTH - SUDOKU_HEIGHT/500, VERTICAL_GAP_WIDTH + SUDOKU_HEIGHT/250))
            pygame.draw.rect(window, GREEN, horizontal_gap(y - HORIZONTAL_GAP_HEIGHT - SUDOKU_HEIGHT/500, HORIZONTAL_GAP_HEIGHT + SUDOKU_HEIGHT/250))
            pygame.draw.rect(window, GREEN, horizontal_gap(y + TILE_HEIGHT - SUDOKU_HEIGHT/500, HORIZONTAL_GAP_HEIGHT + SUDOKU_HEIGHT/250))
        else:
            # replace green marker
            pygame.draw.rect(window, WHITE, vertical_gap(x - VERTICAL_GAP_WIDTH - SUDOKU_HEIGHT/500, VERTICAL_GAP_WIDTH + SUDOKU_HEIGHT/250))
            pygame.draw.rect(window, WHITE, vertical_gap(x + TILE_WIDTH - SUDOKU_HEIGHT/500, VERTICAL_GAP_WIDTH + SUDOKU_HEIGHT/250))
            pygame.draw.rect(window, WHITE, horizontal_gap(y - HORIZONTAL_GAP_HEIGHT - SUDOKU_HEIGHT/500, HORIZONTAL_GAP_HEIGHT + SUDOKU_HEIGHT/250))
            pygame.draw.rect(window, WHITE, horizontal_gap(y + TILE_HEIGHT - SUDOKU_HEIGHT/500, HORIZONTAL_GAP_HEIGHT + SUDOKU_HEIGHT/250))

            # default black lines
            pygame.draw.rect(window, BLACK, vertical_gap(x - VERTICAL_GAP_WIDTH, VERTICAL_GAP_WIDTH))
            pygame.draw.rect(window, BLACK, vertical_gap(x + TILE_WIDTH, VERTICAL_GAP_WIDTH))
            pygame.draw.rect(window, BLACK, horizontal_gap(y - HORIZONTAL_GAP_HEIGHT, HORIZONTAL_GAP_HEIGHT))
            pygame.draw.rect(window, BLACK, horizontal_gap(y + TILE_HEIGHT, HORIZONTAL_GAP_HEIGHT))

            # thick black lines
            pygame.draw.rect(window, BLACK, (0, 3*TILE_HEIGHT + 2*HORIZONTAL_GAP_HEIGHT, SCREEN_WIDTH, THICK_HORIZONTAL_GAP_HEIGHT))
            pygame.draw.rect(window, BLACK, (0, 6*TILE_HEIGHT + 5*HORIZONTAL_GAP_HEIGHT, SCREEN_WIDTH, THICK_HORIZONTAL_GAP_HEIGHT))
            pygame.draw.rect(window, BLACK, (3*TILE_WIDTH + 2*VERTICAL_GAP_WIDTH, 0, THICK_VERTICAL_GAP_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(window, BLACK, (6*TILE_WIDTH + 5*VERTICAL_GAP_WIDTH, 0, THICK_VERTICAL_GAP_WIDTH, SCREEN_HEIGHT))

        if self.is_collision:
            pygame.draw.rect(window, RED, (x, y, TILE_WIDTH, TILE_HEIGHT))
        else:
            pygame.draw.rect(window, WHITE, (x, y, TILE_WIDTH, TILE_HEIGHT))
        
        font = pygame.font.SysFont(FONT, int(TILE_HEIGHT//2))

        if self.backval != 0:
            text = font.render(str(self.backval), True, GRAY)
            text_rect = text.get_rect()
            text_rect.center = (x + TILE_WIDTH/2), (y + TILE_HEIGHT/2)
            window.blit(text, text_rect)
        elif self.val != 0:
            text = font.render(str(self.val), True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (x + TILE_WIDTH/2), (y + TILE_HEIGHT/2)
            window.blit(text, text_rect)
