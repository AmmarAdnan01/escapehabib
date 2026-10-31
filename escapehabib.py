import curses
import os
import time

if os.name == "nt":
    os.system("mode con: cols=180 lines=55")
MAP_GAME_OVER = [
    "#######################################################################################################################",
    "#                                                                                                                     #",
    "#                                               E S C A P E   H A B I B                                               #",
    "#                                                                                                                     #",
    "#                   --------------------------------------------------------------------------------                  #",
    "#                                                                                                                     #",
    "#                       ####      ##     #    #   ######         ####    #    #   ######   #####                      #",
    "#                      #         #  #    ##  ##   #             #    #   #    #   #        #    #                     #",
    "#                      #  ###   #    #   # ## #   #             #    #   #    #   #        #    #                     #",
    "#                      #    #   ######   #    #   #####         #    #   #    #   #####    #####                      #",
    "#                      #    #   #    #   #    #   #             #    #    #  #    #        # #                        #",
    "#                      #    #   #    #   #    #   #             #    #    #  #    #        #  #                       #",
    "#                       ####    #    #   #    #   ######         ####      ##     ######   #   #                      #",
    "#                                                                                                                     #",
    "#                   --------------------------------------------------------------------------------                  #",
    "#                                                   Tries Left: [tries_left]                                          #",
    "#                                      YOU WERE CAUGHT BEFORE REACHING THE EXIT!                                      #",
    "#                                                                                                                     #",
    "#                                       [R] RESTART                     [Q] QUIT                                      #",
    "#                                                                                                                     #",
    "#                                                BETTER LUCK NEXT TIME                                                #",
    "#                                                                                                                     #",
    "#######################################################################################################################",
]
characters = {
    "hasnain":"#",
    "ammar":"@",   
    "shaheer":"&"
}
selected = "ammar"
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
    [108, 17], [109, 17], [110, 17], [111, 17], [112, 17], [113, 17], [114, 17], [115, 17], [116, 17], [117, 17],[116, 17], [115, 17], [114, 17], [113, 17], [112, 17], [111, 17], [110, 17], [109, 17], [108, 17]
]

playercoords = []
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


def center_text_horizontally(newwin, y, text, attr):
    height, width = newwin.getmaxyx()
    if 0 < y < height - 1 and len(text) < width - 2:
        x = (width - len(text)) // 2
        newwin.addstr(y, x, text, attr)

#actual game functions
def game(newwin, currentTry):
    retries_allowed = 3
    curses.curs_set(0)
    newwin.keypad(True)
    init_color()
    attr_countdown = curses.color_pair(1) | curses.A_BOLD
    tickrate = 28

    #spawn location of player    
    player_y = 5
    player_x = 8

    #time interval for limiting teacher movement 
    interval = 0.08
    next_print_time = time.monotonic() + interval

    #map max_width
    map_width = 0
    for i in MAP_LAYOUT_G_FLOOR:
        if len(i) > map_width:
            map_width = len(i)
    i = 0
    j = 0
    while True:
        current_time = time.monotonic()
        newwin.erase()

        #current terminal max height and width
        rows, cols = newwin.getmaxyx()

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
        newwin.addch(player_y + 1, player_x + 1, characters[selected], curses.color_pair(6) | curses.A_BOLD)
        #teachers spawning
        newwin.addch(C109_LOOP[i][1] + 1, C109_LOOP[i][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)
        try:
            newwin.addch(GATE2_LOOP[j][1] + 1, GATE2_LOOP[j][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)
        except:
            pass
        newwin.refresh()

        newwin.timeout(1)
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

                #if player and teacher colliod condition checks
                if player_x == C109_LOOP[i][0] and player_y == C109_LOOP[i][1]:
                    #if yes gmae over screen display loop
                    newwin.erase()
                    if currentTry == retries_allowed:
                        return

                    #game over map display useing str
                    for y in range(len(MAP_GAME_OVER)):
                        row = MAP_GAME_OVER[y]
                        if y == 15:
                            row = row.replace("[tries_left]", str(str(retries_allowed-currentTry)+"           "))
                            newwin.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)
                        else:
                            newwin.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)


                    #waiting for the input either Q for quit and R to restart
                    key = newwin.getch()
                    #if input is some other key it will gonna stay on game over screen until you press q or r
                    while key not in (ord("q"), ord("Q"), ord("r"), ord("R")):
                        key = newwin.getch()

                    if key in (ord("q"), ord("Q")):
                        return #return works in both cases: recursive call or single call only
                    elif key in (ord("r"), ord("R")):
                        game(newwin, currentTry + 1)
                        break #after recursive call gets back it will gonna break the while loop


        #looping condition for teacher
        if current_time >= next_print_time:
            #teacher 1
            i = i + 1
            if i >= len(C109_LOOP):
                i = 0

            #teacher 2
            j = j + 1
            if j >= len(GATE2_LOOP):
                j = 0
            
            next_print_time += interval

def load_instruction_screen(newwin):
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        newwin.clear()
        height, width = newwin.getmaxyx()
        newwin.border()

        center_text_horizontally(newwin, height // 5, 'INSTRUCTIONS', attr)
        center_text_horizontally(newwin, height // 2 - 2, 'Your goal is to avoid teachers and escape Habib', attr2)
        center_text_horizontally(newwin, height // 2 - 1, 'from either Gate 2 or Gate 4.', attr2)
        center_text_horizontally(newwin, height - 4, 'Press 5 to go back to home screen.', attr2)

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

    center_text_horizontally(newwin, height // 5, 'ESCAPE HABIB: BUNK', attr)
    center_text_horizontally(newwin, height // 5 + 1, 'A CLASS', attr)

    menu_start = height // 2 - 3
    center_text_horizontally(newwin, menu_start, '1. START GAME', attr2)
    center_text_horizontally(newwin, menu_start + 1, '2. CHANGE CHARACTER', attr2)
    center_text_horizontally(newwin, menu_start + 2, '3. INSTRUCTIONS', attr2)
    center_text_horizontally(newwin, menu_start + 3, '4. HIGH SCORE', attr2)
    center_text_horizontally(newwin, menu_start + 4, '5. QUIT', attr2)
    center_text_horizontally(newwin, height - 4, 'POWERED BY TMZ (The Mighty Zingers)', attr3)

    newwin.refresh()

def load_character_screen(newwin):
    global selected
    originallyselected = selected
    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        newwin.clear()
        height, width = newwin.getmaxyx()
        if selected == "ammar":
            center_text_horizontally(newwin, height // 3, "SELECT CHARACTER", attr2)
            center_text_horizontally(newwin, height // 2, "(1. Ammar "+characters["ammar"]+")   2. Hasnain "+characters["hasnain"]+"   3. Shaheer "+characters["shaheer"], attr2)
            center_text_horizontally(newwin, height - 3, "Press 1, 2 or 3 to select Character, then Press Enter to save. Press 5 to go back", attr2)
        elif selected == "hasnain":
            center_text_horizontally(newwin, height // 3, "SELECT CHARACTER", attr2)
            center_text_horizontally(newwin, height // 2, "1. Ammar "+characters["ammar"]+"   (2. Hasnain "+characters["hasnain"]+")   3. Shaheer "+characters["shaheer"], attr2)
            center_text_horizontally(newwin, height - 3, "Press 1, 2 or 3 to select Character, then Press Enter to save. Press 5 to go back", attr2)
        elif selected == "shaheer":
            center_text_horizontally(newwin, height // 3, "SELECT CHARACTER", attr2)
            center_text_horizontally(newwin, height // 2, "1. Ammar "+characters["ammar"]+"   2. Hasnain "+characters["hasnain"]+"   (3. Shaheer "+characters["shaheer"]+")", attr2)
            center_text_horizontally(newwin, height - 3, "Press 1, 2 or 3 to select Character, then Press Enter to save. Press 5 to go back", attr2)
        newwin.refresh()
        key = newwin.getch()
        if key == ord("1"):
            selected = "ammar"
        elif key == ord("2"):
            selected = "hasnain"
            newwin.refresh()
        elif key == ord("3"):
            selected = "shaheer"
        elif key in (curses.KEY_ENTER, 10, 13):
            return

            
        
        if key == ord("5"):
            selected = originallyselected
            return
    
    

def main(stdscr):
    curses.curs_set(0)
    init_color()
    stdscr.clear()
    stdscr.keypad(True)
    newwin = stdscr

    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        load_home_screen(newwin)
        newwin.timeout(-1)
        key = newwin.getch()

        if key == ord('1'):
            game(newwin, 1)
        elif key == ord('2'):
            load_character_screen(newwin)
        elif key == ord('3'):
            load_instruction_screen(newwin)
        elif key == ord('4'):
            newwin.clear()
            height, width = newwin.getmaxyx()
            newwin.border()
            center_text_horizontally(newwin, height // 2,
                        "HIGH SCORE", attr2)
        elif key == ord('5'):
            break


if __name__ == "__main__":
    curses.wrapper(main)