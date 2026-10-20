import curses
import os



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


def center_text(newwin, y, text, attr):
    height, width = newwin.getmaxyx()

    if 0 < y < height - 1 and len(text) < width - 2:
        x = (width - len(text)) // 2
        newwin.addstr(y, x, text, attr)

def load_character_screen(newwin):
    pass

def game(newwin):
    curses.curs_set(0)
    newwin.keypad(True)
    curses.start_color()
    curses.use_default_colors()


def load_instruction_screen(newwin):
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        newwin.clear()
        height, width = newwin.getmaxyx()

        newwin.border()

        center_text(newwin, height // 5, 'INSTRUCTIONS', attr)

        center_text(newwin, height // 2 - 2,
                    'Your goal is to avoid teachers and escape Habib', attr2)

        center_text(newwin, height // 2 - 1,
                    'from either Gate 2 or Gate 4.', attr2)

        center_text(newwin, height - 4,
                    'Press 5 to go back to home screen.', attr2)

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

    center_text(newwin, height // 5,
                'ESCAPE HABIB: BUNK', attr)

    center_text(newwin, height // 5 + 1,
                'A CLASS', attr)

    menu_start = height // 2 - 3

    center_text(newwin, menu_start,
                '1. START GAME', attr2)

    center_text(newwin, menu_start + 1,
                '2. CHANGE CHARACTER', attr2)

    center_text(newwin, menu_start + 2,
                '3. INSTRUCTIONS', attr2)

    center_text(newwin, menu_start + 3,
                '4. HIGH SCORE', attr2)

    center_text(newwin, menu_start + 4,
                '5. QUIT', attr2)

    center_text(newwin, height - 4,
                'POWERED BY TMZ (The Mighty Zingers)', attr3)

    newwin.refresh()


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
        init_color()

        if key == ord('1'):
            pass
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