import curses
import os
from datetime import datetime

MAP_LAYOUT_G_FLOOR = [
    "#######################################################################################################################",
    "#    [Ecology W121] #   [Dig.Sys &  #                                                                                 #",
    "#                   #    Ins. W114] #               [MATLAB W110]         [Physics W100]    # [Student Center]        #",
    "#######   ###########               #                                                       #                         #",
    "#  [Chemistry W118] #[Communications]               #############   ###   ###############   #             #############",
    "#                   #     W111]     #               # [Stair 2] #   # |   # [Wellness   #   #   [OCS]     #           #",
    "#######   ###########   #############               #           #   # |   #  Center]    #   #             #           #",
    "      #                                             #############   # |   ###############   ###############           #",
    "#######   ###########################   #########                   # |                     #  [Student   #   #########",
    "#   [Faculty C114]  #                   #[C-109]#   #############   # |                     #   Life]     #   #       #",
    "#                   #   #############   #########   # [Faculty  #   # |   ###############   #             #   # Gate2 #",
    "#######   ###########   # [Stair 9] #               #    Pod]   #   # |   #             #   ###############   #       #",
    "      #   #             #############               #############   # |   # [Reception] #   #                 #       #",
    "      #####   #######                                               ###   #             #####                 #       #",
    "          #   #     #   #############   #############################     ###############                     #       #",
    "  #########   #######   # [Stair 7] #   # [Stair 8] #                                                         #       #",
    "  #                     #############   #############   #######################################################       #",
    "  #   #############                                     #[Tech Alpha/Beta]#                                           #",
    "  #   #  [E121]   #                                     #   N-425/N-426   #   #############                           #",
    "  #   #############         #####################       ###################   # [Stairs]  #                           #",
    "  #                         #   [Cassim Lab]    #                             #############                           #",
    "  #                                                                                                                   #",
    " ######################################################################################################################",
]

def init_color():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_GREEN)

    #color initializing for map rendering specficially
    wall_color = 174 
    wall_background = 236
    path_color = 108
    curses.init_pair(4, wall_color, wall_background)
    curses.init_pair(5, path_color, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK) 
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK) 

def center_text(newwin, y, text, attr):
    height, width = newwin.getmaxyx()
    if 0 < y < height - 1 and len(text) < width - 2:
        x = (width - len(text)) // 2
        newwin.addstr(y, x, text, attr)

#actual game functions
def game(newwin):
    curses.curs_set(0)
    newwin.keypad(True)
    init_color()

    #spawn location of player    
    player_y = 5
    player_x = 8

    #map max_width
    map_width = 0
    for i in MAP_LAYOUT_G_FLOOR:
        if len(i) > map_width:
            map_width = len(i)

    while True:
        newwin.erase()

        #current terminal max height and width
        rows, cols = newwin.getmaxyx()

        newwin.addstr(0, 1, "Tile: you", curses.color_pair(3))

        #time for retro feel
        stamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        newwin.addnstr(0, max(1, cols - len(stamp) - 2), stamp, len(stamp), curses.color_pair(6))

        #map rendering logics
        for y in range(len(MAP_LAYOUT_G_FLOOR)):
            row = MAP_LAYOUT_G_FLOOR[y]
            for x in range(len(row)):
                char = row[x]
                if char == "#":
                    newwin.addch(y + 1, x + 1, "#", curses.color_pair(4) | curses.A_BOLD)
                elif char == " " and x % 2 == 0:
                    newwin.addch(y + 1, x + 1, ".", curses.color_pair(5))
                elif char == " " and x % 2 != 0:
                    newwin.addch(y + 1, x + 1, char, curses.color_pair(5))
                elif char == "|":
                    newwin.addch(y + 1, x + 1, char, curses.color_pair(5) | curses.A_BOLD)
                else:
                    newwin.addch(y + 1, x + 1, char, curses.color_pair(7))

        #actual spawning player
        newwin.addch(player_y + 1, player_x + 1, "@", curses.color_pair(6) | curses.A_BOLD)
        newwin.refresh()

        #waiting here for getting an action key
        key = newwin.getch()

        #breaking if press q or Q
        if key in (ord("q"), ord("Q")):
            break

        #player movement logic on pressing arrow keys
        new_y, new_x = player_y, player_x
        if key == curses.KEY_UP:
            new_y -= 1
        elif key == curses.KEY_DOWN:
            new_y += 1
        elif key == curses.KEY_LEFT:
            new_x -= 1
        elif key == curses.KEY_RIGHT:
            new_x += 1

        #if not colliding with walls or getting out of map, player coordinates changes with the new ones
        if 0 <= new_y < len(MAP_LAYOUT_G_FLOOR) and 0 <= new_x < len(MAP_LAYOUT_G_FLOOR[new_y]):
            if MAP_LAYOUT_G_FLOOR[new_y][new_x] not in ("#"):
                player_y = new_y
                player_x = new_x

def load_instruction_screen(newwin):
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        newwin.clear()
        height, width = newwin.getmaxyx()
        newwin.border()

        center_text(newwin, height // 5, 'INSTRUCTIONS', attr)
        center_text(newwin, height // 2 - 2, 'Your goal is to avoid teachers and escape Habib', attr2)
        center_text(newwin, height // 2 - 1, 'from either Gate 2 or Gate 4.', attr2)
        center_text(newwin, height - 4, 'Press 5 to go back to home screen.', attr2)

        newwin.refresh()
        key = newwin.getch()
        if key == ord('5'):
            return

def load_home_screen(newwin):
    newwin.clear()

    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD
    attr3 = curses.color_pair(3) | curses.A_BOLD

    height, width = newwin.getmaxyx()

    newwin.border()
    newwin.keypad(True)

    center_text(newwin, height // 5, 'ESCAPE HABIB: BUNK', attr)
    center_text(newwin, height // 5 + 1, 'A CLASS', attr)

    menu_start = height // 2 - 3

    center_text(newwin, menu_start, '1. START GAME', attr2)
    center_text(newwin, menu_start + 1, '2. CHANGE CHARACTER', attr2)
    center_text(newwin, menu_start + 2, '3. INSTRUCTIONS', attr2)
    center_text(newwin, menu_start + 3, '4. HIGH SCORE', attr2)
    center_text(newwin, menu_start + 4, '5. QUIT', attr2)
    center_text(newwin, height - 4, 'POWERED BY TMZ (The Mighty Zingers)', attr3)

    newwin.refresh()

def load_character_screen(newwin):
    pass

def main(stdscr):
    curses.curs_set(0)
    init_color()
    stdscr.clear()
    stdscr.keypad(True)
    newwin = stdscr

    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        load_home_screen(newwin)
        key = newwin.getch()

        if key == ord('1'):
            game(newwin)
        elif key == ord('2'):
            load_character_screen(newwin)
        elif key == ord('3'):
            load_instruction_screen(newwin)
        elif key == ord('4'):
            newwin.clear()
            height, width = newwin.getmaxyx()
            newwin.border()
            center_text(newwin, height // 2,
                        "HIGH SCORE", attr2)
        elif key == ord('5'):
            break


if os.name == "nt":
    os.system("mode con: cols=180 lines=55")


if __name__ == "__main__":
    curses.wrapper(main)