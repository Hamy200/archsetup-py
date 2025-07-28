import os 


def main():
    """
    Module to install Paru
    """
    os.system("""
    mkdir ~/build && 
    cd ~/build && 
    sudo pacman -S --needed base-devel && 
    git clone https://aur.archlinux.org/paru.git && 
    cd paru && 
    makepkg -si && 
    cd ~ && 
    rm -rf ~/build
    """)
