import os 
PKGS = [
    "hyprland",
    "git",
    "neovim",
    "kitty",
    "nemo",
    "waybar",
    "rofi",
    "ttf-nerd-fonts-symbols",
    "ttf-jetbrains-mono-nerd",
    "fastfetch",
    "pavucontrol",
    "noto-fonts-cjk",
    "hyprsunset",
    "mpv",
    "zsh",
    "fzf",
    "zsh-autosuggestions",
    "zsh-syntax-highlighting"


]


def main():
    """Module to install pacman pkgs"""
    pkg_string = ""
    for pkg in PKGS:
        #Create the string separated by a space
        pkg_string += pkg + " "
    
    os.system(f"yes | sudo pacman -Sy {pkg_string}")
