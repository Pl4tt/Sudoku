import pygame
from copy import deepcopy

from sudoku_solver import solve, is_valid, all_invalid
from tile import Tile
from utils import coordinate_builder


class Board:
    def __init__(self, board, window, information_panel):
        self.board = board
        self.tiles = self.create_tiles()
        self.window = window
        self.information_panel = information_panel
        
        self.marked = None
        self.invalids = []

        if not solve(deepcopy(board)):
            pygame.quit()

    def create_tiles(self):
        result = []

        for x in range(len(self.board)):
            result.append([])

            for val in self.board[x]:
                result[x].append(Tile(val, val==0))
        
        return result

    def is_valid(self, x, y, val):
        return is_valid(self.board, x, y, val)
    
    def all_invalid(self, x, y, val):
        return all_invalid(self.board, x, y, val)

    def on_click(self, row, col):
        if self.marked is not None:
            x, y, = self.marked
            coordinate = coordinate_builder(x, y)
            self.tiles[x][y].toggle_marked(*coordinate, self.window)

        coordinate = coordinate_builder(row, col)
        self.tiles[row][col].on_click(*coordinate, self.window)
        self.marked = (row, col)

    def clean_validation(self):
        remove = []

        for ix, iy in self.invalids:
            coords = coordinate_builder(ix, iy)

            if self.board[ix][iy] == 0:
                self.tiles[ix][iy].set_collision(False, *coords, self.window)

            elif self.is_valid(ix, iy, self.board[ix][iy]):
                self.tiles[ix][iy].set_collision(False, *coords, self.window)
                remove.append((ix, iy))
            else:
                self.tiles[ix][iy].set_collision(True, *coords, self.window)
        
        for rm in remove:
            self.invalids.remove(rm)
        
    def delete(self):
        if self.marked is None:
            return

        x, y = self.marked
        coordinate = coordinate_builder(x, y)

        if not self.tiles[x][y].changeable:
            return

        self.tiles[x][y].delete(*coordinate, self.window)

        self.board[x][y] = 0

        self.clean_validation()
        
        self.tiles[x][y].draw(*coordinate, self.window)
    
    def update_backval(self, new_val):
        if self.marked is None:
            return

        x, y = self.marked
        coordinate = coordinate_builder(x, y)

        if not self.tiles[x][y].changeable:
            return

        self.tiles[x][y].update_backval(new_val, *coordinate, self.window)

    def update(self):
        if self.marked is None:
            return

        x, y = self.marked
        coordinate = coordinate_builder(x, y)

        if not self.tiles[x][y].changeable:
            return

        new_val = self.tiles[x][y].backval
        if new_val == 0:
            return

        if not self.is_valid(x, y, new_val) and new_val != 0:
            self.information_panel.mistake()
            self.tiles[x][y].set_collision(True, *coordinate, self.window)

            self.invalids.append((x, y))
            self.invalids.extend(self.all_invalid(x, y, new_val))

            for ix, iy in self.invalids:
                coords = coordinate_builder(ix, iy)
                self.tiles[ix][iy].set_collision(True, *coords, self.window)

        if self.tiles[x][y].update(*coordinate, self.window):
            self.board[x][y] = new_val
            
        self.clean_validation()

        self.tiles[x][y].draw(*coordinate, self.window)

        return self.is_win()

    def is_filled(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    return False
        
        return True

    def is_win(self):
        return not self.invalids and self.is_filled()

    def draw(self):
        for x, row in enumerate(self.tiles):
            for y, tile in enumerate(row):
                coordinate = coordinate_builder(x, y)
                tile.draw(*coordinate, self.window)
