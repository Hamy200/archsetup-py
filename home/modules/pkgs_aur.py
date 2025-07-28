import os 
PKGS = [
    "vscodium-bin",
    "zen-browser-bin",
    "anki-bin"

    

]


def main():
    """Modules to install AUR packages using paru"""
    pkg_string = ""
    for pkg in PKGS:
        #Create the string separated by a space
        pkg_string += pkg + " "
    
    os.system(f"yes | paru -S {pkg_string} --skipreview")
