import colorama
from colorama import Fore, Back, Style

class consol():
    colorama.init()

    def logotip():
        trello_log1 = ("""▀▀█▀▀ █▀▀█ █▀▀ █░░ █░░ █▀▀█  ▀▀█▀▀ █▀▀ █░░ █▀▀ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█""")
        trello_log2 = ("""░▒█░░ █▄▄▀ █▀▀ █░░ █░░ █░░█  ░▒█░░ █▀▀ █░░ █▀▀ █░▀█ █▄▄▀ █▄▄█ █░▀░█""")
        trello_log3 = ("""░▒█░░ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀  ░▒█░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀░░▀ ▀░░░▀""")

        print ("\n",
                "\033[33m\033[34m\033[40m{}\033[0m\n".format(trello_log1),
                "\033[33m\033[37m\033[40m{}\033[0m\n".format(trello_log2),
                "\033[33m\033[32m\033[40m{}\033[0m\n".format(trello_log3))
        print(Fore.WHITE)

    def GREEN(text=""):
        print(Fore.GREEN,text)

    def RED(text=""):
        print(Fore.RED,text)

    def WHITE(text=""):
        print(Fore.WHITE,text)

    def BLACK(text=""):
        print(Fore.BLACK,text)

    def BLUE(text=""):
        print(Fore.BLUE,text)

    def CYAN(text=""):
        print(Fore.CYAN,text)

    def MAGENTA(text=""):
        print(Fore.MAGENTA,text)

    def YELLOW(text=""):
        print(Fore.YELLOW,text)

    def RESET(text=""):
        print(Fore.RESET,text)

    def ERROR(text=""):
        print(Fore.RED,text)
        print(Fore.WHITE)