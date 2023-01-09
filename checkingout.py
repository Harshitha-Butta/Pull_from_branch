import git 
from git import Repo

g=git.cmd.Git('https://github.com/Harshitha-Butta/Pull_from_branch.git')
g.pull()

repo=Repo('C:\git practice\Pull_from_branch')
repo_heads=repo.heads
repo_heads['test'].checkout()
