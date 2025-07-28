import os
from shared import HOME_NOTCOPY
def main():
    """Zen with ArkenFox User.js"""
    ZEN_PROFILE_DIR = ""
    os.system("""
    zen-browser &
    sleep 3 && 
    killall -q zen-bin && 
    ls $HOME/.zen/
    """)
    print(" ")
    profile_name = input("Enter the profile name (look at the line above): ").strip()
    ZEN_PROFILE_DIR = f"$HOME/.zen/{profile_name}"
    os.system(f"""
    cd "$HOME/build" &&
    git clone https://github.com/arkenfox/user.js.git;
    cd user.js &&
    cp prefsCleaner.sh "{ZEN_PROFILE_DIR}/" &&
    cp updater.sh "{ZEN_PROFILE_DIR}/" &&
    cp user.js "{ZEN_PROFILE_DIR}/" &&
    cp {HOME_NOTCOPY.resolve()}/arkenfox/user-overrides.js "{ZEN_PROFILE_DIR}/user-overrides.js" &&
    cd "{ZEN_PROFILE_DIR}" &&
    printf 'y\n' | ./updater.sh &&
    printf '1\n' | ./prefsCleaner.sh 
    """)