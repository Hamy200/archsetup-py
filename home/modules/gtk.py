import os
def main():
    """Set GTK theme settings"""
    os.system("""gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark" """)