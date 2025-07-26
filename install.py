import home.home
import system.system
import sys


def main():
    if len(sys.argv) > 1:
        top_module = sys.argv[1]
        if top_module == "home":
            home.home.main()
        elif top_module == "system":
            system.system.main()   
    else:
        home.home.main()
        system.system.main()   

if __name__ == "__main__":
    main()