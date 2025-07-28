from shared import ModuleStore

MODULES = [
    #"pkgs_pacman",
    "copy",
    #"paru",
    # "pkgs_aur",
    # "zsh",
    #"git",
    "gtk",

]

def main():
    """
    The base home module to execute submodules
    Allows for easily removing and adding modules when wanted
    """
    mod_store = ModuleStore("home.modules", MODULES)

    for mod in mod_store.modules:
        mod.main()


if __name__ == "__main__":
    main()
