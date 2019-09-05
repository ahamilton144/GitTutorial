# GitTutorial

Tutorial to get CoFIRES up to speed on Git & Github.

Links
- [Git manual](https://git-scm.com/book/en/v1/Git-Basics-Getting-a-Git-Repository)
- Water programming blog posts: [here](https://waterprogramming.wordpress.com/2014/09/29/getting-started-git-and-github/), [here](https://waterprogramming.wordpress.com/2012/10/29/intro-to-git-part-1-local-version-control/), [here](https://waterprogramming.wordpress.com/2012/10/29/intro-to-git-part-2-remote-repositories/).

## Useful commands
Command | Meaning
--------|--------
git checkout *branch_name* | switch to existing branch 
git checkout -b *branch_name* | create new branch and check out
git branch | list all local branches. current branch has asterisk.
git brach -d *branch_name* | delete local branch. Use -D flag to force delete of unsaved changes.
git status | show current state of working tree, which has all changes relative to last commit. Changes in green have already been added to stage, but still awaiting commit. Changes in red have not been staged yet.
git add *file_name* | add changes in *file_name* to stage
git add . | add all uncommitted changes in current directory (recursive) to stage
git rm --cached *file_name* | remove file from git repo/staging area, so it will no longer be tracked.
git reset HEAD *file_name* | unstage changes to *file_name*, but keep changes to working tree
git reset --soft HEAD^ | undo last commit, but keep all the changes to working tree
git reset --hard | reset working tree to last commit. BE CAREFUL, this actually deletes the changes you have made!
git stash | save local changes to working tree to a "stash", and revert working tree to last commit. This lets you switch between branches without having to commit first. Note the stash number in output.
git stash apply stash@{#} | reapply changes that were previously stashed to working tree. Replace {#} in command with the stash number.
git commit -m "*message*" | commit all staged changes, which will create a new "node" in version control history. Add a short message  to the commit, in quotes. No need to add date or user name, this will be automatically recorded.
git log -n *N* | Output log of last *N* commits
git push | push most recent commit of current local branch to its already existing remote  branch
git push --set-upstream origin *branch_name* | create a branch *branch_name* in remote repo that is identical to current local branch
git pull | pull updated version of remote branch into local branch
git merge *other_branch* | if *current_branch* is checked out, merge commits from *other_branch* into *current_branch*
git merge --abort | abort a failed merge
