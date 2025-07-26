import os 
PKGS = [
    "vscodium-bin",
    "zen-browser-bin",

    

]


def main():
    pkg_string = ""
    for pkg in PKGS:
        #Create the string separated by a space
        pkg_string += pkg + " "
    
    os.system(f"paru -S {pkg_string} --skipreview")
