from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.github.com")
driver.set_window_size(1500, 1000)

# read json
with open('./infos.json') as credentialsJson:
    infos       = json.load(credentialsJson)
    username    = infos["username"]
    password    = infos["password"]
    repo_name   = infos["repo_name"]
    # repo_name must not end with an '/' character
    if repo_name[len(repo_name)-1] == '/':
        repo_name   = repo_name[:len(repo_name)-1] 
    description = infos["description"]
    is_private  = infos["is_private"]
    repo_path   = infos["repo_path"]


# go to sign in screen
go_to_sign_in_button = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
go_to_sign_in_button.click()

username_input_element = driver.find_element_by_xpath('//*[@id="login_field"]')
password_input_element = driver.find_element_by_xpath('//*[@id="password"]')
sign_in_button         = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

username_input_element.send_keys(username)
password_input_element.send_keys(password)
sign_in_button.click()

# go to new repo window
new_repo_button = driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a")
new_repo_button.click()

# enter repo infos and create repo
repo_name_input_element = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name_input_element.send_keys(repo_name)

description_input_element = driver.find_element_by_xpath('//*[@id="repository_description"]')
description_input_element.send_keys(description)

if is_private:
    is_private_checkbox_element = driver.find_element_by_xpath('//*[@id="repository_visibility_private"]')
    is_private_checkbox_element.click()

time.sleep(1.5)
create_repo_button = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
create_repo_button.click()


# repo is now created, execute git commands to init repo locally
command = 'mkdir -p %s/%s && cd %s/%s && echo "# TEST" >> README.md && git init && git add README.md && git commit -m "first commit" && git remote add origin https://github.com/%s/%s.git && git push -u origin master' % (
    repo_path,
    repo_name,
    repo_path, 
    repo_name, 
    username,
    repo_name)

os.system(command)

# close browser
driver.close()