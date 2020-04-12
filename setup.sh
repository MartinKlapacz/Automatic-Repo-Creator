#!/bin/bash

# python, package manager and package installation
sudo apt install python
sudo apt install python-pip
pip install selenium

# make file executable
chmod +x createrepo

# move files 
sudo cp createrepo /usr/local/bin
sudo cp chromedriver /usr/local/bin
# export PATH=$PATH:/usr/local/bin/chromedriver
# source ~/.profile 