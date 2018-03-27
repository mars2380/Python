Command line instructions

Git global setup
git config --global user.name "Alessandro Di Micoli"
git config --global user.email "adimicoli@gmail.com"

Create a new repository
git clone https://gitlab.com/adimicoli/Python.git
cd Python
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Existing folder
cd existing_folder
git init
git remote add origin https://gitlab.com/adimicoli/Python.git
git add .
git commit -m "Initial commit"
git push -u origin master

Existing Git repository
cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.com/adimicoli/Python.git
git push -u origin --all
git push -u origin --tags


This is a push test to my Github