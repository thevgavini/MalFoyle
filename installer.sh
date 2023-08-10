#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root." 
   exit 1
fi
pip3 install -r requirements.txt
chmod +x malfoyle.py
cp malfoyle.py /usr/local/bin/
ln -s /usr/local/bin/malfoyle.py /usr/local/bin/malfoyle
echo "Malfoyle CLI tool has been installed."
