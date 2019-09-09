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

## Tutorial steps
### Config for github
1. `git config --global user.name "John Doe"`

1. `git config --global user.email johndoe@example.com`

### Create repo for existing project
This is when you've been working on a project on your local computer and you want to make a repository on Github for it. Follow instructions [here](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line)

### Clone a repo on github to your local computer
This is when there is an online repo (either one of yours, or someone else's repo you plan to contribute to) that you want to download onto your own computer. Follow instructions [here](https://help.github.com/en/articles/cloning-a-repository).

### Branches, file structure, and project development
Generally it is best practice (especially when co-developing with a team) not to make changes directly to the Master branch. Rather, each team member who is working on a different set of changes should create their own working branch. Once a set of changes is finalized, the changes are merged into the master branch. Git streamlines the merge process so that different team members don't have to manually add changes made by others into their own changes, which can lead to major headaches.

[Here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) and [here](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) together are a great description of how Git stores the files in your project and handles changes between branches and commits. While some version control systems track *changes* to your files, Git operates with *snapshots*. You can think of the version control system as a tree, with different branches branching off of the master branch. When the working branch is merged back into the master, the tree branches merge back together. Each time you *commit* a set of changes to whatever branch you are on, Git stores a new snapshot of the project. For files that are unchanged since the last commit, Git just stores a pointer to the last update of that file. For files that are new or changed, the commit will store the new updated version of the file. This means that Git generally only "adds" to the project, rather than deleting files & changes, which means that in general there is a way to go back and retrieve an earlier version of a file if you mess something up.

Your *working tree* is the current state of your directory. If you have just *checked out* a particular branch, and not made any changes yet, then your working tree will be identical to the last commit on that branch. Once you make changes (add new files, delete files, or modify files), then your working tree is different from the last commit (remember, a commit is just a snapshot of the file system). You can check the state of your working tree using the command

`git status`

Now once you have a set of changes that you want to commit (i.e. add a new node on the branch), you first have to add all your working tree changes to the *staging area*. You do this with

`git add`*`file`* for a particular file, or `git add .` for all files

Next, we commit the changes using

`git commit -m "`*`message`*`"`

When possible, it is good to have multiple commits on your local working branch, denoting discrete new functionalities, bug fixes, etc., added to the project. Whenever you are ready to add the changes back into the master branch, the first step is to *push* your local branch to the online repository. If my branch is called *andrew_working*, and I have never pushed this particular branch to the remote repo before, then I run the command

`git push --set-upstream origin`*`andrew_working`*

If I have previously pushed *andrew_working* to the remote repo, so that there is already a branch with this name in the repo, then I can simply run

`git push`

Now we want to merge our working directory into the master branch. To do this, log into the browser version of [Github](https://github.com/) and navigate to the repository that you are working on (in this case, GitTutorial). You
