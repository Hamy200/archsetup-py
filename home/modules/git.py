import os
from shared import GIT_EMAIL
def main():
    """Module to setup git and create ssh key"""
    print("#### GIT ####")

    os.system(f"""
    git config --global user.name "HC" &&
    git config --global user.email = "{GIT_EMAIL}" &&
    ssh-keygen -t ed25519 -C "{GIT_EMAIL}" &&
    eval "$(ssh-agent -s)" &&
    ssh-add ~/.ssh/id_ed25519
    """)