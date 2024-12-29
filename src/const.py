# Game logic
MAZE_MAP_FILE = "./app_file/maze_map.txt"
MAZE_CONFIG_MAP = "./app_file/maze_config.txt"
MAZE_GENERATOR_DLL_LIB_PATH = "./src/game/maze_generator/maze_lib.dll"

# Game render
OUTLINE_COLOR = "black"
PLAYER_COLOR = "red"
FPS = 144
GAME_MAP_PADDING = 20
DEFAULT_TIMER_TIME_STR = "00:00:00"

# Game setting {DIFFICULTY_NAME, HEIGHT, WIDTH, SCORE_MULTIPLE}
GAME_DIFFICULTY = {
    "Hard": [105, 105, 300],
    "Medium": [75, 75, 200],
    "Easy": [25, 25, 50],
}

#Game
GAME_NAME = "Wonder maze"


# Interface
MAIN_FONT_NAME = "KARMATIC ARCADE"
MAIN_FONT = (MAIN_FONT_NAME, 25)
GAME_NAME_FONT = (MAIN_FONT_NAME, 100, "bold")

BLURRED_BG_PATH = "./app_file/assets/img/blurred_bg.ppm"
BG_PATH = "./app_file/assets/img/background.ppm"

# Table
TABLE_LINE_COLOR = "black"
TABLE_ENTRY_COLOR = "black"
TABLE_HEADER_NAME_COLOR = "purple"
TABLE_LINE_WIDTH = 10

TABLE_TOP_MARGIN = 20
TABLE_RIGHT_MARGIN = 50
TABLE_BOTTOM_MARGIN = 100
TABLE_LEFT_MARGIN = 50


# Button
BUTTON_TEXT_COLOR = "black"
BUTTON_TEXT_COVER_COLOR = "purple"
TAGS= 'button'

#Timer
TIMER_FILL = "purple"