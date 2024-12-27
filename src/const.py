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

# Game setting {HARD_NAME, HEIGHT, WIDTH, SCORE_MULTIPLE}
GAME_DIFFICULTY = {
    "Hard": [105, 105, 300],
    "Medium": [75, 75, 200],
    "Easy": [25, 25, 50],
}


# Interface
MAIN_FONT_NAME = "KARMATIC ARCADE"
BLURRED_BG_PATH = "./app_file/assets/img/blurred_bg.ppm"
BG_PATH = "./app_file/assets/img/background.ppm"


# Button
BUTTON_TEXT_COLOR: str = "black"
FONT: tuple[str, int] = (MAIN_FONT_NAME, 25)
BUTTON_TEXT_COVER_COLOR = "purple"
TAGS: str = 'button'

