# Automatic-Repo-Creator

A Python 2.7 based command line tool that initializes a repository remotely on your Github account and locally on your Ubuntu machine.

### Installing / Getting started

Clone or download the project.

Run the setup file
```
./setup
```
This will:
- install python 2.7 and pip
- install selenium using pip (a python library for automated browser interaction)
- copy the main script and the browser driver executable into ```/usr/local/bin```

From now on you can type  ```createrepo``` in your terminal to call the main script.
It will ask you for your:
- Github name
- Github password
- Repo name
- Repo path
- private or public?

Then, it will start Chrome, login with your credentials and create the repository for you.
Locally it will initialize the repository at the right location.

### Prerequisites
At the moment this Project uses Chrome.
