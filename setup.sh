#!/bin/bash

# python, package manager and package installation
sudo apt install python
sudo apt install python-pip
pip install selenium --user

# make file executable
chmod +x createrepo

# move main script and chromedriver executable to $PATH location
sudo cp createrepo /usr/local/bin
sudo cp chromedriver /usr/local/bin