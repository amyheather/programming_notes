# Git

## Create and delete repositories
When you create the repository on GitHub, be sure to include:  
* **.gitignore** - tells git which files it should ignore when run git status and upload files to git (e.g. ignoring .Rhistory when use R)  
* **LICENSE** - use open source license like MIT  
* **README.<area>md** - contains information about project, shown on front page of repository  

To clone remote repository, start in the directory where you would like to create the folder (don't start within folder with desired name, or will make the same named folder again within it!), then e.g.: `git clone https://github.com/amyheather/programming_notes.git`  
To delete repository, enter it and type: `rm -rf .git`. Then leave go up a directory and do `rm -r repofoldername`  

## Add, rename, remove, push
To check status: `git status`  
To add file: `git add filename`  
To add all files: `git add --all`  
To remove file: `git rm filename`  
To rename file: `git mv oldfilename newfilename`  
To add commit message (applies to all staged files): `git commit -m "Message"`  
To push commits to remote repo: `git push`  

## Branches and versions
To view branches (current branch marked with star): `git branch`  
To create new branch: `git branch branchname`  
When push for new branch (only on local, not yet on remote), will need to set upstream: `git push --set-upstream origin branchname`  

To switch branches: `git checkout branchname`  

To check for different between local and remote file:  
`git fetch origin branchname`  
`git diff origin/branchname -- filename`  

To merge dev branch with main branch, push, then return to dev:  
`git checkout main`  
`git merge dev`  
`git push`  
`git checkout dev`  

To move to main branch and force local files to match main (loses unstaged commits):  
*Not sure this is best way! Need to investigate more*  
`git checkout main`  
`git fetch`  
`git reset --hard origin/main`