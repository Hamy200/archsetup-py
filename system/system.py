from shared import ModuleStore

MODULES = ["boot"]

def main():
    mod_store = ModuleStore("system.modules", MODULES)

    for mod in mod_store.modules:
        mod.main()


if __name__ == "__main__":
    main()