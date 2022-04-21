import pygame
import time

from sudoku_solver import print_board, boards
from constants import (
    FONT,
    WIN_FONT_SIZE,
    GREEN,
    SUDOKU_HEIGHT,
    SUDOKU_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    CAPTION,
    TILE_HEIGHT,
    TILE_WIDTH,
    HORIZONTAL_GAP_HEIGHT,
    VERTICAL_GAP_WIDTH
)
from information_panel import InformationPanel
from board import Board


def draw_win(window):
    font = pygame.font.SysFont(FONT, WIN_FONT_SIZE)
    text = font.render("YOU'VE WON! :)", True, GREEN)
    text_rect = text.get_rect()
    text_rect.center = SUDOKU_WIDTH/2, SUDOKU_HEIGHT/2
    window.blit(text, text_rect)

    font2 = pygame.font.SysFont(FONT, int(WIN_FONT_SIZE//2))
    text2 = font2.render("this window will quit in 10 Seconds", True, GREEN)
    text2_rect = text2.get_rect()
    text2_rect.center = SUDOKU_WIDTH/2, SUDOKU_HEIGHT/2 + WIN_FONT_SIZE
    window.blit(text2, text2_rect)

    pygame.display.update()


def launch(board_list):
    pygame.init()
    
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)

    start_time = time.time()
    information_panel = InformationPanel(0, start_time, window)
    information_panel.draw()

    board = Board(board_list, window, information_panel)
    board.draw()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:  # select tile
                row = int(event.pos[1]//(TILE_HEIGHT + HORIZONTAL_GAP_HEIGHT))
                col = int(event.pos[0]//(TILE_WIDTH + VERTICAL_GAP_WIDTH))
                board.on_click(row, col)
            
            elif event.type == pygame.KEYDOWN:
                key = event.key
                
                match key:
                    case 8 | 127 | 48:  # del / backspace / 0
                        board.update(0)

                    case num if 57 >= num >= 49:  # [1;9]
                        if board.update(int(chr(num))):  # win
                            draw_win(window)
                            print_board(board.board)
                            pygame.time.wait(10000)
                            running = False

        information_panel.tick()

        pygame.display.update()



if __name__ == "__main__":
    level = int(input("Enter the difficulty you want to play [1-3] "))

    if level < 1 or level > 3:
        raise Exception("difficulty must be 1, 2 or 3")

    launch(boards[level-1])
