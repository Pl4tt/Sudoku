import pygame
import time

from constants import FONT, SCREEN_HEIGHT, SUDOKU_WIDTH, TILE_WIDTH, TILE_HEIGHT, BLACK, WHITE, RED
from utils import coordinate_builder



class InformationPanel:
    def __init__(self, mistakes, start_time, window):
        self.mistakes = mistakes
        self.window = window

        self.start_time = start_time
        self.time = start_time
    
    def get_time(self):
        seconds = self.time%60
        minutes = (self.time//60)%60
        hours = (self.time-seconds-minutes*60)//(60*60)

        seconds = "0" + str(int(seconds)) if len(str(int(seconds))) < 2 else str(int(seconds))
        minutes = "0" + str(int(minutes)) if len(str(int(minutes))) < 2 else str(int(minutes))
        hours = "0" + str(int(hours)) if len(str(int(hours))) < 2 else str(int(hours))

        return f"{hours}:{minutes}:{seconds}"
    
    def tick(self):
        self.time = time.time() - self.start_time
        self.draw()

    def mistake(self):
        self.mistakes += 1
        self.draw()
    
    def rm_mistake(self):
        self.mistakes -= 1
        self.draw()

    def draw(self):
        pygame.draw.rect(self.window, WHITE, (*coordinate_builder(9, 0), SUDOKU_WIDTH, TILE_HEIGHT))

        font = pygame.font.SysFont(FONT, int(TILE_HEIGHT//2))
        text = font.render(str(self.get_time()), True, BLACK)
        text_rect = text.get_rect()
        text_rect.centery = SCREEN_HEIGHT - TILE_HEIGHT/2
        text_rect.right = SUDOKU_WIDTH - TILE_WIDTH/2
        self.window.blit(text, text_rect)

        mistakes = font.render("X"*self.mistakes, True, RED)
        mistakes_rect = mistakes.get_rect()
        mistakes_rect.centery = SCREEN_HEIGHT - TILE_HEIGHT/2
        mistakes_rect.left = TILE_WIDTH/2
        self.window.blit(mistakes, mistakes_rect)
        
