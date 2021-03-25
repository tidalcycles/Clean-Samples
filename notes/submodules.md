I know the decision hasn't been made yet, but for the sake of testing here's a submodule example

Adding a new a submodule:
```
bernie@jobim:~/source/Clean-Samples$ git submodule add https://github.com/cleary/samples-flbass.git
Cloning into '/home/bernie/source/Clean-Samples/samples-flbass'...
remote: Enumerating objects: 68, done.
remote: Counting objects: 100% (68/68), done.
remote: Compressing objects: 100% (61/61), done.
remote: Total 68 (delta 19), reused 47 (delta 7), pack-reused 0
Unpacking objects: 100% (68/68), 10.41 MiB | 3.48 MiB/s, done.
bernie@jobim:~/source/Clean-Samples$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   .gitmodules
	new file:   samples-flbass

bernie@jobim:~/source/Clean-Samples$ git commit -am 'add flbass as submodule'
[main ceb0ed0] add flbass as submodule
 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 samples-flbass
bernie@jobim:~/source/Clean-Samples$ git push 
Username for 'https://github.com': cleary
Password for 'https://cleary@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 470 bytes | 470.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/cleary/Clean-Samples.git
   d360302..ceb0ed0  main -> main
bernie@jobim:~/source/Clean-Samples$
```

Clone Command needs to change (and should be updated in the README:
```
git clone --recurse-submodules https://github.com/tidalcycles/Clean-Samples.git
```

To update all submodules in the repo, use:
```
git submodule update --remote [--merge]
```

To update a specific submodule in the repo, it's possible but I haven't done it myself explicitly:
https://stackoverflow.com/a/45251405/3164018

