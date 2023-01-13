from os.path import isdir
from os import system


def pre():
    # install dependencies if it isn't already
    if not isdir("node_modules"):
        system("npm install")


def run():
    system("npm run start")
