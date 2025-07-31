import os
def main():
    """
    This module edits the fstab to auto mount Hamza HDD
    Potentially Dangerous!!
    """
    os.system(""" 
    sudo su -c "echo 'LABEL=Hamza\040HDD  /media/Hamza\040HDD  ntfs  defaults,nofail  0  2' >> /etc/fstab"  &&
    findmnt --verify --verbose &&
    sudo systemctl daemon-reload"
    """)
    
        




#Backup FStab
"""
# Static information about the filesystems.
# See fstab(5) for details.

# <file system> <dir> <type> <options> <dump> <pass>
# /dev/mapper/root
UUID=d87144ba-d7e4-49ac-b4d3-6711272096f3	/         	ext4      	rw,relatime	0 1

# /dev/nvme0n1p5
UUID=4FA7-6D79      	/boot     	vfat      	rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro	0 2

LABEL=Hamza\040HDD      /media/Hamza\040HDD  ntfs  defaults,nofail 0 2
"""