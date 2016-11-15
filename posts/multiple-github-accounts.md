<!--
.. title: Setting Up Multiple GitHub User Account on One Machine
.. slug: multiple-github-accounts
.. date: 2016-11-15 12:39:45 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

It is not unusual that developers need multiple github accounts on a single machine.  I was looking through the resources on the internet and found [this](https://gist.github.com/jexchan/2351996/) the most useful.  None the less, I decided to write a post about this, just so for my own references.  

Here are the steps:
- Create the users (however many you need) on [github](https://github.com/) first.     


- Use `ssh-keygen` to generate various ssh keys.  When prompted, make sure the keys are named appropriately so they can be identified easily.     
```
ssh-keygen -t rsa -C "{email1@youremail1.com}"
ssh-keygen -t rsa -C "{email1@youremail1.com}"
```
Make sure emails used are the ones you used for creating the github accounts.    

Usually ssh keys are stored under `home/{username}/.ssh` folder (or `/Users/{username}/.ssh` if you are on mac).  For example, the following keys are generated:    
```
~/.ssh/id_rsa_{git_username1}
~/.ssh/id_rsa_{git_username2}
```


- Add the keys to SSH to the SSH Agent on the system:     
```
ssh-add ~/.ssh/id_rsa_{git_username1}
ssh-add ~/.ssh/id_rsa_{git_username2}
```
To delete ALL previously added keys:    
```
ssh-add -D
```
To delete a previously added key:    
```
ssh-add -d {id_rsa_keyname}
```
To list ALL previously added keys:    
```
ssh-add -l
```    


- The public keys need to be added to the github accounts accordingly.  
```
pbcopy < ~/.ssh/id_rsa_{git_username1}.pub
```
Paste the content to corresponding [github SSH key management](https://github.com/settings/keys).     
Repeat for all other keys for other accounts.     


- Configure SSH config
```
cd ~/.ssh/
nano config
```    


- Add the following lines, modify accordingly:
```
# github_{user1} account
Host github.com-{user1}
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_{git_username1}
    IdentitiesOnly yes

# github_{user2} account
Host github.com-{user2}
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_{git_username2}
    IdentitiesOnly yes
```     


- Manage Global Git Configs.  You may either define those in command line or store them in a .gitconfig_global under     
```
[core]
	   editor = atom -n -w
	   excludesfile = {filepath}/.gitignore_global
[push]
	   default = upstream
[merge]
	   conflictstyle = diff3
[color]
	   ui = true
[user]
	   name = {leave null, define this locally}
	   email = {leave null, define this locally}
```    


- Manage Local Git Configs    
For example, github user1
```
[user]
        name = {github_username1}
        email = {github_email1}
[remote "origin"]
        url = git@github.com-{user1}:{github_username}/{github_repo}
```   
Note that the host in URL has to be the right host defined earlier in the `~/.ssh/config` file.   

The same precaution has to be taken when cloning.  ie when executing `git clone` command, make sure the git host in 'copied and pasted' repo url is edited accordingly to the right user/host.  
