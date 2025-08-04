import os
from shared import SYSTEM_TOCOPY

def main():
    """
    Copy system files, starting at the root
    BEWWARE, potentially dangerous
    """
    for file in SYSTEM_TOCOPY.iterdir():
        print(f"Copying {file}")
        os.system(f"sudo cp -r {str(file)} /")
        