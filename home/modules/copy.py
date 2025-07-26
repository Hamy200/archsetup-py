import os
from shared import HOME_TOCOPY, HOME

def main():
    for file in HOME_TOCOPY.iterdir():
        print(f"Copying {file}")
        os.system(f"cp -r {str(file)} {str(HOME)}")
        