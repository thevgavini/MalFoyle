#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root." 
   exit 1
fi

rm /usr/local/bin/malfoyle.py
rm /usr/local/bin/malfoyle
echo "Malfoyle CLI tool has been uninstalled."
