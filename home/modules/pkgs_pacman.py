import os 
PKGS = [
    "hyprland",
    "git",
    "neovim",
    "kitty",
    "nemo",
    "waybar",
    "rofi",
    "firefox",
    

]


def main():
    pkg_string = ""
    for pkg in PKGS:
        #Create the string separated by a space
        pkg_string += pkg + " "
    
    os.system(f"sudo pacman -Sy {pkg_string}")
