import os
def main():
    """Set GTK settings"""
    os.system("""
    gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark" &&
    gsettings set org.cinnamon.desktop.default-applications.terminal exec kitty
    """)