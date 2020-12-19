#!/bin/bash
# THIS SCRIPT SHOULD ONLY BE USED INSIDE A VMWARE VIRTUAL MACHINE
# Mount a folder from the host machine to /mnt/hgfs

sudo vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
