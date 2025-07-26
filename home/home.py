from shared import ModuleStore

MODULES = [
    "pkgs_pacman",
    "copy",
    "paru",
    "pkgs_aur"
]

def main():
    mod_store = ModuleStore("home.modules", MODULES)

    for mod in mod_store.modules:
        mod.main()


if __name__ == "__main__":
    main()