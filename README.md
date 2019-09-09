# GitTutorial

Tutorial to get CoFIRES up to speed on Git & Github.

## Other useful links
- [Super basic intro](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Git manual](https://git-scm.com/book/en/v1/Getting-Started-Git-Basics)
- [Tutorials from Github](https://lab.github.com/)
- Water programming blog posts: [here](https://waterprogramming.wordpress.com/2014/09/29/getting-started-git-and-github/), [here](https://waterprogramming.wordpress.com/2012/10/29/intro-to-git-part-1-local-version-control/), [here](https://waterprogramming.wordpress.com/2012/10/29/intro-to-git-part-2-remote-repositories/).

## Useful commands
Command | Meaning
--------|--------
`git checkout *branch_name*` | switch to existing branch 
`git checkout -b *branch_name*` | create new branch and check out
`git branch` | list all local branches. current branch has asterisk.
`git brach -d *branch_name*` | delete local branch. Use -D flag to force delete of unsaved changes.
`git status` | show current state of working tree, which has all changes relative to last commit. Changes in green have already been added to stage, but still awaiting commit. Changes in red have not been staged yet.
`git add *file_name*` | add changes in *file_name* to stage
`git add .` | add all uncommitted changes in current directory (recursive) to stage
`git rm --cached *file_name*` | remove file from git repo/staging area, so it will no longer be tracked.
`git reset HEAD *file_name*` | unstage changes to *file_name*, but keep changes to working tree
`git reset --soft HEAD^` | undo last commit, but keep all the changes to working tree
`git reset --hard` | reset working tree to last commit. BE CAREFUL, this actually deletes the changes you have made!
`git stash` | save local changes to working tree to a "stash", and revert working tree to last commit. This lets you switch between branches without having to commit first. Note the stash number in output.
`git stash apply stash@{#}` | reapply changes that were previously stashed to working tree. Replace {#} in command with the stash number.
`git commit -m "*message*"` | commit all staged changes, which will create a new "node" in version control history. Add a short message  to the commit, in quotes. No need to add date or user name, this will be automatically recorded.
`git log -n *N* `| Output log of last *N* commits
`git push `| push most recent commit of current local branch to its already existing remote  branch
`git push --set-upstream origin *branch_name*` | create a branch *branch_name* in remote repo that is identical to current local branch
`git pull` | pull updated version of remote branch into local branch
`git merge *other_branch*` | if *current_branch* is checked out, merge commits from *other_branch* into *current_branch*
`git merge --abort` | abort a failed merge

## Config for github
1. `git config --global user.name "John Doe"`

1. `git config --global user.email johndoe@example.com`

## Create repo for existing project
This is when you've been working on a project on your local computer and you want to make a repository on Github for it. Follow instructions [here](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line)

## Clone a repo on github to your local computer
This is when there is an online repo (either one of yours, or someone else's repo you plan to contribute to) that you want to download onto your own computer. Follow instructions [here](https://help.github.com/en/articles/cloning-a-repository).

## Branches, file structure, and project development in Git
[Here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) and [here](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) together are a great description of how Git stores the files in your project and handles changes between branches and commits. While some version control systems track *changes* to your files, Git operates with *snapshots*. You can think of the version control system as a tree, with different branches branching off of the master branch. When the working branch is merged back into the master, the tree branches merge back together. Each time you *commit* a set of changes to whatever branch you are on, Git stores a new snapshot of the project. For files that are unchanged since the last commit, Git just stores a pointer to the last update of that file. For files that are new or changed, the commit will store the new updated version of the file. This means that Git generally only "adds" to the project, rather than deleting files & changes, which means that in general there is a way to go back and retrieve an earlier version of a file if you mess something up.

One common source of confusion occurs when new Git users attempt to find the different project branches in their file system. In your Windows File Explorer (or Mac or Linux equivalent), you won't find separate folders for each branch. Rather, you will just find a single project directory, and the files in that directory will correspond to the versions in the branch that is currently *checked out*. For example, if the master branch is checked out, then only the files that are part of the master branch will show up in the folder, and if you open a file in Notepad or PyCharm, it will show you the version from the master branch. If you then check out a different branch, all files will magically change to reflect the new branch.

## Local branches and changes
Generally it is best practice (especially when co-developing with a team) not to make changes directly to the master branch. Rather, each team member who is working on a different set of changes should create their own working branch. Once a set of changes is finalized, the changes are merged into the master branch. Git streamlines the merge process so that different team members don't have to manually add changes made by others into their own changes, which can lead to major headaches.

First, create a local working branch (e.g. *andrew_working*) and *checkout* the branch.

`git checkout -b`*`andrew_working`*

Now your *working tree* is the current state of your directory. If you have just *checked out* a particular branch, and not made any changes yet, then your working tree will be identical to the last commit on that branch. Once you make changes (add new files, delete files, or modify files), then your working tree is different from the last commit (remember, a commit is just a snapshot of the file system). You can check the state of your working tree using the command

`git status`

Now once you have a set of changes that you want to commit (i.e. add a new node on the branch), you first have to add all your working tree changes to the *staging area*. You do this with

`git add`*`file`* for a particular file, or `git add .` for all files

Next, we commit the changes using

`git commit -m "`*`message`*`"`

When possible, it is good to have multiple commits on your local working branch, denoting discrete new functionalities, bug fixes, etc., added to the project. 

## Pushing changes to online repository
Before you can merge your changes into the master branch, you need to add your changes to the online repository. The online repo can also serve as backup for changes on your local machine, even if you are not ready to merge the changes into the master branch. I recently had to take my computer in for repairs, and I was glad that I had recently pushed my changes to the cloud so that I could download my repo on a loaner computer and get back to work. The first step is to *push* your local branch to the online repository. If my branch is called *andrew_working*, and I have never pushed this particular branch to the remote repo before, then I run the command

`git push --set-upstream origin`*`andrew_working`*

If I have previously pushed *andrew_working* to the remote repo, so that there is already a branch with this name in the repo, then I can simply run

`git push`

## Pull requests and merging changes into the master branch
Now we want to merge our working directory into the master branch. To do this, log into the browser version of [Github](https://github.com/) and navigate to the repository that you are working on (in this case, GitTutorial). If you click where it says "2 branches" (or more if there are multiple working branches in your project), you will see your working branch. Click "New pull request", which will activate a request for the master branch to *pull* your changes, so that they become part of the master branch. Remember that this pull request includes one or more commits from your local branch - everything that you have changed since you first branched off the the master branch. Now give the pull request a name (the default is the last commit message on your working branch), leave a comment if you want to tell your collaborators (or your future self) what was in this pull request, and click "Create pull request".

If you are not an administrator to the repository (e.g. you are suggesting a change to an open source project), then this is all you can do. It is now up to the administrator to accept or deny your pull request. But if you are an administrator, the next step is the *merge*. If you are the only person that has made changes on the master branch, so that the current master branch is identical to the branch from which you created your working branch, then it will tell you that there are no merge conflicts. You can hit "Merge pull request" and then "Confirm merge" to safely and automatically add your changes on top of the master branch. 

However, if multiple people are co-developing, it will sometimes be the case that there are merge conflicts. This occurs when someone else has pushed changes to the master branch in between the time when you first created your branch and the current moment. If that person made changes to similar parts of a file which you have also made changes to, then Git will ask you to manually merge the files. This is easiest done in the Github browser, in my opinion. After you create the pull request, it will tell you that the branch has conflict, and you can click "Resolve conflicts." This will take you to an online merge tool, with one tab for each file that has merge conflicts. Merge conflicts are marked as follows:

```
<<<<<<< andrew_working
code from andrew_working 
=======
code from master
>>>>>>> master
```

For each merge conflict (there may be multiple conflicting sections in any given file), the conflicting code from the working branch is shown in the first section and the code from the master branch is shown in the second section. To resolve the merge conflict, you should manually remove everything except the correct block of code that should be included in the new, merged version of the master branch. This merged block can be the code from the working branch, the code from the master branch, or some combination of the two. Once you have done this for all conflicts within a file, you can click "Mark as resolved," and once you have resolved the conflicts from each file, you can click "Commit merge".  

Once the conflicts have been resolved, you can "Merge pull request" to create a new commit that includes the newest conflict-free changes. Then you "Confirm merge" to add these changes into the master branch.

## Updating your local repository
Once the pull request and merge has been completed, you can safely delete the working branch from the online repository. Next, we want to update your local repository to reflect the newest version of the master branch. Back in Git Bash or Cygwin, we can run

`git checkout master`

`git pull`

to checkout the master branch and *pull* the newest version from the online repository. Now that our master branch contains the changes which we had previously made on our working branch (along with potentially any changes made by other co-developers), we should delete the working branch

`git branch -d`*`andrew_working`*

Assuming your working tree does not contain any changes since your last commit on *andrew_working*, then this command will work fine. But if you have made changes, then it will throw an error. You can use the `-D` flag instead of `-d` if you no longer need those changes and want to delete them along with the branch. Alternatively, you can [*stash* the changes](https://www.atlassian.com/git/tutorials/saving-changes/git-stash), which removes them from your working tree but stores the changes so that you can reapply them to another branch later. 

Lastly, we want to create and checkout a new working branch so that we can begin making our next set of changes. Thus we circle back to the **Local branches and changes** section and begin again, starting with 

`git checkout -b`*`andrew_working`*

## Comparing different branches using Meld
Because Git does not actually store each different branch in its own directory, it can be difficult to compare the differences between files. The simplest way to do a quick comparison is with the *diff* tool

`git diff andrew_working:main.py master:main.py > changes.diff`

This will compare the versions of the *main.py* file in the working and master branches, and write the output to the file *changes.diff*. If you open this in a program like Notepad++, then lines which are exclusive to *andrew_working* will be preceded by (-) signs, and lines exclusive to *master* will be preceded by (+) signs.

This works well for relatively minor changes, but can be difficult to read for more complex changes. I recommend the program [Meld](https://meldmerge.org/) which can show you convenient side-by-side comparisons with difference highlighting. However, it can be a bit tricky to integrate with Git on Windows. With my Cygwin-installed Git, I had to add the following lines to my .gitconfig file, which was located in my Cygwin home directory. If you installed Git using a different method, your .gitconfig file will be located somewhere else, and the path variables below should be adjusted accordingly.

```
[merge]
              tool = meld
[diff]
              tool = meld
[mergetool "meld"]
              path = "/cygdrive/c/Program Files (x86)/Meld/Meld.exe"
[difftool "meld"]
              path = "/cygdrive/c/Program Files (x86)/Meld/Meld.exe"
[difftool]
              prompt = true
```

Lastly, if you have Cygwin's Git, you will probably have to follow Carl's comment at the bottom of [this page](https://helmiagustian.wordpress.com/2014/03/17/install-meld-at-cygwin-as-mergetool/). 

Once you have followed these steps, you can compare the differences between the current working tree and another branch (say, *master*) by typing 

`git difftool master`

Git will find all files which are different between the two branches, and ask you one-by-one whether you want to open that file for comparison in Meld. You can also look at the difference between two different named branches or commits, and can specify a specific file if you don't want to be prompted on all files.

`git difftool working_branch_1 working_branch_2`

`git difftool commit_hash_1 commit_hash_2 main.py`
