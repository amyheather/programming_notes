# Git

## Conventional commits

VSCode has extension `Conventional Commits` to help with following this criteria.

Format:

```
type(scope): description

body

footer
```

If you have a breaking change (correlates with `major` in semantic versioning) you need to:
* Add a "!" after type/scope
* In footer, have "BREAKING CHANGE: description of change"

Type (mandatory):

| Type | Summary | Description |
| --- | --- | --- |
| `style` | Styles | Commit doesn't affect meaning (white-space, formatting, missing semi-colons, etc.) |
| `docs` | Documentation | Commit affects documentation only (correlates with `patch` in semantic versioning) |
| `refactor` | Code refactoring | Commit rewrites/restructures code but doesn't change expected behaviour of code |
| `perf` | Performance improvements | Commit rewrites/restructures code to improve performance (but doesn't change expected behaviour of code) |
| `improvement` | Improvement | Commit improves current implementation without adding new feature or fixing bug (would have no effect on semantic versioning) |
| `feat` | Features | New feature | Commit adds new feature (correlates with `minor` in semantic versioning) (whilst keeping backward compatability) |
| `fix` | Bug fixes | Bug fix | Commit fixes bug (correlates with `patch` in semantic versioning) |
| `test` | Test | Commit adds or amends tests |
| `build` | Builds | Commit affects build system or external dependencies (e.g. adding, removing, upgrading dependencies) |
| `ops` | Operational | Commit affects operational components (e.g. infrastructure, deployment, backup, recovery) |
| `chore` | Chores | Miscellanous commit (e.g. modifying `.gitignore`, regenerating generated code, releasing product) |
| `revert` | Reverts | Revert to old commit |
| `ci` | Continuous integrations (CI) | Commit changes CI files (e.g. Travis) |

Scope (optional)

Description (mandatory)
* Concise description of change in present tense
* Don't capitalise first letter, and no dot (`.`) at end

Body (optional)
* Motivation for change and contrast with previous behaviour, in present tense
* Must have one blank line before

Footer (optional)
* Must have one blank line before
* Should include issue ref (e.g. `Fixes: #13`). As long as you use one of GitHub's key words, it will automatically create a link. (`close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves`, `resolved`). If for a commit in a different repository, then e.g. `Resolves: neudesic/projectcenter#22`
* Should only include BREAKING CHANGE, external links, issue references, and other meta-information

Examples:

```
fix: add missing parameter to service call

The error occurred because of <reasons>.
```

```
feat!: remove ticket list endpoint

refers to JIRA-1337

BREAKING CHANGES: ticket enpoints no longer supports list all entites.
```

```
feat(shopping cart): add the amazing button
```

Sources:
* <https://kapeli.com/cheat_sheets/Conventional_Commits.docset/Contents/Resources/Documents/index>
* <https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13>
* <https://www.conventionalcommits.org/en/v1.0.0-beta.2/>
* <https://medium.com/neudesic-innovation/conventional-commits-a-better-way-78d6785c2e08>

## Download folder from a GitHub repository

Replace `.com` in the URL with `.dev`. This will open an editor, where you can then right click the folder in the sidebar and select download.

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
To unstage latest commmit: `git reset HEAD^`

## Track large file

Git will give warning for file over 50MB and block file over 100MB. However, you can track (as long as not too big)...
* Install git-lfs `sufo apt-get install git-lfs`
* Initialise in repository `git-lfs install`
* Set tracking of a particular file `git lfs track 'filename.csv'`
* Can then git add and commit that file
* Recommended that you also add the .gitattributes file produced

## Tags

Tag an old release: `git tag tagname commit` e.g. `git tag v0.1.0 f94e8f6`

Push tag to remote: `git push origin v0.1.0`

View date of tag (i.e. date of commit that was tagged): `git log -1 --format=%ai v0.1.0`

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

To remove listing of remote branches that have actually been removed: `git remote prune origin`

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

## Git stash

If you have local uncommitted changes, and realise you are not working on the right branch, you can resolve this using git stash...

```
git stash
git checkout branchname
git stash apply
```

If there are differences, a merge conflict will appear, and you can resolve using conflict editor in VS Code which shows you the two versions and changes on each line, and as you accept one or the other, it shows you the end result from that.

## Git fork

If you fork a repository and want to push changes to a branch other than main, switch to that branch in the forked repository and make the changes there.

## Commits  
To view commit history: `git log`  
To return to a previous commit: 
```
git revert --no-commit 65f8ed3..HEAD
git commit -m "Revert back as removing ambulance filters results in heavily skewed means"
git push
```

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

## Public v.s. private repositories  
Nobody can push to public repository until you add them as collaborator.