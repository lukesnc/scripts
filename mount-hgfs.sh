#!/bin/bash
# THIS SCRIPT SHOULD ONLY BE USED INSIDE A VIRTUAL MACHINE
# Mount a folder from the host machine to /mnt/hgfs
# Only works with VMWare

sudo vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
