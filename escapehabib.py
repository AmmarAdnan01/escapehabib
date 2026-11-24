import curses
import os
import time

if os.name == "nt":  # Check whether the system is Windows.
    os.system("mode con: cols=180 lines=55")  # set the terminal to this size

MAP_GAME_OVER = [
    (
        '#############################################################'
        '##########################################################'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                               E S C A P E  '
        ' H A B I B                                               #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                   -----------------------------------------'
        '---------------------------------------                  #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                       ####      ##     #    #   ######     '
        '    ####    #    #   ######   #####                      #'
    ),
    (
        '#                      #         #  #    ##  ##   #          '
        '   #    #   #    #   #        #    #                     #'
    ),
    (
        '#                      #  ###   #    #   # ## #   #          '
        '   #    #   #    #   #        #    #                     #'
    ),
    (
        '#                      #    #   ######   #    #   #####      '
        '   #    #   #    #   #####    #####                      #'
    ),
    (
        '#                      #    #   #    #   #    #   #          '
        '   #    #    #  #    #        # #                        #'
    ),
    (
        '#                      #    #   #    #   #    #   #          '
        '   #    #    #  #    #        #  #                       #'
    ),
    (
        '#                       ####    #    #   #    #   ######     '
        '    ####      ##     ######   #   #                      #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                   -----------------------------------------'
        '---------------------------------------                  #'
    ),
    (
        '#                                                   Tries Lef'
        't: [tries_left]                                          #'
    ),
    (
        '#                                      YOU WERE CAUGHT BEFORE'
        ' REACHING THE EXIT!                                      #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                       [R] RESTART          '
        '           [Q] QUIT                                      #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                                BETTER LUCK '
        'NEXT TIME                                                #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#############################################################'
        '##########################################################'
    ),
]

MAP_END_SCREEN = [
    (
        '#############################################################'
        '##########################################################'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                            E S C A P E   H '
        'A B I B                                                  #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#  ----------------------------------------------------------'
        '-------------------------------------------------------  #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                       ##   ##   #######   ##     ##      ##'
        '     ##   #######   ##    ##                             #'
    ),
    (
        '#                        ## ##   ##     ##  ##     ##      ##'
        '     ##  ##     ##  ###   ##                             #'
    ),
    (
        '#                         ###    ##     ##  ##     ##      ##'
        '  #  ##  ##     ##  ####  ##                             #'
    ),
    (
        '#                         ###    ##     ##  ##     ##      ##'
        ' ### ##  ##     ##  ## ## ##                             #'
    ),
    (
        '#                         ###    ##     ##  ##     ##      ##'
        '#   ###  ##     ##  ##  ####                             #'
    ),
    (
        '#                         ###     #######    #######       ##'
        '     ##   #######   ##   ###                             #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#  ----------------------------------------------------------'
        '-------------------------------------------------------  #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                  DEGREE SECURED! YOU ESCAPE'
        'D CAMPUS ALIVE!                                          #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                               [Q] GRADUATE '
        '                                                         #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#                                        CONGRATULATIONS, GRA'
        'DUATE HABIB!                                             #'
    ),
    (
        '#                                                            '
        '                                                         #'
    ),
    (
        '#############################################################'
        '##########################################################'
    ),
]

MAP_LAYOUT_G_FLOOR = [
    (
        '#############################################################'
        '##########################################################'
    ),
    (
        '#    [Ecology W121] #   [Dig.Sys &  #                        '
        '                                                         #'
    ),
    (
        '#                   #    Ins. W114] #               [MATLAB W'
        '110]         [Physics W100]    # [Student Center]        #'
    ),
    (
        '#######   ###########               #                        '
        '                               #                         #'
    ),
    (
        '#  [Chemistry W118] #[Communications]               #########'
        '####   ###   ###############   #             #############'
    ),
    (
        '#                   #     W111]     #               # [Stair '
        '2] #   # |   # [Wellness   #   #   [OCS]     #           #'
    ),
    (
        '#######   ###########   #############               #        '
        '   #   # |   #  Center]    #   #             #           #'
    ),
    (
        '      #                                             #########'
        '####   # |   ###############   ###############           #'
    ),
    (
        '#######   ###########################   #########            '
        '       # |                     #  [Student   #   #########'
    ),
    (
        '#   [Faculty C114]  #                   #[C-109]#   #########'
        '####   # |                     #   Life]     #   # Gate2 #'
    ),
    (
        '#                   #   #############   #########   # [Facult'
        'y  #   # |   ###############   #             #   #       #'
    ),
    (
        '#######   ###########   # [Stair 9] #               #    Pod]'
        '   #   # |   #             #   ###############   #       #'
    ),
    (
        '      #   #             #############               #########'
        '####   # |   # [Reception] #   #                 #       #'
    ),
    (
        '      #####   #######                                        '
        '       ###   #             #####                 #       #'
    ),
    (
        '          #   #     #   #############   #####################'
        '########     ###############                     #       #'
    ),
    (
        '  #########   #######   # [Stair 7] #   # [Stair 8] #        '
        '                                                 #       #'
    ),
    (
        '  #                     #############   #############   #####'
        '##################################################       #'
    ),
    (
        '  #   #############                                     #[Tec'
        'h Alpha/Beta]#                                           #'
    ),
    (
        '  #   #  [E121]   #                                     #   N'
        '-425/N-426   #   #############                           #'
    ),
    (
        '  #   #############         #####################       #####'
        '##############   # [Stairs]  #                           #'
    ),
    (
        '  #                         #   [Cassim Lab]    #            '
        '                 #############                           #'
    ),
    (
        '  #                                                          '
        '                                                         #'
    ),
    (
        ' ############################################################'
        '##########################################################'
    ),
]

characters = {
    "hasnain":"#",
    "ammar":"@",
    "shaheer":"&"
}
selected = "ammar"

C109_LOOP = [
    [39, 7], [40, 7], [41, 7], [42, 7],
    [43, 7], [44, 7], [45, 7], [46, 7],
    [47, 7], [48, 7], [49, 7],
    [49, 8], [49, 9], [49, 10], [49, 11],
    [48, 11], [47, 11], [46, 11],
    [45, 11], [44, 11], [43, 11],
    [42, 11], [41, 11], [40, 11],
    [39, 11], [39, 10], [39, 9], [39, 8]
]

GATE2_LOOP = [
    [108, 17], [109, 17], [110, 17], [111, 17], [112, 17], [113, 17],
    [114, 17], [115, 17], [116, 17], [117, 17], [116, 17], [115, 17],
    [114, 17], [113, 17], [112, 17], [111, 17], [110, 17], [109, 17], [108, 17]
]

STAIR9_LOOP = [
    [23, 9], [24, 9], [25, 9], [26, 9], [27, 9], [28, 9], [29, 9], [30, 9],
    [31, 9], [32, 9], [33, 9],
    [34, 9], [35, 9], [36, 9],
    [37, 9], [37, 10], [37, 11], [37, 12],
    [37, 13], [36, 13], [35, 13], [34, 13], [33, 13], [32, 13], [31, 13],
    [30, 13], [29, 13], [28, 13], [27, 13],
    [26, 13], [25, 13], [24, 13],
    [23, 13], [23, 12], [23, 11], [23, 10]
]

STAIRS_LOOP = [
    [77, 17], [78, 17], [79, 17], [80, 17], [81, 17], [82, 17], [83, 17],
    [84, 17], [85, 17], [86, 17], [87, 17],
    [88, 17], [89, 17], [90, 17],
    [91, 17], [91, 18], [91, 19], [91, 20],
    [91, 21], [90, 21], [89, 21], [88, 21], [87, 21], [86, 21], [85, 21],
    [84, 21], [83, 21], [82, 21], [81, 21],
    [80, 21], [79, 21], [78, 21],
    [77, 21], [77, 20], [77, 19], [77, 18]
]

CASSIMLAB_LOOP = [
    [27, 18], [28, 18], [29, 18], [30, 18], [31, 18], [32, 18], [33, 18],
    [34, 18], [35, 18], [36, 18], [37, 18],
    [38, 18], [39, 18], [40, 18], [41, 18], [42, 18], [43, 18], [44, 18],
    [45, 18], [46, 18], [47, 18], [48, 18],
    [49, 18], [49, 19], [49, 20],
    [49, 21], [48, 21], [47, 21], [46, 21], [45, 21], [44, 21], [43, 21],
    [42, 21], [41, 21], [40, 21], [39, 21],
    [38, 21], [37, 21], [36, 21], [35, 21], [34, 21], [33, 21], [32, 21],
    [31, 21], [30, 21], [29, 21], [28, 21],
    [27, 21], [27, 20], [27, 19]
]

GATE2 = [[9, 112], [9, 113], [9, 114], [9, 115], [9, 116]]

def init_color():
    curses.start_color()  # Initialize curses colors first.
    curses.use_default_colors()  # Allow default terminal colors.
    # Define a foreground and background color pair.
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_GREEN)

    # Set the original map colors.
    wall_color = 174
    wall_background = 236
    path_color = 108
    # hash-color = wall color (orangish)
    curses.init_pair(4, wall_color, wall_background)
    # Set the path color.
    curses.init_pair(5, path_color, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)

def center_text_horizontally(screen, y, text, attr):
    # getting maximum terminal size which is (newin)
    height, width = screen.getmaxyx()
    if 0 < y < height - 1 and len(text) < width:  # Check that the text fits.
        # formula for making any text center horizontally
        x = (width - len(text)) // 2
        screen.addstr(y, x, text, attr)

# Game functions.
def render_map(screen):
    for y in range(len(MAP_LAYOUT_G_FLOOR)):
        row = MAP_LAYOUT_G_FLOOR[y]
        for x in range(len(row)):
            tile = row[x]
            if tile == "#":
                # Render using the current color and style.
                screen.addch(y + 1, x + 1, "#", curses.color_pair(4) |
                    curses.A_BOLD)
            elif tile == " " and x % 2 == 0:
                screen.addch(y + 1, x + 1, ".", curses.color_pair(5))
            elif tile == " " and x % 2 != 0:
                screen.addch(y + 1, x + 1, tile, curses.color_pair(5))
            elif tile == "|":
                screen.addch(y + 1, x + 1, tile, curses.color_pair(5) |
                    curses.A_BOLD)
            else:
                screen.addch(y + 1, x + 1, tile, curses.color_pair(6))

def render_player(screen, player_y, player_x):
    screen.addch(player_y + 1, player_x + 1, characters[selected],
        curses.color_pair(6) | curses.A_BOLD)

def render_teachers(screen, i, j, k, l, m):
    screen.addch(C109_LOOP[i][1] + 1, C109_LOOP[i][0] + 1, "C",
        curses.color_pair(6) | curses.A_BOLD)
    screen.addch(GATE2_LOOP[j][1] + 1, GATE2_LOOP[j][0] + 1, "C",
        curses.color_pair(6) | curses.A_BOLD)
    screen.addch(STAIR9_LOOP[k][1] + 1, STAIR9_LOOP[k][0] + 1, "C",
        curses.color_pair(6) | curses.A_BOLD)
    screen.addch(STAIRS_LOOP[l][1] + 1, STAIRS_LOOP[l][0] + 1, "C",
        curses.color_pair(6) | curses.A_BOLD)
    screen.addch(CASSIMLAB_LOOP[m][1] + 1, CASSIMLAB_LOOP[m][0] + 1, "C",
        curses.color_pair(6) | curses.A_BOLD)

def move_player(key, player_y, player_x):
    new_y, new_x = player_y, player_x
    if key == curses.KEY_UP:
        new_y -= 1
    elif key == curses.KEY_DOWN:
        new_y += 1
    elif key == curses.KEY_LEFT:
        new_x -= 1
    elif key == curses.KEY_RIGHT:
        new_x += 1
    return new_y, new_x

def is_valid_position(new_y, new_x):
    return (0 <= new_y < len(MAP_LAYOUT_G_FLOOR)
            and 0 <= new_x < len(MAP_LAYOUT_G_FLOOR[new_y]))

def check_collision(player_x, player_y, i, j, k, l, m):
    return (
        (player_x == C109_LOOP[i][0] and player_y == C109_LOOP[i][1])
        or (player_x == GATE2_LOOP[j][0] and player_y == GATE2_LOOP[j][1])
        or (player_x == STAIR9_LOOP[k][0] and player_y == STAIR9_LOOP[k][1])
        or (player_x == STAIRS_LOOP[l][0] and player_y == STAIRS_LOOP[l][1])
        or (player_x == CASSIMLAB_LOOP[m][0]
            and player_y == CASSIMLAB_LOOP[m][1])
    )


def show_game_over(screen, retries_allowed, current_attempt):
    for y in range(len(MAP_GAME_OVER)):
        row = MAP_GAME_OVER[y]
        if y == 15:
            row = row.replace("[tries_left]", str(str(retries_allowed-
                current_attempt)+"           "))
            screen.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)
        else:
            screen.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)

    screen.refresh()

def move_teachers(i, j, k, l, m):
    i = (i + 1) % len(C109_LOOP)
    j = (j + 1) % len(GATE2_LOOP)
    k = (k + 1) % len(STAIR9_LOOP)
    l = (l + 1) % len(STAIRS_LOOP)
    m = (m + 1) % len(CASSIMLAB_LOOP)
    return i, j, k, l, m

def show_win_screen(screen):
    screen.erase()
    for y in range(len(MAP_END_SCREEN)):
        row = MAP_END_SCREEN[y]
        screen.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)
    screen.refresh()

def game(screen, current_attempt):
    retries_allowed = 3
    curses.curs_set(0)  # hides the blinking cursor in the terminal
    screen.keypad(True)  # allows to press up,down,left and right special keys
    init_color()

    start_time = time.monotonic()

    # spawn location of player
    player_y = 5
    player_x = 8

    # time interval for limiting teacher movement
    teacher_move_interval = 0.10
    last_teacher_move = time.monotonic()

    # Original map width variable (retained).
    map_width = MAP_LAYOUT_G_FLOOR[0]
    high_score = []
    # starting positions for the teachers
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0

    while True:
        current_time = time.monotonic()
        screen.erase()  # Clear the screen before drawing.

        # start rendering map again for the new loop
        # map rendering logics
        render_map(screen)
        render_player(screen, player_y, player_x)
        render_teachers(screen, i, j, k, l, m)
        screen.refresh()  # Refresh the screen.

        screen.timeout(1)
        # waiting here for getting an action key
        key = screen.getch()


        # breaking if press q or Q
        if key in (ord("q"), ord("Q")):
            return []

        # player movement logic on pressing arrow keys
        new_y, new_x = move_player(key, player_y, player_x)
        if is_valid_position(new_y, new_x):
            # in the map and now check of #
            if MAP_LAYOUT_G_FLOOR[new_y][new_x] not in ("#"):
                player_y = new_y
                player_x = new_x

                # player touches gate 2
                if check_win(screen, player_x, player_y, start_time):
                    high_score.append(time.monotonic()-start_time)

                    key = screen.getch()
                    # Wait for one of the accepted keys.
                    while key not in (ord("q"), ord("Q")):
                        key = screen.getch()
                    if key in (ord("q"), ord("Q")):
                        # return works in both cases: recursive call or single
                        # call only
                        return high_score

                # Check the player against the current teacher positions.
                # collision check with the new teachers too
                if check_collision(player_x, player_y, i, j, k, l, m):
                    # Clear the screen before drawing again.
                    screen.erase()
                    if current_attempt == retries_allowed:
                        return []

                    # game over map display useing str
                    show_game_over(screen, retries_allowed, current_attempt)
                    # waiting for the input either Q for quit and R to restart
                    key = screen.getch()
                    # Wait for one of the accepted keys.
                    while key not in (ord("q"), ord("Q"), ord("r"), ord("R")):
                        key = screen.getch()

                    if key in (ord("q"), ord("Q")):
                        # return works in both cases: recursive call or single
                        # call only
                        return []
                    elif key in (ord("r"), ord("R")):
                        return game(screen, current_attempt + 1)
        # Continue the existing patrol timing.


        # looping condition for teacher
        if current_time - last_teacher_move >= teacher_move_interval:

            i, j, k, l, m = move_teachers(i, j, k, l, m)
            last_teacher_move = current_time

def check_win(screen, player_x, player_y, start_time):
    if (
        (player_x == GATE2[0][1] and player_y == GATE2[0][0])
        or (player_x == GATE2[1][1] and player_y == GATE2[1][0])
        or (player_x == GATE2[2][1] and player_y == GATE2[2][0])
        or (player_x == GATE2[3][1] and player_y == GATE2[3][0])
        or (player_x == GATE2[4][1] and player_y == GATE2[4][0])
    ):
        show_win_screen(screen)
        return True
    return False

def get_name(screen):
    screen.clear()
    height, width = screen.getmaxyx()
    attr2 = curses.color_pair(2) | curses.A_BOLD
    center_text_horizontally(screen, height // 2, "ENTER YOUR NAME: ", attr2)

    key = 0
    name = ""

    while True:
        key = screen.getch()
        if key in (curses.KEY_ENTER, 10, 13):
            break
        if len(name) > 0 and key in (curses.KEY_BACKSPACE, 127, 8):
            name = name[:-1]
        if key not in (curses.KEY_ENTER, 10, 13, curses.KEY_BACKSPACE, 127, 8):
            name += str(chr(key))
        screen.clear()
        center_text_horizontally(screen, height // 2,"ENTER YOUR NAME: " + name,
            attr2)
        screen.refresh()
    return name

def load_instruction_screen(screen):
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        screen.clear()
        height, width = screen.getmaxyx()
        screen.border()

        center_text_horizontally(screen, height // 5, 'INSTRUCTIONS', attr)
        center_text_horizontally(screen, height // 2 - 2,
            'Your goal is to avoid teachers and escape Habib', attr2)
        center_text_horizontally(screen, height // 2 - 1,
            'from either Gate 2 or Gate 4.', attr2)
        center_text_horizontally(screen, height - 4,
            'Press 5 to go back to home screen.', attr2)

        screen.refresh()
        key = screen.getch()
        if key == ord('5'):
            return

def load_home_screen(screen):
    screen.clear()

    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD
    attr3 = curses.color_pair(3) | curses.A_BOLD

    height, width = screen.getmaxyx()

    screen.border()  # gives border the code
    screen.keypad(True)  # start acceptiong special keys like arrow up, down etc

    center_text_horizontally(screen, height // 5, 'ESCAPE HABIB: BUNK', attr)
    center_text_horizontally(screen, height // 5 + 1, 'A CLASS', attr)

    menu_start = height // 2 - 3
    center_text_horizontally(screen, menu_start, '1. START GAME', attr2)
    center_text_horizontally(screen, menu_start + 1, '2. CHANGE CHARACTER',
        attr2)
    center_text_horizontally(screen, menu_start + 2, '3. INSTRUCTIONS', attr2)
    center_text_horizontally(screen, menu_start + 3, '4. HIGH SCORE', attr2)
    center_text_horizontally(screen, menu_start + 4, '5. QUIT', attr2)
    center_text_horizontally(screen, height - 4,
        'POWERED BY TMZ (The Mighty Zingers)', attr3)

    screen.refresh()

def load_character_screen(screen):
    global selected
    previous_character = selected
    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        screen.clear()
        height, width = screen.getmaxyx()
        if selected == "ammar":
            center_text_horizontally(screen, height // 3, "SELECT CHARACTER",
                attr2)
            center_text_horizontally(screen, height // 2, "(1. Ammar "+
                characters["ammar"]+")   2. Hasnain "+characters["hasnain"]+
                "   3. Shaheer "+characters["shaheer"], attr2)
            center_text_horizontally(screen, height - 3,
                'Press 1, 2 or 3 to select Character, then Press '
                'Enter to save. Press 5 to go back', attr2)
        elif selected == "hasnain":
            center_text_horizontally(screen, height // 3, "SELECT CHARACTER",
                attr2)
            center_text_horizontally(screen, height // 2, "1. Ammar "+characters
                ["ammar"]+"   (2. Hasnain "+characters["hasnain"]+
                ")   3. Shaheer "+characters["shaheer"], attr2)
            center_text_horizontally(screen, height - 3,
                'Press 1, 2 or 3 to select Character, then Press '
                'Enter to save. Press 5 to go back', attr2)
        elif selected == "shaheer":
            center_text_horizontally(screen, height // 3, "SELECT CHARACTER",
                attr2)
            center_text_horizontally(screen, height // 2, "1. Ammar "+characters
                ["ammar"]+"   2. Hasnain "+characters["hasnain"]+
                "   (3. Shaheer "+characters["shaheer"]+")", attr2)
            center_text_horizontally(screen, height - 3,
                'Press 1, 2 or 3 to select Character, then Press '
                'Enter to save. Press 5 to go back', attr2)
        screen.refresh()
        key = screen.getch()
        if key == ord("1"):
            selected = "ammar"
        elif key == ord("2"):
            selected = "hasnain"
            screen.refresh()
        elif key == ord("3"):
            selected = "shaheer"
        # 10 and13 are ascii code for enter different for mac and windows
        elif key in (curses.KEY_ENTER, 10, 13):
            return
        if key == ord("5"):
            selected = previous_character
            return

def load_high_score(screen, name, high_scores):
    screen.clear()

    attr2 = curses.color_pair(2) | curses.A_BOLD
    height, width = screen.getmaxyx()
    # Keep the heading and score lines together as a centered block.
    score_lines = max(len(high_scores), 1)
    first_line = (height - (score_lines + 1)) // 2
    screen.border()

    high_scores.sort()
    center_text_horizontally(screen, first_line, "HIGH SCORE", attr2)
    for i in range(len(high_scores)):
        center_text_horizontally(screen, first_line + i + 2, str(i+1) + ") " +
            name + " - " + str(int(high_scores[i])) + " sec", attr2)
    if len(high_scores) == 0:
        center_text_horizontally(screen, first_line + 2,
            "No high score avaliable", attr2)

    # Display the return instruction.
    center_text_horizontally(screen, height - 2,
        "Press 5 to go back to home screen.", attr2)

    screen.refresh()
    key = screen.getch()
    while key !=  ord('5'):
        key = screen.getch()
    return

def main(stdscr):
    curses.curs_set(0)  # removing blinking curosr
    init_color()  # initialize color
    stdscr.clear()  # clear screen
    stdscr.keypad(True)  # allow special characters
    screen = stdscr  # changing varaible for screen

    name = ""
    high_scores = []

    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        screen.timeout(-1)
        load_home_screen(screen)
        key = screen.getch()
        if key == ord('1'):
            if name == "":
                name = get_name(screen)
            high_scores += game(screen, 1)
        elif key == ord('2'):
            load_character_screen(screen)
        elif key == ord('3'):
            load_instruction_screen(screen)
        elif key == ord('4'):
            load_high_score(screen, name, high_scores)
        elif key == ord('5'):
            break

if __name__ == "__main__":  # Run only when executed directly.
    curses.wrapper(main)  # Start curses and call main.

