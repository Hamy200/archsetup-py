import os 
PKGS = [
    "hyprland",
    "git",
    "neovim"

]


def main():
    pkg_string = ""
    for pkg in PKGS:
        #Create the string separated by a space
        pkg_string += pkg + " "
    print(pkg_string)
    os.system(f"sudo pacman -Sy {pkg_string}")
