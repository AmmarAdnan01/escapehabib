import curses
import os
import time

if os.name == "nt": #check wheather the system/os is windows or not
    os.system("mode con: cols=180 lines=55") #set the terminal to this size
    
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

MAP_END_SCREEN = [
    "#######################################################################################################################",
    "#                                                                                                                     #",
    "#                                            E S C A P E   H A B I B                                                  #",
    "#                                                                                                                     #",
    "#  -----------------------------------------------------------------------------------------------------------------  #",
    "#                                                                                                                     #",
    "#                       ##   ##   #######   ##     ##      ##     ##   #######   ##    ##                             #",
    "#                        ## ##   ##     ##  ##     ##      ##     ##  ##     ##  ###   ##                             #",
    "#                         ###    ##     ##  ##     ##      ##  #  ##  ##     ##  ####  ##                             #",
    "#                         ###    ##     ##  ##     ##      ## ### ##  ##     ##  ## ## ##                             #",
    "#                         ###    ##     ##  ##     ##      ###   ###  ##     ##  ##  ####                             #",
    "#                         ###     #######    #######       ##     ##   #######   ##   ###                             #",
    "#                                                                                                                     #",
    "#  -----------------------------------------------------------------------------------------------------------------  #",
    "#                                                                                                                     #",
    "#                                  DEGREE SECURED! YOU ESCAPED CAMPUS ALIVE!                                          #",
    "#                                                                                                                     #",
    "#                                               [Q] GRADUATE                                                          #",
    "#                                                                                                                     #",
    "#                                        CONGRATULATIONS, GRADUATE HABIB!                                             #",
    "#                                                                                                                     #",
    "#######################################################################################################################",
]

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
    "#   [Faculty C114]  #                   #[C-109]#   #############   # |                     #   Life]     #   # Gate2 #",
    "#                   #   #############   #########   # [Faculty  #   # |   ###############   #             #   #       #",
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
    [108, 17], [109, 17], [110, 17], [111, 17], [112, 17], [113, 17], [114, 17], [115, 17], [116, 17], [117, 17],[116, 17], [115, 17], [114, 17], [113, 17], [112, 17], [111, 17], [110, 17], [109, 17], [108, 17]
]

STAIR9_LOOP = [
    [23, 9], [24, 9], [25, 9], [26, 9], [27, 9], [28, 9], [29, 9], [30, 9], [31, 9], [32, 9], [33, 9],
    [34, 9], [35, 9], [36, 9],
    [37, 9], [37, 10], [37, 11], [37, 12],
    [37, 13], [36, 13], [35, 13], [34, 13], [33, 13], [32, 13], [31, 13], [30, 13], [29, 13], [28, 13], [27, 13],
    [26, 13], [25, 13], [24, 13],
    [23, 13], [23, 12], [23, 11], [23, 10]
]

STAIRS_LOOP = [
    [77, 17], [78, 17], [79, 17], [80, 17], [81, 17], [82, 17], [83, 17], [84, 17], [85, 17], [86, 17], [87, 17],
    [88, 17], [89, 17], [90, 17],
    [91, 17], [91, 18], [91, 19], [91, 20],
    [91, 21], [90, 21], [89, 21], [88, 21], [87, 21], [86, 21], [85, 21], [84, 21], [83, 21], [82, 21], [81, 21],
    [80, 21], [79, 21], [78, 21],
    [77, 21], [77, 20], [77, 19], [77, 18]
]

CASSIMLAB_LOOP = [
    [27, 18], [28, 18], [29, 18], [30, 18], [31, 18], [32, 18], [33, 18], [34, 18], [35, 18], [36, 18], [37, 18],
    [38, 18], [39, 18], [40, 18], [41, 18], [42, 18], [43, 18], [44, 18], [45, 18], [46, 18], [47, 18], [48, 18],
    [49, 18], [49, 19], [49, 20],
    [49, 21], [48, 21], [47, 21], [46, 21], [45, 21], [44, 21], [43, 21], [42, 21], [41, 21], [40, 21], [39, 21],
    [38, 21], [37, 21], [36, 21], [35, 21], [34, 21], [33, 21], [32, 21], [31, 21], [30, 21], [29, 21], [28, 21],
    [27, 21], [27, 20], [27, 19]
]

GATE2 = [[9, 112], [9, 113], [9, 114], [9, 115], [9, 116]]

def init_color():
    curses.start_color() #use before initializing colors
    curses.use_default_colors() #allow to use default terminal colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK) #built in function, takes three parameters pair_number, text color and bg color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_GREEN)

    #color initializing for map rendering specficially
    wall_color = 174 
    wall_background = 236
    path_color = 108
    curses.init_pair(4, wall_color, wall_background) # hash-color = wall color (orangish)
    curses.init_pair(5, path_color, curses.COLOR_BLACK) # dots on the path uska color hai ye
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK) 

def center_text_horizontally(newwin, y, text, attr):
    height, width = newwin.getmaxyx() # getting maximum terminal size which is (newin)
    if 0 < y < height - 1 and len(text) < width: #safety check if text is out of window - height - 1 for safety of boarders
        x = (width - len(text)) // 2 #formula for making any text center horizontally
        newwin.addstr(y, x, text, attr)

#actual game functions
def game(newwin, currentTry):
    retries_allowed = 3
    curses.curs_set(0) #hides the blinking cursor in the terminal
    newwin.keypad(True) #allows to press up,down,left and right special keys
    init_color()

    start_time = time.monotonic()

    #spawn location of player    
    player_y = 5
    player_x = 8

    #time interval for limiting teacher movement 
    interval = 0.10
    last_teacher_move = time.monotonic()

    #map max_width
    map_width = MAP_LAYOUT_G_FLOOR[0]
    high_score = []
    #starting positions for the teachers
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0

    while True:
        current_time = time.monotonic()
        newwin.erase() #remove all the prev loop rendering from memory and re-render next time only what changes

        #start rendering map again for the new loop
        #map rendering logics
        for y in range(len(MAP_LAYOUT_G_FLOOR)):
            row = MAP_LAYOUT_G_FLOOR[y]
            for x in range(len(row)):
                char = row[x]
                if char == "#":
                    newwin.addch(y + 1, x + 1, "#", curses.color_pair(4) | curses.A_BOLD) # | bitwise helps to give two styles to a charater, else curses me aek hi de sakte ho
                elif char == " " and x % 2 == 0:
                    newwin.addch(y + 1, x + 1, ".", curses.color_pair(5))
                elif char == " " and x % 2 != 0:
                    newwin.addch(y + 1, x + 1, char, curses.color_pair(5))
                elif char == "|":
                    newwin.addch(y + 1, x + 1, char, curses.color_pair(5) | curses.A_BOLD)
                else:
                    newwin.addch(y + 1, x + 1, char, curses.color_pair(6))

        #actual spawning player
        newwin.addch(player_y + 1, player_x + 1, characters[selected], curses.color_pair(6) | curses.A_BOLD)

        #teachers spawning
        newwin.addch(C109_LOOP[i][1] + 1, C109_LOOP[i][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)
        newwin.addch(GATE2_LOOP[j][1] + 1, GATE2_LOOP[j][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)
        newwin.addch(STAIR9_LOOP[k][1] + 1, STAIR9_LOOP[k][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)
        newwin.addch(STAIRS_LOOP[l][1] + 1, STAIRS_LOOP[l][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)
        newwin.addch(CASSIMLAB_LOOP[m][1] + 1, CASSIMLAB_LOOP[m][0] + 1, "C", curses.color_pair(6) | curses.A_BOLD)

        newwin.refresh() #curses sab dimag me karta hai so to show all those changes we use refreash

        newwin.timeout(1)
        #waiting here for getting an action key
        key = newwin.getch()

    
        #breaking if press q or Q
        if key in (ord("q"), ord("Q")):
            return []

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
        if 0 <= new_y < len(MAP_LAYOUT_G_FLOOR) and 0 <= new_x < len(MAP_LAYOUT_G_FLOOR[new_y]): #checking if the charater is in the map or not
            if MAP_LAYOUT_G_FLOOR[new_y][new_x] not in ("#"): #in the map and now check of #
                player_y = new_y
                player_x = new_x

                #player touches gate 2 
                if check_win(newwin, player_x, player_y, start_time):
                    high_score.append(time.monotonic()-start_time)

                    key = newwin.getch()
                    #if input is some other key it will gonna stay on game over screen until you press q or r
                    while key not in (ord("q"), ord("Q")):
                        key = newwin.getch()
                    if key in (ord("q"), ord("Q")):
                        return high_score #return works in both cases: recursive call or single call only
            
                #if player and teacher colliod condition checks
                #collision check with the new teachers too
                if (player_x == C109_LOOP[i][0] and player_y == C109_LOOP[i][1]) or (player_x == GATE2_LOOP[j][0] and player_y == GATE2_LOOP[j][1]) or (player_x == STAIR9_LOOP[k][0] and player_y == STAIR9_LOOP[k][1]) or (player_x == STAIRS_LOOP[l][0] and player_y == STAIRS_LOOP[l][1]) or (player_x == CASSIMLAB_LOOP[m][0] and player_y == CASSIMLAB_LOOP[m][1]):
                    #if yes gmae over screen display loop
                    newwin.erase()
                    if currentTry == retries_allowed:
                        return []

                    #game over map display useing str
                    for y in range(len(MAP_GAME_OVER)):
                        row = MAP_GAME_OVER[y]
                        if y == 15:
                            row = row.replace("[tries_left]", str(str(retries_allowed-currentTry)+"           "))
                            newwin.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)
                        else:
                            newwin.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)

                    newwin.refresh()
                    #waiting for the input either Q for quit and R to restart
                    key = newwin.getch()
                    #if input is some other key it will gonna stay on game over screen until you press q or r
                    while key not in (ord("q"), ord("Q"), ord("r"), ord("R")):
                        key = newwin.getch()

                    if key in (ord("q"), ord("Q")):
                        return [] #return works in both cases: recursive call or single call only
                    elif key in (ord("r"), ord("R")):
                        return game(newwin, currentTry + 1)
                        #after recursive call gets back it will gonna break the while loop


        #looping condition for teacher
        if current_time - last_teacher_move >= interval:

            i = (i + 1) % len(C109_LOOP)
            j = (j + 1) % len(GATE2_LOOP)
            k = (k + 1) % len(STAIR9_LOOP)
            l = (l + 1) % len(STAIRS_LOOP)
            m = (m + 1) % len(CASSIMLAB_LOOP)

            last_teacher_move = current_time

def check_win(newwin, player_x, player_y, start_time):
    if (player_x == GATE2[0][1] and player_y == GATE2[0][0]) or (player_x == GATE2[1][1] and player_y == GATE2[1][0]) or (player_x == GATE2[2][1] and player_y == GATE2[2][0]) or (player_x == GATE2[3][1] and player_y == GATE2[3][0]) or (player_x == GATE2[4][1] and player_y == GATE2[4][0]):      
        newwin.erase()
        for y in range(len(MAP_END_SCREEN)):
            row = MAP_END_SCREEN[y]
            newwin.addstr(y + 1, 1, row, curses.color_pair(4) | curses.A_BOLD)
        newwin.refresh()
        return True
    return False

def get_name(newwin):
    newwin.clear()
    height, width = newwin.getmaxyx()
    attr2 = curses.color_pair(2) | curses.A_BOLD
    center_text_horizontally(newwin, height // 2, "ENTER YOUR NAME: ", attr2)

    key = 0
    name = ""
    
    while True:
        key = newwin.getch()
        if key in (curses.KEY_ENTER, 10, 13):
            break
        if len(name) > 0 and key in (curses.KEY_BACKSPACE, 127, 8):
            name = name[:-1]
        if key not in (curses.KEY_ENTER, 10, 13, curses.KEY_BACKSPACE, 127, 8):
            name += str(chr(key))
        newwin.clear()
        center_text_horizontally(newwin, height // 2,"ENTER YOUR NAME: " + name, attr2)
        newwin.refresh()
    return name

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

    newwin.border() #gives border the code
    newwin.keypad(True) #start acceptiong special keys like arrow up, down etc

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
        elif key in (curses.KEY_ENTER, 10, 13): #10 and13 are ascii code for enter different for mac and windows
            return 
        if key == ord("5"):
            selected = originallyselected
            return
    
def load_high_score(newwin, name, time):
    newwin.clear()

    attr2 = curses.color_pair(2) | curses.A_BOLD
    height, width = newwin.getmaxyx()
    # Keep the heading and score lines together as a centered block.
    score_lines = max(len(time), 1)
    first_line = (height - (score_lines + 1)) // 2
    newwin.border()

    time.sort()
    center_text_horizontally(newwin, first_line, "HIGH SCORE", attr2)
    for i in range(len(time)):
        center_text_horizontally(newwin, first_line + i + 2, str(i+1) + ") " + name + " - " + str(int(time[i])) + " sec", attr2)
    if len(time) == 0:
        center_text_horizontally(newwin, first_line + 2, "No high score avaliable", attr2)

    # Keep the return instruction centered near the bottom of the screen.
    center_text_horizontally(newwin, height - 2, "Press 5 to go back to home screen.", attr2)

    newwin.refresh()
    key = newwin.getch()
    while key !=  ord('5'):
        key = newwin.getch()
    return 

def main(stdscr):
    curses.curs_set(0) #removing blinking curosr
    init_color() #initialize color 
    stdscr.clear() #clear screen
    stdscr.keypad(True) #allow special characters
    newwin = stdscr #changing varaible for screen

    name = ""
    time = []

    attr2 = curses.color_pair(2) | curses.A_BOLD

    while True:
        load_home_screen(newwin)
        key = newwin.getch()
        if key == ord('1'):
            if name == "":
                name = get_name(newwin)
            time += game(newwin, 1)
        elif key == ord('2'):
            load_character_screen(newwin)
        elif key == ord('3'):
            load_instruction_screen(newwin)
        elif key == ord('4'):
            load_high_score(newwin, name, time)
        elif key == ord('5'):
            break

if __name__ == "__main__": #checks wheather the file is running directly or getting improted to some other file
    curses.wrapper(main) #wrapper function takes main as argument and then usko khud apne function ke andr se call karta with a screen which is ready to get keyboard inputs

