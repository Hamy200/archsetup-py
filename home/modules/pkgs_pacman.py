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
    "zsh-syntax-highlighting",
    "ntfs-3g",
    "python-requests", #for the prayer time waybar module
    "yazi",
    "liquidctl",
    "fcitx5",
    "openvpn",
    "openresolv",
    "hyprshot"

]


def main():
    """Module to install pacman pkgs"""
    print("#### PACMAN PKGS ####")

    pkg_string = ""
    for pkg in PKGS:
        #Create the string separated by a space
        pkg_string += pkg + " "
    
    os.system(f"yes | sudo pacman -Sy {pkg_string}")
