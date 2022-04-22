from constants import TILE_WIDTH, TILE_HEIGHT, VERTICAL_GAP_WIDTH, HORIZONTAL_GAP_HEIGHT, SUDOKU_HEIGHT, SUDOKU_WIDTH


coordinate_builder = lambda x, y: (y*(TILE_WIDTH + VERTICAL_GAP_WIDTH), x*(TILE_HEIGHT + HORIZONTAL_GAP_HEIGHT))
vertical_gap = lambda x, width: (x, 0, width, SUDOKU_HEIGHT)
horizontal_gap = lambda y, height: (0, y, SUDOKU_WIDTH, height)
