SUDOKU_WIDTH = 850
SUDOKU_HEIGHT = 850
CAPTION = "Sudoku"

FONT = "comicsans"
WIN_FONT_SIZE = SUDOKU_HEIGHT//10

VERTICAL_GAP_WIDTH = SUDOKU_WIDTH/300
THICK_VERTICAL_GAP_WIDTH = 2*VERTICAL_GAP_WIDTH
HORIZONTAL_GAP_HEIGHT = SUDOKU_HEIGHT/300
THICK_HORIZONTAL_GAP_HEIGHT = 2*HORIZONTAL_GAP_HEIGHT

TILE_WIDTH = (SUDOKU_WIDTH-8*VERTICAL_GAP_WIDTH)/9
TILE_HEIGHT = (SUDOKU_HEIGHT-8*HORIZONTAL_GAP_HEIGHT)/9

INFORMATION_HEIGHT = TILE_HEIGHT + HORIZONTAL_GAP_HEIGHT
SCREEN_WIDTH = SUDOKU_WIDTH
SCREEN_HEIGHT = SUDOKU_HEIGHT + INFORMATION_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
