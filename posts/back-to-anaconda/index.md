<!--
.. title: Back to Anaconda
.. slug: back-to-anaconda
.. date: 2017-08-15 10:20:58 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

It was last year that I first heard of Anaconda, iPython (currently known as Jupyter) Notebook, etc... It didn't make sense to me back then, mind you it is a mighty and powerful platform.  I felt a bit overwhelmed then.  But today as I revisit the [Anaconda](https://www.continuum.io/) website and [Jupyter](http://jupyter.readthedocs.io/en/latest/) (formerly iPython) website, reading the documents again, it sort of makes sense now.  

What prompted me to revisit Anaconda, and Jupyter Notebook?  I am kind of looking for a "one tool does all" environment for data science project that accommodate the use of python and R.  I have been using homebrew with pip, virtualenv, virtualenvwrapper to manage development environment and packages for python projects; and RStudio for R projects.  It is sort of redundant to set up different environments, use different package manager and learn two different tools to do any kind of data science work at all.

So here we are.  The set up for Anaconda is pretty straight forward and there are tons of documentations out there.  Here is a simplified short list of steps:      

1. Go to [Download](https://www.continuum.io/downloads) page on [Anaconda](https://www.continuum.io/) home page.
2. Choose the download that is suitable for your platform:    
3. Install by double clicking the installer package, or type `bash AnacondaX.Y.Z-XXX.sh` if you downloaded the bash installer script instead.  
4. Once installation is completed, we could move on to using the terminal/bash. Type in `conda update conda` and `conda update anaconda` to make sure packages at root are up-to-date.  
5. Sometimes packages or library that comes with anaconda might be out of date, you can update by `conda update scikit-learn` or `conda install -c anaconda scikit-learn=X.XX.X`.  

One thing I noticed was the project-env hook that virtualenvwrapper offers.  When I typed `workon XXXenv`, the virtual environment of XXX will be activated, and I was also redirected to the project directory.  This is convenient, if we have 1-to-1 match of project and virtualenv setups, which was mostly the case for me.  Note that this is not a fixed/default setup, I just happened to like it this way.  

I guess the advantage of anaconda is one could set up an environment once and share it across projects that uses similar libraries or packages.  

TODO: Explore anaconda-project.  
