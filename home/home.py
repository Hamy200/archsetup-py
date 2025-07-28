from shared import ModuleStore
import os

MODULES = [
    #"pkgs_pacman",
    # "copy",
    #"paru",
    # "pkgs_aur",
    # "zsh",
    #"git",
    # "gtk",
    "browser"

]

def main():
    """
    The base home module to execute submodules
    Allows for easily removing and adding modules when wanted
    """
    os.system("mkdir ~/build")
    mod_store = ModuleStore("home.modules", MODULES)

    for mod in mod_store.modules:
        mod.main()


if __name__ == "__main__":
    main()
