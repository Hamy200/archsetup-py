import os
def main():
    """Module for setting up yazi with plugins and themes"""
    os.system("""
    ya pkg add yazi-rs/plugins:mount &&
    ya pkg add bennyyip/gruvbox-dark &&
    ya pkg install
    """)