from datetime import datetime

from colorama import Fore as Foreground, init


def critical(message):
    init(autoreset=True)
    print(Foreground.MAGENTA, "[" + str(datetime.now()) + "] " + message, flush=True)


def error(message):
    init(autoreset=True)
    print(Foreground.RED, "[" + str(datetime.now()) + "] " + message, flush=True)


def warning(message):
    init(autoreset=True)
    print(Foreground.YELLOW, "[" + str(datetime.now()) + "] " + message, flush=True)


def info(message):
    print("[" + str(datetime.now()) + "] " + message, flush=True)
