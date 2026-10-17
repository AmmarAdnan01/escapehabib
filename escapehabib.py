import curses 


def load_instruction_screen(newwin):
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD
    attr3 = curses.color_pair(3) | curses.A_BOLD
    newwin.clear()
    newwin.addstr(5, 32, 'INSTRUCTIONS', attr)
    newwin.addstr(10, 20, 'Your goal is to avoid teachers and escape habib ', attr2)
    newwin.addstr(11, 20, 'from either Gate 2 or Gate 4.', attr2)
    newwin.addstr(20, 25, 'Press 5 to go back to home screen.', attr2)
    newwin.border()
    while True:
        key = newwin.getch()
        if key == ord('5'):
            load_home_screen(newwin)
            break


    
def load_home_screen(newwin):
    newwin.clear()
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD
    attr3 = curses.color_pair(3) | curses.A_BOLD
    newwin.border()
    newwin.keypad(True)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_GREEN)
    newwin.addstr(5, 32, 'ESCAPE HABIB: BUNK', attr)
    newwin.addstr(6, 37, 'A CLASS', attr)
    newwin.addstr(10, 32, '1. START GAME', attr2)
    newwin.addstr(11, 32, '2. CHANGE CHARACTER', attr2)
    newwin.addstr(12, 32, '3. INSTRUCTIONS', attr2)
    newwin.addstr(13, 32, '4. HIGH SCORE', attr2)
    newwin.addstr(14, 32, '5. QUIT', attr2)
    newwin.addstr(20, 25, 'POWERED BY TMZ (The Mighty Zingers)', attr3)
    curses.curs_set(0)

def main(stdscr):
    stdscr.clear()
    sh = 25
    sw = 90

    newwin = curses.newwin(sh + 1, sw + 1, 0, 0)
    attr = curses.color_pair(1) | curses.A_BOLD
    attr2 = curses.color_pair(2) | curses.A_BOLD
    attr3 = curses.color_pair(3) | curses.A_BOLD
    load_home_screen(newwin)
    while True:
        key = newwin.getch()
        if key == ord('1'):
            newwin.clear()
            newwin.addstr(11, 32, "1", attr2)
            newwin.border()
        elif key == ord('2'):
            newwin.clear()
            newwin.addstr(11, 32, "2", attr2)
            newwin.border()
        elif key == ord('3'):
            load_instruction_screen(newwin)
        elif key == ord('4'):
            newwin.clear()
            newwin.addstr(11, 32, "4", attr2)
            newwin.border()




curses.wrapper(main)
