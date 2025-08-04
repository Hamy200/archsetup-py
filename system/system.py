from shared import ModuleStore

MODULES = [
    "boot",
    #"automount"
    "copy"

    ]

def main():
    """
    The base system module to execute submodules
    Allows for easily removing and adding modules when wanted
    """
    mod_store = ModuleStore("system.modules", MODULES)

    for mod in mod_store.modules:
        mod.main()


if __name__ == "__main__":
    main()