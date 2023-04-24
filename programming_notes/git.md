# Git

## Storing credentials  
The `credential.helper cache` value tells Git to keep your password cached in memory for a particular amount of minutes. The default is 15 minutes, you can set a longer timeout with:
```
# Cache for 1 hour
git config --global credential.helper "cache --timeout=3600"

# Cache for 1 day
git config --global credential.helper "cache --timeout=86400"

# Cache for 1 week
git config --global credential.helper "cache --timeout=604800"
```  

## Create and delete repositories
When you create the repository on GitHub, be sure to include:  
* **.gitignore** - tells git which files it should ignore when run git status and upload files to git (e.g. ignoring .Rhistory when use R)  
* **LICENSE** - use open source license like MIT  
* **README.<area>md** - contains information about project, shown on front page of repository  

To clone remote repository, start in the directory where you would like to create the folder (don't start within folder with desired name, or will make the same named folder again within it!), then e.g.: `git clone https://github.com/amyheather/programming_notes.git`  
To delete repository, enter it and type: `rm -rf .git`. Then leave go up a directory and do `rm -r repofoldername`  

To add local repository to remote:  
* Set up local repository, making it use git, `git init -b main`  
* Add and commit something  
* Create empty repo on GitHub account  
* `git remote add origin https://github.com/amyheather/package_test.git`  
* `git push -u origin main`  


## Add, rename, remove, push
To check status: `git status`  
To add file: `git add filename`  
To add all files: `git add --all`  
To remove file: `git rm filename`  
To rename file: `git mv oldfilename newfilename`  
To add commit message (applies to all staged files): `git commit -m "Message"`  
To push commits to remote repo: `git push`  

## Undo git command  
To unstage specific uncommitted file: `git reset filename`  
To unstage all uncommitted files: `git reset`  

## Git fetch v.s. git pull  
`git fetch` downloads remote data, but doesn't integrate it with your files - it gives you a fresh view but is totally "harmless", won't affect local stuff.  
`git pull` updates your local files with changes from the remote server, integrating it with the working copies of your files (and will try to merge remote changes in merge conflicts) - so should not do this when you have uncommitted local changes.   

## Branches and versions
To view branches (current branch marked with star): `git branch`  

To create new branch:
```
git branch branchname
git push --set-upstream origin branchname
```  

To switch branches: `git checkout branchname`  

To delete remote branch: `git push origin --delete branchname`  
To delete local branch: `git branch -d branchname`  

To check for different between local and remote file:  
`git fetch origin branchname`  
`git diff origin/branchname -- filename`  

To merge dev branch with main branch, push, then return to dev:  
```
git checkout main
git merge dev
git push
git checkout dev
```  

To move to main branch and force local files to match main (loses unstaged commits):  
*Not sure this is best way! Need to investigate more*  
`git checkout main`  
`git fetch`  
`git reset --hard origin/main`  

## Commits  
To view commit history: `git log`  
To return to a previous commit: `git reset 7111dce4748bb213ede5a43912889a350355039a` - but then I was at that commit but with unstaged changes, so I returned by doing `git reflog` to see where I wanted to return to, then `git reset HEAD@{1}` to get back to head.  
Never quite figured out... stopped needing it... jot down if figure out next time...  
I also tried these but they were the right thing either:  
* `git revert 7111dce4748bb213ede5a43912889a350355039a`  
* git checkout 7111dce4748bb213ede5a43912889a350355039a` ... but this means in detatched head state... so still not super certain regarding this...)... if you make changes but want to get rid of them and return, `git checkout branchname -f` to force it  

## Public v.s. private repositories  
Nobody can push to public repository until you add them as collaborator.