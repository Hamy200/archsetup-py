import os 


def main():
    os.system("""
    rm -r ~/build && mkdir ~/build && cd ~/build && sudo pacman -S --needed base-devel && git clone https://aur.archlinux.org/paru.git && cd paru && makepkg -si
    """)