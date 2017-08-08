<!--
.. title: dyld: Library Not Loaded: @executable_path/../.Python
.. slug: python-library-not-loaded
.. date: 2017-08-07 16:39:43 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

I have always been a fan of virtualenv and virtualenvwrapper.  It is nice to be able to isolate development environments for each of my python projects.  

However some of the projects I work on aren't python projects.  It could be R, it could be iPython Jupyter notebook.   That means I could be away from meddling with any of the python virtual environments for a while.  And if I 'accidentally' updated my native python version on my MacOS machine, I would see the error as such "dyld: Library Not Loaded: @executable_path/../.Python".  

After googling around, the solutions out there are either to start from scratch and recreate a new virtual environments or to go through the some steps to recreate the links from the virtual environments to the new version and paths of python.  

I tried both ways, and I really can't tell which is easier.  Ultimately, after recreating the links or recreate a project, one will still have to re-install all the packages needed for the project.  I would love the ability to freeze requirements into a requirements.txt, but even that will require a working python virtualenv and pip.  Typical chicken and egg problem.  

Anyway, for the sake of future reference, I thought it would be good to type out all the command lines to recreate the links:

```
$ cd {python virtualenv folder}
$ find {broken virtualenv}/ -type l         ## to list out all the links
$ deactivate ## Optional, deactivate if virtualenv is active
$ find {broken virtualenv}/ -type l -delete ## to delete the broken links
$ virtualenv {broken virtualenv} --python=python3   ## recreate links to OS's python
$ workon {broken virtualenv} ## activate and workon the fixed virtualenv
$ pip3 install  ... {other packages required for the project}

```

All that said, **NOTE TO SELF**:
### REMEMBER TO PIP FREEZE REQUIREMENTS.TXT BEFORE UPGRADING SYSTEM'S PYTHON.    
